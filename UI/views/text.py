from UI.views.view import View

class Text(View):
    def __init__(self, text, horizontalOffset=0, verticalOffset=0):
        View.__init__(self, horizontalOffset, verticalOffset)
        self.text = text
    
    def draw(self):
        View.draw(self)
        print(self.text, end='')