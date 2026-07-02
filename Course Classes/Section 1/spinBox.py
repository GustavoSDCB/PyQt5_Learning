import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

font = QFont("Comic", 15)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle("Spin Box")

        self.setUI()

    def setUI(self):
        # SpinBox
        self.spinBox = QSpinBox(self)
        # Setting range
        self.spinBox.setRange(1, 150)
        # Setting Prefix/Sufix
        self.spinBox.setPrefix("R$ ")
        self.spinBox.setSuffix(",00")
        # Setting the value of the step (when you click the arrow, how many values it'll increase/decrease each click)
        self.spinBox.setSingleStep(2)
        # There's also a function for this object that you can call that has offers the same result as the one in QPushButton (clicked.connect), here it is valueChanged.connect()
        self.spinBox.move(100, 70)
        self.spinBox.setFont(font)

        # Submit
        self.spinBtn = QPushButton("Submit Value", self)
        self.spinBtn.setFont(QFont("Times", 10))
        self.spinBtn.move(100, 100)
        self.spinBtn.clicked.connect(self.getSpinValue)

        self.show()

    def getSpinValue(self):
        spinValue = self.spinBox.value()
        print(f"You choose R${spinValue:.2f}")

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()