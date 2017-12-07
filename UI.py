# UI.py - simple UI module for Python
#
# Version:  1.1
# Author:   declipz 
# Date:     29.11.2017

from abc import ABCMeta, abstractmethod
from os import system
from math import ceil

class Key:
    arrowUp = 72
    arrowDown = 80
    arrowLeft = 75
    arrowRight = 77
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
            print('> {} '.format(self.text), end='')
        else:
            print('  {} '.format(self.text), end='')

class Menu(View):
    def __init__(self, *args, itemsInRow = 1, horizontalOffset=0, verticalOffset=0):
        View.__init__(self, horizontalOffset, verticalOffset)
        self.menuItems = []
        self.itemsInRow = itemsInRow
        self.currentRow = 0
        self.currentColumn = 0
        for item in args:
            self.menuItems.append(item)
        if self.menuItems:
            self.menuItems[0].isSelected = True
    
    def select(self):
        index = self.currentRow * self.itemsInRow + self.currentColumn
        menuItem = self.menuItems[index]
        if menuItem.argumentList:
            menuItem.execute(menuItem.argumentList)
        else:
            menuItem.execute()

    def goLeft(self):
        if self.currentColumn == 0:
            return
        index = self.currentRow * self.itemsInRow + self.currentColumn
        self.menuItems[index].isSelected = False
        self.currentColumn -= 1
        self.menuItems[index - 1].isSelected = True

    def goRight(self):
        if self.currentColumn == self.itemsInRow - 1:
            return
        index = self.currentRow * self.itemsInRow + self.currentColumn
        if index == len(self.menuItems) - 1:
            return
        self.menuItems[index].isSelected = False
        self.currentColumn += 1
        self.menuItems[index + 1].isSelected = True

    def goUp(self):
        if self.currentRow == 0:
            return
        index = self.currentRow * self.itemsInRow + self.currentColumn
        self.menuItems[index].isSelected = False
        self.currentRow -= 1
        index = self.currentRow * self.itemsInRow + self.currentColumn
        self.menuItems[index].isSelected = True

    def goDown(self):
        if self.currentRow == ceil(len(self.menuItems) / self.itemsInRow) - 1:
            return
        predictedIndex = (self.currentRow + 1) * self.itemsInRow + self.currentColumn
        if predictedIndex > len(self.menuItems) - 1:
            return
        index = self.currentRow * self.itemsInRow + self.currentColumn
        self.menuItems[index].isSelected = False
        self.currentRow += 1
        index = self.currentRow * self.itemsInRow + self.currentColumn
        self.menuItems[index].isSelected = True

    def draw(self):
        if self.verticalOffset:
            print('\n' * self.verticalOffset, end='')
        _positionInRow = 0
        for item in self.menuItems:
            if item.verticalOffset:
                print('\n' * item.verticalOffset, end='')
            if _positionInRow == 0:
                print(' ' * self.horizontalOffset, end='')
            item.draw()
            if _positionInRow == self.itemsInRow - 1:
                print('\n', end='')
                _positionInRow = 0
                continue
            _positionInRow += 1
    
    def appendElement(self, item):
        item.horizontalOffset += self.horizontalOffset
        self.menuItems.append(item)

class MenuHandler(Command):
    def __init__(self, menu, goUpKey=Key.arrowUp, goDownKey=Key.arrowDown, goLeftKey=Key.arrowLeft, goRightKey=Key.arrowRight,executeKey=Key.executeKey, interruptKey=Key.interruptKey):
        self.menu = menu
        self.goUpKey = goUpKey
        self.goDownKey = goDownKey
        self.goRightKey = goRightKey
        self.goLeftKey = goLeftKey
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
        if key == self.goLeftKey:
            self.menu.goLeft()
        if key == self.goRightKey:
            self.menu.goRight()
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
        self.screenContent.append(view)
    
    def start(self):
        self.running = True

    def exit(self):
        self.running = False
        system('cls')