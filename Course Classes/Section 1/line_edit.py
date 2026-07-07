import sys
from PyQt5.QtWidgets import QLabel, QWidget, QApplication, QLineEdit, QPushButton

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(999, 300, 300, 300)
        self.setWindowTitle("Line Edit Widget")
        self.UI()

    def UI(self):
        self.nameText = QLabel("Name", self)
        self.nameText.move(83, 35)
        self.nameTextBox = QLineEdit("Gustavo", self)
        self.nameTextBox.setPlaceholderText("Type your name")
        self.nameTextBox.move(80, 50)

        self.passwordText = QLabel("Password", self)
        self.passwordText.move(83, 85)
        self.passwordTextBox = QLineEdit(self)
        self.passwordTextBox.setPlaceholderText("Type your password")
        self.passwordTextBox.setEchoMode(QLineEdit.Password)
        self.passwordTextBox.move(80, 100)

        enterButton = QPushButton("Save", self)
        enterButton.move(110, 125)
        enterButton.clicked.connect(self.enterAction)

        self.show()

    def enterAction(self):
        name_value = self.nameTextBox.text()
        pass_value = self.passwordTextBox.text()

        print(f"User name: {name_value} \nUser Password: {pass_value}")
        self.setWindowTitle("You clicked the button, huh? o.o")

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == "__main__":
    main()
