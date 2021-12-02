from abc import ABCMeta, abstractmethod

class Handler(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def setNext(self, nextHandler):
        """Set the next handler in the chain"""

    @staticmethod
    @abstractmethod
    def handle(self, request):
        """Handle the event"""