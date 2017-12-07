from UI.controllers.command import Command
from UI.models.keys import Key
from os import system

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
