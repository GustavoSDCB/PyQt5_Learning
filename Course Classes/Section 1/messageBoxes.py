import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMessageBox
from PyQt5.QtGui import QFont

font = QFont("Times", 10, 100)     # Setting up a new Font Style

class Window(QWidget):
    def __init__(self):
        super().__init__()
        # Setting up Window
        self.setGeometry(300, 300, 400, 500)
        self.setWindowTitle("Message Box")
        self.setUI()

    def setUI(self):
        # Warning Button
        warningBtn = QPushButton("Warning", self)
        warningBtn.setFont(font)    # Changing the Font Style
        warningBtn.move(70, 150)
        warningBtn.clicked.connect(self.warningAct)

        # Info Button
        infoBtn = QPushButton("Information", self)
        infoBtn.setFont(font)
        infoBtn.move(150, 150)
        infoBtn.clicked.connect(self.infoAct)

        self.show()

    def warningAct(self):
        # Warning Message Box
        mBox = QMessageBox.question(
            self, 
            "Warning", "Exit?", 
            QMessageBox.Yes | QMessageBox.No, # You can add a third option addin pipe and Cancel i.g
            QMessageBox.No
            )
        
        sys.exit() if mBox == QMessageBox.Yes else None
    
    def infoAct(self):
        # Information Message Box
        mBox = QMessageBox.information(
            self,
            "Information",
            "This is an Information Message Box",
            QMessageBox.Ok
        )

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
