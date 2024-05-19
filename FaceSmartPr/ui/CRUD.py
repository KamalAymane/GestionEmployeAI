
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1008, 640)
        Form.setStyleSheet("")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1011, 271))
        self.widget.setStyleSheet("#widget{\n"
"background-color:#677B5E;\n"
"}")
        self.widget.setObjectName("widget")
        self.idINP = QtWidgets.QLineEdit(self.widget)
        self.idINP.setGeometry(QtCore.QRect(170, 40, 271, 41))
        self.idINP.setStyleSheet("#idINP{\n"
"border-radius:15%;\n"
"}")
        self.idINP.setObjectName("idINP")
        self.firstnameINP = QtWidgets.QLineEdit(self.widget)
        self.firstnameINP.setGeometry(QtCore.QRect(170, 120, 271, 41))
        self.firstnameINP.setStyleSheet("#firstnameINP{\n"
"border-radius:15%;\n"
"}")
        self.firstnameINP.setObjectName("firstnameINP")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(20, 200, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("#label_3{\n"
"color:#fff;\n"
"}")
        self.label_3.setObjectName("label_3")
        self.lastnameINP = QtWidgets.QLineEdit(self.widget)
        self.lastnameINP.setGeometry(QtCore.QRect(170, 200, 271, 41))
        self.lastnameINP.setStyleSheet("#lastnameINP{\n"
"border-radius:15%;\n"
"}")
        self.lastnameINP.setObjectName("lastnameINP")
        self.hoursINP = QtWidgets.QLineEdit(self.widget)
        self.hoursINP.setGeometry(QtCore.QRect(720, 190, 271, 41))
        self.hoursINP.setStyleSheet("#hoursINP{\n"
"border-radius:15%;\n"
"}")
        self.hoursINP.setObjectName("hoursINP")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(20, 120, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("#label_4{\n"
"color:#fff;\n"
"}")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(20, 50, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("#label_5{\n"
"color:#fff;\n"
"}")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(560, 200, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("#label_6{\n"
"color:#fff;\n"
"}")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(560, 120, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("#label_7{\n"
"color:#fff;\n"
"}")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setGeometry(QtCore.QRect(560, 50, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("#label_8{\n"
"color:#fff;\n"
"}")
        self.label_8.setObjectName("label_8")
        self.departementINP = QtWidgets.QComboBox(self.widget)
        self.departementINP.setGeometry(QtCore.QRect(710, 50, 281, 41))
        self.departementINP.setObjectName("departementINP")
        self.PositionINP = QtWidgets.QComboBox(self.widget)
        self.PositionINP.setGeometry(QtCore.QRect(710, 120, 281, 41))
        self.PositionINP.setObjectName("PositionINP")
        self.ButtonsWidget = QtWidgets.QWidget(Form)
        self.ButtonsWidget.setGeometry(QtCore.QRect(0, 260, 1011, 61))
        self.ButtonsWidget.setStyleSheet("#ButtonsWidget{\n"
"background-color:#677B5E;\n"
"}")
        self.ButtonsWidget.setObjectName("ButtonsWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.ButtonsWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.AddButton = QtWidgets.QPushButton(self.ButtonsWidget)
        self.AddButton.setStyleSheet("#AddButton{\n"
"background-color:#BC9C22;\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AddButton.setIcon(icon)
        self.AddButton.setObjectName("AddButton")
        self.horizontalLayout.addWidget(self.AddButton)
        self.UpdateButton = QtWidgets.QPushButton(self.ButtonsWidget)
        self.UpdateButton.setStyleSheet("#UpdateButton{\n"
"background-color:#BC9C22;\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/update.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.UpdateButton.setIcon(icon1)
        self.UpdateButton.setObjectName("UpdateButton")
        self.horizontalLayout.addWidget(self.UpdateButton)
        self.SelectButton = QtWidgets.QPushButton(self.ButtonsWidget)
        self.SelectButton.setStyleSheet("#SelectButton{\n"
"background-color:#BC9C22;\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/select.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SelectButton.setIcon(icon2)
        self.SelectButton.setObjectName("SelectButton")
        self.horizontalLayout.addWidget(self.SelectButton)
        self.SearchButton = QtWidgets.QPushButton(self.ButtonsWidget)
        self.SearchButton.setStyleSheet("#SearchButton{\n"
"background-color:#BC9C22;\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SearchButton.setIcon(icon3)
        self.SearchButton.setObjectName("SearchButton")
        self.horizontalLayout.addWidget(self.SearchButton)
        self.ClearButton = QtWidgets.QPushButton(self.ButtonsWidget)
        self.ClearButton.setStyleSheet("#ClearButton{\n"
"background-color:#BC9C22;\n"
"}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/clear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ClearButton.setIcon(icon4)
        self.ClearButton.setObjectName("ClearButton")
        self.horizontalLayout.addWidget(self.ClearButton)
        self.DeleteButton = QtWidgets.QPushButton(self.ButtonsWidget)
        self.DeleteButton.setStyleSheet("#DeleteButton{\n"
"background-color:#BC9C22;\n"
"}")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.DeleteButton.setIcon(icon5)
        self.DeleteButton.setObjectName("DeleteButton")
        self.horizontalLayout.addWidget(self.DeleteButton)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(0, 320, 1011, 321))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "LastName:"))
        self.label_4.setText(_translate("Form", "FirstName:"))
        self.label_5.setText(_translate("Form", "Employee ID:"))
        self.label_6.setText(_translate("Form", "Working Hours:"))
        self.label_7.setText(_translate("Form", "Position:"))
        self.label_8.setText(_translate("Form", "Departement:"))
        self.AddButton.setText(_translate("Form", "ADD"))
        self.UpdateButton.setText(_translate("Form", "UPDATE"))
        self.SelectButton.setText(_translate("Form", "SELECT"))
        self.SearchButton.setText(_translate("Form", "SEARCH"))
        self.ClearButton.setText(_translate("Form", "CLEAR"))
        self.DeleteButton.setText(_translate("Form", "DELETE"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "firstname"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "lastname"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "departement"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "position"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Working Hours"))

