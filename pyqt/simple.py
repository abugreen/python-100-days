from PyQt5.QtWidgets import QApplication, QWidget
import sys



app = QApplication(sys.argv)
w = QWidget()
w.setWindowTitle('simple gui')
w.show()


sys.exit(app.exec_())