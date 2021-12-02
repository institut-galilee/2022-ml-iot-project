from authentication.handler import Handler


class Middleware(Handler):
    def __init__(self):
        self._nextHandler = None

    def setNext(self, nextHandler):
        self._nextHandler = nextHandler
        return nextHandler

    def handle(self, request):
        if (not self._nextHandler):
            return True
        return self._nextHandler.handle(request)