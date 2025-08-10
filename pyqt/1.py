from PyQt5.QtWidgets import *
import sys

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("hello")
        self.resize(400, 300)
        self.move(600, 300)

        self.label =QLabel(self)
        self.label.setText("hello world")
        self.label.move(100, 200)

        button = QPushButton(self)
        button.setText("ok")
        button.move(170, 160)
        button.clicked.connect(self.click_success)

    def click_success(self):
        self.label.setText("i am fine")


def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()




    