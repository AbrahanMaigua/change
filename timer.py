import sys
import os
import functools
from PyQt5.QtWidgets import QApplication, QMainWindow,  QLabel, QLineEdit, QAbstractButton
from PyQt5 import uic
class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.aux = ''
        print(os.getcwd())
        self.ui = uic.loadUi("interfa/viy.ui", self)
        self.setFixedSize(480,800)
        self.initUI()


    def initUI(self):
        # Encuentra los QLabel que quieres manipular
        btn = self.ui.findChildren(QAbstractButton)
       
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MiVentana()
    ventana.show()
    sys.exit(app.exec_())
