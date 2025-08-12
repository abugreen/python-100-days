from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
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
        self.label.move(100, 100)
        self.label.resize(200, 300)

        button_red = QPushButton(self)
        button_red.setText("red")
        button_red.clicked.connect(self.click_sender)

        button_green = QPushButton(self)
        button_green.setText("green")
        button_green.clicked.connect(self.click_sender)

        button_blue = QPushButton(self)
        button_blue.setText("blue")
        button_blue.clicked.connect(self.click_sender)

        layout = QHBoxLayout()
        self.setLayout(layout)
        layout.addWidget(button_red)
        layout.addWidget(button_green)
        layout.addWidget(button_blue)

    def click_sender(self):
        sender = self.sender()
        msg = "this is {} button".format(sender.text())
        print(msg)
        
    def click_success(self):
        self.label.setText("i am fine")
        
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.label.setText("mouse left button clicked")
        elif event.button() == Qt.RightButton:
            self.label.setText("mouse right button clicked")

    def mouseReleaseEvent(self, event):
        self.label.setText("mouse released")
    
    def mouseMoveEvent(self, event):
        self.label.setText(f"mouse moved to ({event.x()}, {event.y()})")
    
    def keyPressEvent(self, event):
        self.label.setText(f"key pressed: {event.text()}")
    
    def keyReleaseEvent(self, event):
        self.label.setText(f"key released: {event.text()}")   

def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()