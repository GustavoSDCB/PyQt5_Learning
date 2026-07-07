import sys
from PyQt5.QtWidgets import QComboBox, QPushButton, QApplication, QWidget

class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setGeometry(300, 300, 400, 500)
        self.setWindowTitle("Combo Box")

        self.setUI()

    def setUI(self) -> None:
        # ComboBox
        self.combo = QComboBox(self)
        self.combo.move(170, 100)

        # Adding items to ComboBox
        self.combo.addItems([None, "Python", "Java Script", "Golang", "Ruby"])

        # Save Button
        saveBtn = QPushButton("Save", self)
        saveBtn.move(170, 130)
        saveBtn.clicked.connect(self.getValue)

        # Display Window
        self.show()

    def getValue(self):
        valueSelected = self.combo.currentText()
        print(valueSelected)

def main() -> None:
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
