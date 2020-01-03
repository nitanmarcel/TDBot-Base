import json


class BaseTdException(Exception):
    def __kill_threads__(self, threads: list):
        for thread in threads:
            thread.kill()


class LibraryNotFound(BaseTdException):
    def __init__(self, message: str, threads: list):
        self.message = message
        self.__kill_threads__()
        super(LibraryNotFound, self).__init__(message)


class TDlibFatalException(BaseTdException):
    def __init__(self, message: str, threads: list):
        self.message = message
        self.__kill_threads__(threads)
        super(TDlibFatalException, self).__init__(message)


class TdError(BaseTdException):
    def __init__(self, js_error):
        self.__dict__ = json.loads(js_error) if not isinstance(
            js_error, dict) else js_error
        self.type = getattr(self, '@type', None)
