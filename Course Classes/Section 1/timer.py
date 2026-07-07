import sys
from PyQt5.QtWidgets import QLabel, QWidget, QApplication, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer

font = QFont("Comic Sans MS", 16)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle("Timer Widget (Trafic Light)")

        self.setUI()

    def setUI(self):
        # Label
        self.colorLabel = QLabel(self)
        self.colorLabel.resize(250, 250)
        self.colorLabel.setStyleSheet("background-color: gray") # Changing the background color
        self.colorLabel.move(80, 20)

        # Timer
        self.timer = QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.changeColor)
        self.actualColor = 0

        # Start Button
        self.startBtn = QPushButton("Start", self)
        self.startBtn.move(80, 270)
        self.startBtn.clicked.connect(self.startAct)

        # Stop Button
        self.stopBtn = QPushButton("Stop", self)
        self.stopBtn.move(250, 270)
        self.stopBtn.clicked.connect(self.stopAct)

        self.show()

    def startAct(self):
        self.timer.start()

    def stopAct(self):
        self.timer.stop()

    def changeColor(self):
        if self.actualColor == 0:
            self.colorLabel.setStyleSheet("background-color: green")
            self.timer.setInterval(5000)
            self.actualColor = 1
        elif self.actualColor == 1:
            self.colorLabel.setStyleSheet("background-color: orange")
            self.timer.setInterval(2000)
            self.actualColor = 2
        else:
            self.colorLabel.setStyleSheet("background-color: red")
            self.timer.setInterval(4000)
            self.actualColor = 0


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
