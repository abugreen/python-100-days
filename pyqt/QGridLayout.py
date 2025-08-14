from PyQt5.QtWidgets import *

import sys

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("my window")
        self.resize(400, 300)
        self.move(600, 300)

        buttonBlue = QPushButton("Blue" , self)
        buttonBlue.clicked.connect(self.on_click)
        buttonRed = QPushButton("Red", self)
        buttonRed.clicked.connect(self.on_click)
        buttonGreen = QPushButton("Green", self)
        buttonGreen.clicked.connect(self.on_click)
        
        gridlayout = QGridLayout(self)
        gridlayout.addWidget(buttonBlue,1,1)
        gridlayout.addWidget(buttonRed,1,2)
        gridlayout.addWidget(buttonGreen,2,1)
     

    def on_click(self): 
        sender = self.sender()
        msg = "you hit {} button".format(sender.text())
        print(msg)

def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()