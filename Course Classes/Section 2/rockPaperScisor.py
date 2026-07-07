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
        self.title.move(60, 1)

        ######### Game Images Setup #########
        self.gameSetUp()

        # Scisor Button
        self.scisorBtn = QPushButton(self)
        self.scisorBtn.setIcon(QIcon(paths['scisor']))
        self.scisorBtn.setIconSize(QSize(50, 50))
        self.scisorBtn.setFlat(True)
        self.scisorBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.scisorBtn.move(100, 200)
        self.scisorBtn.clicked.connect(lambda: self.game('scisor'))

        # Rock Button
        self.rockBtn = QPushButton(self)
        self.rockBtn.setIcon(QIcon(paths['rock']))
        self.rockBtn.setIconSize(QSize(50, 50))
        self.rockBtn.setFlat(True)
        self.rockBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.rockBtn.move(170, 200)
        self.rockBtn.clicked.connect(lambda: self.game('rock'))

        # Paper Button
        self.paperBtn = QPushButton(self)
        self.paperBtn.setIcon(QIcon(paths['paper']))
        self.paperBtn.setIconSize(QSize(50, 50))
        self.paperBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.paperBtn.setFlat(True)
        self.paperBtn.move(240, 200)
        self.paperBtn.clicked.connect(lambda: self.game('paper'))

        self.show()

    def gameSetUp(self):
        # positions = {
        #     'player': 135,
        #     'computer': 185
        # }

        # for player, x in positions.items():
        #     pass


        # Player (scisor, rock, paper)
        self.pScisorImg = QLabel(self)
        self.pScisorImg.setPixmap(QPixmap(paths['scisor']))
        self.pScisorImg.resize(50, 50)
        self.pScisorImg.setScaledContents(True)
        self.pScisorImg.move(135, 110)
        # self.pScisorImg.hide()

        self.pRockImg = QLabel(self)
        self.pRockImg.setPixmap(QPixmap(paths['rock']))
        self.pRockImg.resize(50, 50)
        self.pRockImg.setScaledContents(True)
        self.pRockImg.move(135, 110)
        self.pRockImg.hide()

        self.pPaperImg = QLabel(self)
        self.pPaperImg.setPixmap(QPixmap(paths['paper']))
        self.pPaperImg.resize(50, 50)
        self.pPaperImg.setScaledContents(True)
        self.pPaperImg.move(135, 110)
        self.pPaperImg.hide()

        # Computer (scisor, rock, paper)
        self.cScisorImg = QLabel(self)
        self.cScisorImg.setPixmap(QPixmap(paths['scisor']))
        self.cScisorImg.resize(50, 50)
        self.cScisorImg.setScaledContents(True)
        self.cScisorImg.move(185, 110)
        self.cScisorImg.hide()

        self.cRockImg = QLabel(self)
        self.cRockImg.setPixmap(QPixmap(paths['rock']))
        self.cRockImg.resize(50, 50)
        self.cRockImg.setScaledContents(True)
        self.cRockImg.move(185, 110)
        self.cRockImg.hide()

        self.cPaperImg = QLabel(self)
        self.cPaperImg.setPixmap(QPixmap(paths['paper']))
        self.cPaperImg.resize(50, 50)
        self.cPaperImg.setScaledContents(True)
        self.cPaperImg.move(185, 110)
        self.cPaperImg.hide()

    def game(self, player:str):
        # Computer's Hand
        i = random.randint(0, 2)
        oponent = opt[i]

        # Game setup     
        if player == oponent:
            print(f"Your hand: {player}\nOponent's hand: {oponent}")
            print("Draw!")
        
        elif player != rules[oponent]:
            print(f"Your hand: {player}\nOponent's hand: {oponent}")
            print("You win!")

        else:
            print(f"Your hand: {player}\nOponent's hand: {oponent}")
            print("You lost!")


def main():
    App = QApplication(sys.argv)

    # Adding a new font (a cool one)
    QFontDatabase.addApplicationFont(r"Course Classes\Section 2\fonts\PlaypenSans-VariableFont_wght.ttf")

    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()