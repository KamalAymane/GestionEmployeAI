from PyQt5.QtWidgets import QWidget
from ui.faceRecognition import Ui_FaceRecognition

class Face(QWidget):
    def __init__(self):
        super(Face, self).__init__()
        self.ui=Ui_FaceRecognition()
        self.ui.setupUi(self)