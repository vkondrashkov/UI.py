from UI.views.view import View
from os import system

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