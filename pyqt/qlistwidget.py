from PyQt5.QtWidgets import *
import sys


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("qlsitwidget")
        layout = QFormLayout(self)

        listwidget = QListWidget()
        listwidget.addItem("c++")
        listwidget.addItem("c")
        listwidget.addItems(["java", "python"])
        listwidget.currentItemChanged.connect(self.selectionchange)

        layout.addRow(QLabel("choice your language"),listwidget)

  
    def selectionchange(self, item):
        print(item.text())
       


def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()