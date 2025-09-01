from PyQt5.QtWidgets import *
from empty_qd import Ui_Form

import sys

        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()
    Form = Ui_Form()
    Form.setupUi(window)
    window.show()
    sys.exit(app.exec_())