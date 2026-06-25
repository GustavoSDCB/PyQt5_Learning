import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        # Setting up Window
        self.setGeometry(300, 300, 400, 500)
        self.setWindowTitle("Message Box")
        self.setUI()

    def setUI(self):
        self.show()

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_)


if __name__ == '__main__':
    main()