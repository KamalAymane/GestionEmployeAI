from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication
from ui.login import Ui_login
import sys
import mysql.connector as mc

class Log(QWidget):
    def __init__(self):
        super(Log, self).__init__()
        self.ui=Ui_login()
        self.ui.setupUi(self)

