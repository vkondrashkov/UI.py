from abc import ABCMeta, abstractmethod

class Command:
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, app, executeCommand=None, argumentList=[]):
        self.argumentList = []
        self.app = app
        if executeCommand:
            self.execute = executeCommand
        for argument in argumentList:
            self.argumentList.append(argument)
    
    @abstractmethod
    def execute(self, argumentList=[]):
        pass