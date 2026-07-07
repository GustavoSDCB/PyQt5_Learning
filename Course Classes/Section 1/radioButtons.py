import sys
from PyQt5.QtWidgets import QLineEdit, QRadioButton, QPushButton, QWidget, QApplication

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 400, 500)
        self.setWindowTitle("Radio Button")

        self.setUI()

    def setUI(self):
        # Name, Surname
        self.name = QLineEdit("Gustavo", self)
        self.name.setPlaceholderText("Type your name")
        self.name.move(130, 20)

        self.surname = QLineEdit("Silva", self)
        self.surname.setPlaceholderText("Type your surname")
        self.surname.move(130, 50)


        # Radio Button
        self.male = QRadioButton("Male", self)
        self.male.setChecked(True)   # Default
        self.male.move(130, 80)

        self.female = QRadioButton("Female", self)
        self.female.move(200, 80)

        # Submit
        self.submitBtn = QPushButton("Submit", self)
        self.submitBtn.move(150, 110)
        self.submitBtn.clicked.connect(self.submitAct)

        self.show()

    def submitAct(self):
        # Get Values
        name = self.name.text()
        surname = self.surname.text()
        gender = "Male" if self.male.isChecked() else "Female"

        print(f"Name: {name} {surname}\nGender: {gender}")


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
