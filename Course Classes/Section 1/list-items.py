import sys
from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, QMessageBox, QApplication, QListWidget
from PyQt5.QtGui import QFont

font = QFont("Comic Sans MS", 10)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle("List Widget")
        self.informations = {
            0 : ("Null Value", "Please, inform a value to add."),
            1 : ("Null Value", "Please select a value to delete."),
            2 : ("Null Value", "Please, select a value to get its content")
        }

        self.setUI()



    def setUI(self):
        # Line Edit
        self.addRecord = QLineEdit(self)
        self.addRecord.setPlaceholderText("Type an item")
        self.addRecord.setFont(font)
        self.addRecord.move(100, 50)
        
        # List Widget
        self.listWidget = QListWidget(self)
        self.listWidget.move(100, 80)

        # Buttons
        self.addBtn = QPushButton("Add Item", self)
        self.addBtn.move(360, 80)
        self.addBtn.clicked.connect(self.addAct)

        self.delBtn = QPushButton("Delete Item", self)
        self.delBtn.move(360, 105)
        self.delBtn.clicked.connect(self.delAct)

        self.getBtn = QPushButton("Get Item", self)
        self.getBtn.move(360, 130)
        self.getBtn.clicked.connect(self.getAct)

        self.delAllBtn = QPushButton("Delete All", self)
        self.delAllBtn.move(360, 155)
        self.delAllBtn.clicked.connect(self.delAllAct)

        self.show()

    def addAct(self):
        value = self.addRecord.text()
        self.listWidget.addItem(value) if value != "" else self.infoBox(0)
        self.addRecord.clear()
        self.addRecord.setFocus()

    def delAct(self):
        currentValue = self.listWidget.currentRow()
        self.listWidget.takeItem(currentValue) if currentValue != -1 else self.infoBox(1)

    def getAct(self):
        value = self.listWidget.currentItem()
        print(value.text()) if value is not None else self.infoBox(2)

    def delAllAct(self):
        answer = QMessageBox.warning(
            self, "DELETE ALL",
            "Do you really want to delete all items?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No
        )

        self.listWidget.clear() if answer == QMessageBox.Yes else None

    def infoBox(self, code):
        title, message = self.informations[code]
        QMessageBox.information(self, title, message)


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
