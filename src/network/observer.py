from abc import ABCMeta, abstractclassmethod


class Observer(metaclass=ABCMeta):
    @staticmethod
    @abstractclassmethod
    def update(self, event):
        """
        implement update operations
        """