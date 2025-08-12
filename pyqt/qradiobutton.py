from PyQt5.QtWidgets import *
import sys


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Radiobutton")

        label1 = QLabel("choice your favorite color:")

        rb1 = QRadioButton("red")
        rb1.setChecked(True)
        rb2 = QRadioButton("blue")
        rb3 = QRadioButton("green")

        layout = QHBoxLayout()
        self.setLayout(layout)

        layout.addWidget(label1)
        layout.addWidget(rb1)
        layout.addWidget(rb2)
        layout.addWidget(rb3)
  
        rb1.toggled.connect(self.btn_clicked)
        rb2.toggled.connect(self.btn_clicked)
        rb3.toggled.connect(self.btn_clicked)


    def btn_clicked(self):
        rb = self.sender()
        if rb.isChecked():
            msg = "choice your favorite color is {} ".format(rb.text())
            print(msg)


def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()