from PyQt5.QtWidgets import *
import sys


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("qcombobox")
        layout = QFormLayout(self)

        box = QComboBox()
        box.addItem("c++")
        box.addItem("c")
        box.addItems(["java", "python"])
        box.currentIndexChanged.connect(self.selectionchange)

        layout.addRow(QLabel("choice your language"),box)

  
    def selectionchange(self, item):
        print(item.text())
       


def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()