import sys
from PyQt5.QtWidgets import *

# This is the default code that we need to use in order
# to build your Application.

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(850, 150, 300, 450)
        self.setWindowTitle("My first window")
        self.show()


if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())