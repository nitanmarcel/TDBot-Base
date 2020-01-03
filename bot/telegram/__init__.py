import inspect
import json
import os
from ctypes.util import find_library
from ctypes import *
from functools import wraps
from queue import Queue
from threading import Thread

from bot.custom import errors

from . import td_api

threads: list = list()


def run_async(func):
    @wraps(func)
    def async_func(*ar, **kw):
        queue = Queue()
        func_hl = Thread(target=func, args=ar, kwargs=kw)
        threads.append(func_hl)

        func_hl.start()
        func_hl.join()
        if not queue.empty():
            return queue.get()
        return func_hl

    return func


def on_event(event: td_api.Update):
    @run_async
    def decorator(func):
        add_event_handler(func, event)
        return func

    return decorator


handlers = {}


def add_event_handler(callback, event: td_api.Update):
    handlers.update({callback: event})


@run_async
def ClassFactory(item):
    def convert(item):
        if isinstance(item, dict):
            item = {k.replace('@extra', 'extra'): v for k, v in item.items()}
            imp = __import__('bot.telegram.td_api', fromlist=[item['@type']])
            klass = getattr(imp, item['@type'])
            kwargs = {}
            sig = inspect.signature(klass)

            for k, v in sig.parameters.items():
                _get = item.get(k, v.default)
                if isinstance(_get, list):
                    _item = []
                    for x in _get:
                        _item.append(convert(x))
                    kwargs.update({k: _item})
                else:
                    kwargs.update({k: convert(_get)})
            return klass(**kwargs)
        else:
            return item

    return convert(item)



def get_tdjon():
    import os
    if os.path.isfile('tdjson.so'):
        return os.path.join(os.getcwd(), 'bot/telegram/tdjson.so')
    elif os.path.isfile('tdjson.dll'):
        return os.path.join(os.getcwd(), 'bot/telegram/tdjson.dll')
    else:
        return find_library('tdjson')

tdjson_path = get_tdjon()
if tdjson_path is None:
    raise errors.LibraryNotFound('Can\'t find tdjson library', threads)

tdjson = CDLL(tdjson_path)
td_json_client_create = tdjson.td_json_client_create
td_json_client_create.restype = c_void_p
td_json_client_create.argtypes = []

td_json_client_receive = tdjson.td_json_client_receive
td_json_client_receive.restype = c_char_p
td_json_client_receive.argtypes = [c_void_p, c_double]

td_json_client_send = tdjson.td_json_client_send
td_json_client_send.restype = None
td_json_client_send.argtypes = [c_void_p, c_char_p]

td_json_client_execute = tdjson.td_json_client_execute
td_json_client_execute.restype = c_char_p
td_json_client_execute.argtypes = [c_void_p, c_char_p]

td_json_client_destroy = tdjson.td_json_client_destroy
td_json_client_destroy.restype = None
td_json_client_destroy.argtypes = [c_void_p]

fatal_error_callback_type = CFUNCTYPE(None, c_char_p)

td_set_log_fatal_error_callback = tdjson.td_set_log_fatal_error_callback
td_set_log_fatal_error_callback.restype = None
td_set_log_fatal_error_callback.argtypes = [fatal_error_callback_type]


def on_fatal_error_callback(error_message):
    raise errors.TDlibFatalException(
        'TDLib fatal error {error}:'.format(error=error_message))


def cast_to_json(obj):
    if not isinstance(obj, dict):
        _dict = obj.__dict__
        _dict.update({'@type': obj.__tdlib_type__})
        _dict.update({k.replace('_extra', '@extra'): v for k, v in _dict.items()})
    else:
        _dict = obj
    return json.dumps(_dict)


def td_execute(query):
    query = cast_to_json(query)
    result = td_json_client_execute(None, query.encode('utf-8'))
    if result:
        result = json.loads(result.decode('utf-8'))
        result = ClassFactory(result)
    return result


def td_send(query):
    query = cast_to_json(query)
    td_json_client_send(client, query.encode('utf-8'))


def td_recieve():
    result = td_json_client_receive(client, 1.0)
    if result:
        result = json.loads(result.decode())
    return ClassFactory(result)


def td_send_and_receive(query):
    td_send(query)
    return td_recieve()


c_on_fatal_error_callback = fatal_error_callback_type(on_fatal_error_callback)
td_set_log_fatal_error_callback(c_on_fatal_error_callback)

td_execute(td_api.setLogVerbosityLevel(new_verbosity_level=0, extra=1.01234))

client = td_json_client_create()
