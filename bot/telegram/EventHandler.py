from . import (handlers, run_async, td_api, td_execute, td_recieve, td_send,
               td_send_and_receive, threads)


@run_async
def listenToEvents():
    try:
        while True:
            event = td_recieve()
            if event:
                for k, v in handlers.items():
                    if isinstance(event, v):
                        k(event)
    except KeyboardInterrupt:
        for thread in threads:
            thread.kill()
