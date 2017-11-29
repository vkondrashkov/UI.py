from abc import ABCMeta, abstractmethod
from os import system

class Key:
    arrowUp = 72
    arrowDown = 80
    interruptKey = 3
    executeKey = 13

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

class Command:
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, app, executeCommand=None, *args):
        self.argumentList = []
        self.app = app
        if executeCommand:
            self.execute = executeCommand
        for argument in args:
            self.argumentList.append(argument)
    
    @abstractmethod
    def execute(self):
        pass
    
class Text(View):
    def __init__(self, text, horizontalOffset=0, verticalOffset=0):
        View.__init__(self, horizontalOffset, verticalOffset)
        self.text = text
    
    def draw(self):
        View.draw(self)
        print(self.text, end='')

class Button(Text, Command):
    def __init__(self, text, command=None, horizontalOffset=0, verticalOffset=0):
        Text.__init__(self, text, horizontalOffset, verticalOffset)
        if command:
            Command.__init__(self, command.app, command.execute, command.argumentList)
        self.isSelected = False

    def draw(self):
        View.draw(self)
        if self.isSelected:
            print('> {}'.format(self.text), end='')
        else:
            print('  {}'.format(self.text), end='')

class Menu(View):
    def __init__(self, *args, horizontalOffset=0, verticalOffset=0):
        View.__init__(self, horizontalOffset, verticalOffset)
        self.menuItems = []
        self.currentRow = 0
        for item in args:
            item.horizontalOffset += self.horizontalOffset
            self.menuItems.append(item)
        self.menuItems[self.currentRow].isSelected = True
    
    def select(self):
        menuItem = self.menuItems[self.currentRow]
        menuItem.execute(menuItem.argumentList)

    def goUp(self):
        if self.currentRow == 0:
            return
        self.menuItems[self.currentRow].isSelected = False
        self.currentRow -= 1
        self.menuItems[self.currentRow].isSelected = True

    def goDown(self):
        if self.currentRow == len(self.menuItems)-1:
            return
        self.menuItems[self.currentRow].isSelected = False
        self.currentRow += 1
        self.menuItems[self.currentRow].isSelected = True

    def draw(self):
        if self.verticalOffset:
            print('\n' * self.verticalOffset, end='')
        for item in self.menuItems:
            item.draw()
            print(end='\n')

class MenuHandler(Command):
    def __init__(self, menu, goUpKey=Key.arrowUp, goDownKey=Key.arrowDown, executeKey=Key.executeKey, interruptKey=Key.interruptKey):
        self.menu = menu
        self.goUpKey = goUpKey
        self.goDownKey = goDownKey
        self.executeKey = executeKey
        self.interruptKey = interruptKey
    
    def handle(self, key):
        if key == self.interruptKey:
            system('cls')
            exit()
        if key == self.goUpKey:
            self.menu.goUp()
        if key == self.goDownKey:
            self.menu.goDown()
        if key == self.executeKey:
            self.menu.select()

class Screen(View):
    def __init__(self, *args, width=120, height=30, horizontalOffset=0, verticalOffset=0):
        View.__init__(self, horizontalOffset, verticalOffset)
        self.screenContent = []
        self.width = width
        self.height = height
        system('mode con cols={} lines={}'.format(self.width, self.height))
        for item in args:
            item.horizontalOffset += self.horizontalOffset
            self.screenContent.append(item)

    def draw(self):
        system('cls')
        if self.verticalOffset:
            print('\n' * self.verticalOffset, end='')
        for item in self.screenContent:
            item.draw()
            print(end='\n')

    def appendElement(self, view):
        view.horizontalOffset += self.horizontalOffset
        if type(view) is Menu:
            for items in view.menuItems:
                items.horizontalOffset += self.horizontalOffset
        self.screenContent.append(view)
    
    def start(self):
        self.running = True

    def exit(self, *args):
        self.running = False
        system('cls')