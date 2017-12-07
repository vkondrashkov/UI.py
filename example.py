import UI
from msvcrt import getch

class Application:
    def sayHello(self):
        print('Hello!')
        input('Press any key')

    def sayGoodBye(self):
        print('Good bye!')
        input('Press any key')

    def start(self):
        mainScreen = UI.Screen(width=100, height=20, verticalOffset=2, horizontalOffset=10)
        title = UI.Text('Greet-o-machine')
        
        helloCommand = UI.Command(self, self.sayHello)
        helloButton = UI.Button('Hello', helloCommand)

        goodByeCommand = UI.Command(self, self.sayGoodBye)
        goodByeButton = UI.Button('Good bye', goodByeCommand)

        exitCommand = UI.Command(self, mainScreen.exit)
        exitButton = UI.Button('Exit', exitCommand)

        mainMenu = UI.Menu(helloButton, goodByeButton, exitCommand, horizontalOffset=5)
        menuHandler = UI.MenuHandler(mainMenu)

        mainScreen.appendElement(title)
        mainScreen.appendElement(mainMenu)
        
        mainScreen.start()
        while mainScreen.running:
            mainScreen.draw()
            key = ord(getch())
            menuHandler.handle(key)

app = Application()
app.start()