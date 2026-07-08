import sys, random
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFontDatabase, QFont, QIcon, QCursor, QPixmap
from PyQt5.QtCore import QSize, Qt

font = QFont('Playpen Sans', 15)

opt = ['scisor', 'rock', 'paper']

rules = {
    'scisor' : 'paper',
    'rock' : 'scisor',
    'paper' : 'rock'
}

paths = {
    'scisor': r"Course Classes\images\scisor.png",
    'rock': r"Course Classes\images\rock.jpg",
    'paper': r"Course Classes\images\paper.jpg"
}

positionPlayers = {
    'player': 135,
    'computer': 225
}

positionButtons = {
    'scisor': 100,
    'rock': 170,
    'paper': 240
}


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 400, 500)
        self.setWindowTitle("Rock, paper and Scisor game")


        self.setUI()

    def setUI(self):
        # Title
        self.title = QLabel("Rock, Paper and Scisor game", self)
        self.title.setFont(font)
        self.title.move(60, 60)

        # Vs hidden label
        self.vs = QLabel("Vs", self)
        self.vs.move(195, 115)
        self.vs.setFont(font)
        self.vs.hide()

        # Game Setup
        self.gameSetup()

        # Hidden Try Again / Result
        self.tryAgain = QPushButton("Try Again", self)
        self.tryAgain.setFont(font)
        self.tryAgain.move(150, 200)
        self.tryAgain.hide()
        self.tryAgain.clicked.connect(self.tryAgainAct)

        self.result = QLabel("", self)
        self.result.setFont(font)
        self.result.move(160, 165)

        self.show()

    def gameSetup(self):
        self.images = {}
        for player, x in positionPlayers.items():
            for choice, path in paths.items():
                label = QLabel(self)
                label.setPixmap(QPixmap(path))
                label.resize(50, 50)
                label.setScaledContents(True)
                label.move(x, 110)
                label.hide()
                self.images[(player, choice)] = label

            
        self.buttons = {}
        for choice, path in paths.items():
            label = QPushButton(self)
            label.setIcon(QIcon(path))
            label.setIconSize(QSize(50, 50))
            label.setFlat(True)
            label.setCursor(QCursor(Qt.PointingHandCursor))
            label.move(positionButtons[choice], 200)
            label.clicked.connect(lambda checked, c=choice: self.game(c))
            self.buttons[choice] = label

    def game(self, choice:str):
        # Computer's Hand
        i = random.randint(0, 2)
        cmpChoice = opt[i]

        # Showing both hand
        self.images[('player', choice)].show()
        self.images[('computer', cmpChoice)].show()
        self.vs.show()
        
        # Hiding option buttons
        for button in self.buttons.values():
            button.hide()

        # Showing hidden try again button
        self.tryAgain.show()

        # Game Result    
        if choice == cmpChoice:
            self.result.setText("   Draw!")
            self.result.adjustSize()
        
        elif choice != rules[cmpChoice]:
            self.result.setText("You Win!")
            self.result.adjustSize()

        else:
            self.result.setText("You Lost!")
            self.result.adjustSize()

        self.result.show()

    def tryAgainAct(self):
        for image in self.images.values():
            image.hide()

        for button in self.buttons.values():
            button.show()

        self.tryAgain.hide()
        self.vs.hide()
        self.result.hide()


def main():
    App = QApplication(sys.argv)

    # Adding a new font (a cool one)
    QFontDatabase.addApplicationFont(r"Course Classes\Section 2\fonts\PlaypenSans-VariableFont_wght.ttf")

    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()