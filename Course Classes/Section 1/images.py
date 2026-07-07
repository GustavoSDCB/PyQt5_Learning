import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QPushButton 
from PyQt5.QtGui import QPixmap     # Needed to display images

class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setGeometry(333, 300, 500, 400)
        self.setWindowTitle("Using Images")
        self.UI()

    def UI(self) -> None:
        self.image = QLabel(self)
        self.image.setPixmap(QPixmap(r"Course Classes\images\pokeball.png"))
        
        self.hideShowBtn = QPushButton("Hide", self)
        self.stateBtn = True
        self.hideShowBtn.move(200, 375)
        self.hideShowBtn.clicked.connect(self.hideShowBtnAction)

        self.show()

    def hideShowBtnAction(self) -> None:
        if self.stateBtn:
            self.stateBtn = False
            self.hideShowBtn.setText("Show")
            self.image.hide()
        else:
            self.stateBtn = True
            self.hideShowBtn.setText("Hide")
            self.image.show()


def main() -> None:
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
