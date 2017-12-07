from UI.controllers.command import Command
from UI.views.text import Text

class Button(Text, Command):
    def __init__(self, text, command=None, horizontalOffset=0, verticalOffset=0):
        Text.__init__(self, text, horizontalOffset, verticalOffset)
        if command:
            Command.__init__(self, command.app, command.execute, command.argumentList)
        self.isSelected = False

    def draw(self):
        Text.draw(self)
        if self.isSelected:
            print('> {}'.format(self.text), end='')
        else:
            print('  {}'.format(self.text), end='')