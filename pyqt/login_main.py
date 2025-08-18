import sys
from PyQt5.QtWidgets import *

import login

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QWidget()
    form = login.Ui_Form()
    form.setupUi(window)
    
    window.show()
    app.exec_() 