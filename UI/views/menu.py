from UI.views.view import View
from math import ceil

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