import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle("Check Boxes")
        
        self.setUI()

    def setUI(self):
        self.name = QLineEdit("Gustavo", self)
        self.name.setPlaceholderText("Type your name")
        self.name.move(180, 50)

        self.surname = QLineEdit("Silva", self)
        self.surname.setPlaceholderText("Type your surname")
        self.surname.move(180, 80)

        self.checkbox = QCheckBox("Remember me", self)
        self.checkbox.move(180, 110)

        submitBtn = QPushButton("Submit", self)
        submitBtn.move(210, 140)
        submitBtn.clicked.connect(self.submit)

        self.show()

    def submit(self):
        "Nothing" if not self.checkbox.isChecked() else print(f"Welcome in {self.name.text()} {self.surname.text()}!")

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()