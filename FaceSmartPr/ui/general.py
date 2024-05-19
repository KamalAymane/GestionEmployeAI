
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_home(object):
    def setupUi(self, home):
        home.setObjectName("home")
        home.resize(1009, 638)
        home.setStyleSheet("#Qwidget{\n"
"background-color:url(icons/By chef douaa and chef aymane.png);}")
        self.widget = QtWidgets.QWidget(home)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1011, 641))
        self.widget.setStyleSheet("#widget{\n"
"border-image:url(icons/By chef douaa and chef aymane.png);}")
        self.widget.setObjectName("widget")

        self.retranslateUi(home)
        QtCore.QMetaObject.connectSlotsByName(home)

    def retranslateUi(self, home):
        _translate = QtCore.QCoreApplication.translate
        home.setWindowTitle(_translate("home", "Form"))

