import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFontDatabase, QFont

font = QFont('Playpen Sans', 10)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 400, 500)
        self.setWindowTitle("Rock, paper and Scisor game")


        self.setUI()

    def setUI(self):
        self.test = QLabel("Testing new font", self)
        self.test.setFont(font)

        self.show()


def main():
    App = QApplication(sys.argv)

    # Adding a new font (a cool one)
    QFontDatabase.addApplicationFont(r"Course Classes\Section 2\fonts\PlaypenSans-VariableFont_wght.ttf")

    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()