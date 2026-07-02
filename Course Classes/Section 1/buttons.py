import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(999, 250, 300, 300)
        self.setWindowTitle("Implementing a Button")

        self.UI()

    def UI(self):
        self.text = QLabel("My text", self)
        enterButton = QPushButton("Enter", self)
        exitButton = QPushButton("Exit", self)
        enterButton.move(0, 100)
        exitButton.move(80, 100)
        enterButton.clicked.connect(self.enterFunc)
        exitButton.clicked.connect(self.exitFunc)
        self.show()

    def enterFunc(self):
        self.text.setText("This text was changed '-'")
        self.text.resize(150, 20)

    def exitFunc(self):
        self.text.setText("This one does the same, buddy o.o")
        self.text.resize(180, 20)

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == "__main__":
    main()