
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1273, 744)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.menu_widget = QtWidgets.QWidget(self.centralwidget)
        self.menu_widget.setGeometry(QtCore.QRect(0, 0, 261, 751))
        self.menu_widget.setStyleSheet("background-color:#677B5E;\n"
"color:#fff;\n"
"border:none;\n"
"")
        self.menu_widget.setObjectName("menu_widget")
        self.toolBox = QtWidgets.QToolBox(self.menu_widget)
        self.toolBox.setGeometry(QtCore.QRect(10, 10, 241, 721))
        self.toolBox.setStyleSheet("#tooBox{\n"
"color:#fff\n"
"}\n"
"#toolBox::tab{\n"
"padding-left:5px;\n"
"text-align:left;\n"
"border-radius:2px;\n"
"}\n"
"#toolBox::tab::selected{\n"
"background-color:#BC9C22;\n"
"font-weight:bold;\n"
"}\n"
"#toolBox QPushButton{\n"
"padding: 5px 0px 5px 20px;\n"
"text-align:left;\n"
"border-redius:3px;\n"
"}\n"
"#toolBox QPushButton:hover{\n"
"background-color:#A5C497;\n"
"}\n"
"#toolBox QPushButton:checked{\n"
"background-color:#A5C497;\n"
"}")
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 241, 601))
        self.page.setObjectName("page")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_6 = QtWidgets.QPushButton(self.page)
        self.pushButton_6.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_6.setCheckable(True)
        self.pushButton_6.setChecked(True)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout.addWidget(self.pushButton_6)
        spacerItem = QtWidgets.QSpacerItem(20, 548, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.page, icon, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 241, 601))
        self.page_2.setObjectName("page_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.faceButton = QtWidgets.QPushButton(self.page_2)
        self.faceButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.faceButton.setCheckable(True)
        self.faceButton.setObjectName("faceButton")
        self.verticalLayout_2.addWidget(self.faceButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 548, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/camera.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.page_2, icon1, "")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setGeometry(QtCore.QRect(0, 0, 241, 601))
        self.page_3.setObjectName("page_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.crudButton = QtWidgets.QPushButton(self.page_3)
        self.crudButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.crudButton.setCheckable(True)
        self.crudButton.setObjectName("crudButton")
        self.verticalLayout_3.addWidget(self.crudButton)
        spacerItem2 = QtWidgets.QSpacerItem(20, 548, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/details.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.page_3, icon2, "")
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setGeometry(QtCore.QRect(0, 0, 241, 601))
        self.page_4.setObjectName("page_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_8 = QtWidgets.QPushButton(self.page_4)
        self.pushButton_8.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_8.setCheckable(True)
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout_4.addWidget(self.pushButton_8)
        spacerItem3 = QtWidgets.QSpacerItem(20, 548, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/signout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.page_4, icon3, "")
        self.main_widget = QtWidgets.QWidget(self.centralwidget)
        self.main_widget.setGeometry(QtCore.QRect(260, 0, 1011, 741))
        self.main_widget.setObjectName("main_widget")
        self.tabWidget = QtWidgets.QTabWidget(self.main_widget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 100, 1021, 651))
        self.tabWidget.setStyleSheet("QTabBar::close-button{\n"
"margin-left:3px;\n"
"image:url(icons/cross.png);\n"
"}\n"
"QTabBar::close-button:hover{\n"
"image: url(icons/closehover.png);\n"
"}\n"
"")
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.reduce_widget = QtWidgets.QWidget(self.main_widget)
        self.reduce_widget.setGeometry(QtCore.QRect(0, 0, 1011, 101))
        self.reduce_widget.setStyleSheet("#reduce_widget{\n"
"background-color:#A5C497;\n"
"}")
        self.reduce_widget.setObjectName("reduce_widget")
        self.label = QtWidgets.QLabel(self.reduce_widget)
        self.label.setGeometry(QtCore.QRect(840, 10, 81, 81))
        self.label.setStyleSheet("#label{\n"
"background-color:#677B5E;\n"
"border: 1px solid #677B5E;\n"
"padding:5px 5px;\n"
"border-radius:25%;\n"
"}")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("icons/dorsia.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.reduce_widget)
        self.label_2.setGeometry(QtCore.QRect(120, 30, 801, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(24)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("#label_2{\n"
"color:#BC9C22;\n"
"\n"
"}")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_6.setText(_translate("MainWindow", "home"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("MainWindow", "General"))
        self.faceButton.setText(_translate("MainWindow", "Face Recognition"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("MainWindow", "Attendance"))
        self.crudButton.setText(_translate("MainWindow", "form"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), _translate("MainWindow", "Information"))
        self.pushButton_8.setText(_translate("MainWindow", "sign out"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), _translate("MainWindow", "sign out"))
        self.label_2.setText(_translate("MainWindow", "WELCOME TO DORSIA HR MANAGEMENT APPLICATION"))
