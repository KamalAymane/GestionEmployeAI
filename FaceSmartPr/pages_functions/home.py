from PyQt5.QtWidgets import QWidget
from ui.general import Ui_home

class Home(QWidget):
    def __init__(self):
        super(Home, self).__init__()
        self.ui=Ui_home()
        self.ui.setupUi(self)

