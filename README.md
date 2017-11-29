# UI.py
Simple UI module for Python

## Installation
1. Clone repository from GitHub
2. Place UI.py file with your program
3. Then write such code line:
```Python
import UI
```

## How to use
The following example creates presized screen with some text labels
```Python
import UI

hello = UI.Text('Hello', verticalOffset=2)
world = UI.Text('World!', horizontalOffset=5)

mainScreen = UI.Screen(hello, world, horizontalOffset=5, width=30, height=10)
mainScreen.draw()
```

## Opportunities
You can create some objects, such as:
1. Screens, use them when you need to combine any objects.
```Python
mainScreen = UI.Screen(width=120, height=30)
anotherScreen = UI.Screen(verticalOffset=5, horizontalOffset=10)
```
2. Labels or text
```Python
hello = UI.Text('Hello', verticalOffset=5)
world = UI.Text('World', horizontalOffset=10)
```
3. Buttons, to use buttons you have to create Commands and combine buttons in Menu
```Python
command1 = UI.Command(application, method)
button1 = UI.Button('Button', command1)
```
4. Menu and MenuHandler, Menu handler helps you to control your menu
```Python
command1 = UI.Command(application, method)
button1 = UI.Button('Button1', command1)
command2 = UI.Command(application, method)
button2 = UI.Button('Button2', command2)

menu = UI.Menu(button1, button2)
# You can change keys by adding arguments in constructor
# menuHandler UI.MenuHandler(menu, goUpKey=119) # W letter
menuHandler = UI.MenuHandler(menu)

menuHandler.hanlde(key)
```

## Small example of code
Creates small application with little menu:
```Python
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

        mainMenu = UI.Menu(helloButton, goodByeButton, horizontalOffset=5)
        menuHandler = UI.MenuHandler(mainMenu)

        mainScreen.appendElement(title)
        mainScreen.appendElement(mainMenu)
        mainScreen.start()
        while mainScreen.running:
            mainScreen.draw()
            key = ord(getch())
            menuHandler.handle(key)

app = Application()
app.start()```
