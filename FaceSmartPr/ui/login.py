from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector as mc
from main import MyWindow  # Ensure 'main.py' contains the 'MyWindow' class

class Ui_login(object):
    def setupUi(self, login):
        login.setObjectName("login")
        login.resize(669, 628)
        self.widget = QtWidgets.QWidget(login)
        self.widget.setGeometry(QtCore.QRect(-10, -10, 681, 711))
        self.widget.setStyleSheet("#widget{\n"
                                  "border-image:url(C:/Users/Douaa/Desktop/projetFinal/icons/background.jpg);\n"
                                  "}")
        self.widget.setObjectName("widget")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(90, 110, 491, 391))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.widget_2.setFont(font)
        self.widget_2.setStyleSheet("#widget_2{\n"
                                    "background-color:#92A48A;\n"
                                    "    alternate-background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));\n"
                                    "border-radius:15%;\n"
                                    "\n"
                                    "}")
        self.widget_2.setObjectName("widget_2")
        self.passwordINP = QtWidgets.QLineEdit(self.widget_2)
        self.passwordINP.setGeometry(QtCore.QRect(60, 200, 371, 51))
        self.passwordINP.setStyleSheet("#passwordINP{\n"
                                       "border-radius:15%;\n"
                                       "}")
        self.passwordINP.setObjectName("passwordINP")
        self.passwordINP.setEchoMode(QtWidgets.QLineEdit.Password)  # Hide password input
        self.loginButton = QtWidgets.QPushButton(self.widget_2)
        self.loginButton.setGeometry(QtCore.QRect(110, 280, 251, 51))
        self.loginButton.setStyleSheet("#loginButton{\n"
                                       "background-color:#BC9C22;\n"
                                       "border-radius:15%;\n"
                                       "}")
        self.loginButton.setObjectName("loginButton")
        self.loginButton.clicked.connect(self.login)
        self.usernameINP = QtWidgets.QLineEdit(self.widget_2)
        self.usernameINP.setGeometry(QtCore.QRect(60, 110, 371, 51))
        self.usernameINP.setStyleSheet("#usernameINP{\n"
                                       "\n"
                                       "border-radius:15%;\n"
                                       "}")
        self.usernameINP.setObjectName("usernameINP")
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setGeometry(QtCore.QRect(30, 110, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("C:/Users/Douaa/Desktop/projetFinal/icons/username.png"))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        self.label_4.setGeometry(QtCore.QRect(210, 30, 801, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(24)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("#label_2{\n"
                                   "color:#BC9C22;\n"
                                   "}")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setGeometry(QtCore.QRect(30, 200, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("C:/Users/Douaa/Desktop/projetFinal/icons/pass.png"))
        self.label_5.setObjectName("label_5")
        self.resultLabel = QtWidgets.QLabel(self.widget_2)
        self.resultLabel.setGeometry(QtCore.QRect(40, 350, 391, 20))
        self.resultLabel.setStyleSheet("#resultLabel{\n"
                                       "color:#fff;\n"
                                       "}")
        self.resultLabel.setText("")
        self.resultLabel.setObjectName("resultLabel")

        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)

    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "Form"))
        self.loginButton.setText(_translate("login", "LOGIN"))
        self.label_4.setText(_translate("login", "LOGIN"))

    def login(self):
        try:
            username = self.usernameINP.text()
            password = self.passwordINP.text()

            mydb = mc.connect(
                host='localhost',
                user='root',
                password='root',
                port='3306',
                database='facesmatdb'
            )

            mycursor = mydb.cursor()
            query = "SELECT username, password FROM login WHERE username = %s AND password = %s"
            mycursor.execute(query, (username, password))
            result = mycursor.fetchone()

            if result is None:
                self.resultLabel.setText("Incorrect email or password")
            else:
                self.resultLabel.setText("You are logged in")

                self.openMainWindow()

        except mc.Error as e:
            self.resultLabel.setText(f"Error: {e}")

    def openMainWindow(self):
        self.main_window = MyWindow()
        self.main_window.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login = QtWidgets.QWidget()
    ui = Ui_login()
    ui.setupUi(login)
    login.show()
    sys.exit(app.exec_())
