from PyQt5.QtWidgets import QApplication, QWidget
import sys

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("hello")
        self.resize(400, 300)
        self.move(600, 300)

def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()




    