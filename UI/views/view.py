from abc import ABCMeta, abstractmethod

class View:
    __metaclass__ = ABCMeta
    @abstractmethod
    def __init__(self, horizontalOffset=0, verticalOffset=0):
        if horizontalOffset > 0:
            self.horizontalOffset = horizontalOffset
        else:
            self.horizontalOffset = 0
        if verticalOffset > 0:
            self.verticalOffset = verticalOffset
        else:
            self.verticalOffset = 0

    @abstractmethod
    def draw(self):
        if self.verticalOffset:
            print('\n' * self.verticalOffset, end='')
        if self.horizontalOffset:
            print(' ' * self.horizontalOffset, end='')