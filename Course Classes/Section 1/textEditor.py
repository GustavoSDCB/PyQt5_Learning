import sys
from PyQt5.QtWidgets import QTextEdit, QApplication, QWidget, QPushButton
from PyQt5.QtGui import QFont

font = QFont("Times", 10)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle("Text Editor")

        self.setUI()

    def setUI(self):
        # Text Editor
        self.textEditor = QTextEdit(self)
        self.textEditor.move(1, 30)
        self.textEditor.setFont(font)

        # Text Editor accepts rich texts by default, but we can change it using the following command
        self.textEditor.setAcceptRichText(False)
        # Rich texts are texts that contain different types of formating (Bold, italic, different font/font size...)
        
        # Send Button
        self.sendBtn = QPushButton("Send", self)
        self.sendBtn.move(300, 100)
        self.sendBtn.clicked.connect(self.sendAct)

        self.show()

    def sendAct(self):
        value = self.textEditor.toPlainText()
        print(value)


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
