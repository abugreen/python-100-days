from PyQt5.QtWidgets import *
import sys


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QFormlayout")

        layout = QFormLayout(self)
        layout.addRow(QLabel("user name"), QLineEdit())

        textpad = QLineEdit()
        textpad.setEchoMode(QLineEdit.Password)
        layout.addRow(QLabel("password"),textpad)

        textcom = QTextEdit()
        layout.addRow(textcom)

        # hbox = QHBoxLayout()
        # btnok = QPushButton("ok")
        # btncancel = QPushButton("cancel")
        # hbox.addWidget(btnok)
        # hbox.addWidget(btncancel)
        # layout.addRow(hbox)



def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()