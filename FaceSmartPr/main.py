from PyQt5.QtWidgets import QApplication, QMainWindow
from ui.main_window import Ui_MainWindow
from pages_functions.home import Home
from pages_functions.crud import Crud
from out_window import  Ui_OutputDialog


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.home_btn=self.ui.pushButton_6
        self.face_btn = self.ui.faceButton
        self.crud_btn = self.ui.crudButton
        self.log_btn = self.ui.pushButton_8

        self.menu_btns_dict={
            self.home_btn: Home,
            self.face_btn: Ui_OutputDialog,
            self.crud_btn: Crud,
        }

        self.show_home_window()
        self.ui.tabWidget.tabCloseRequested.connect(self.close_tab)
        self.home_btn.clicked.connect(self.show_selected_window)
        self.crud_btn.clicked.connect(self.show_selected_window)
        self.face_btn.clicked.connect(self.show_selected_window)
        self.log_btn.clicked.connect(self.show_selected_window)



    def show_home_window(self):
        result = self.open_tab_flag(self.home_btn.text())
        self.set_btn_checked(self.home_btn)

        if result[0]:
            self.ui.tabWidget.setCurrentIndex(result[1])
        else:
            tab_title = self.home_btn.text()
            new_widget_instance = Home()
            curIndex = self.ui.tabWidget.addTab(new_widget_instance,tab_title)
            self.ui.tabWidget.setCurrentIndex(curIndex)
            self.ui.tabWidget.setVisible(True)


    def set_btn_checked(self,btn):
        for button in self.menu_btns_dict.keys():
            if button != btn:
                button.setChecked(False)
            else:
                button.setChecked(True)

    def open_tab_flag(self, btn_text):
        open_tab_count = self.ui.tabWidget.count()

        for i in range(open_tab_count):
            tab_title = self.ui.tabWidget.tabText(i)
            if tab_title == btn_text:
                return True, i

        return False, None

    def show_selected_window(self):
        button = self.sender()

        if button == self.log_btn:

            self.close()


            return


        result = self.open_tab_flag(button.text())
        self.set_btn_checked(button)

        if result[0]:
            self.ui.tabWidget.setCurrentIndex(result[1])
        else:
            tab_title = button.text()
            curIndex = self.ui.tabWidget.addTab(self.menu_btns_dict[button](), tab_title)
            self.ui.tabWidget.setCurrentIndex(curIndex)
            self.ui.tabWidget.setVisible(True)

    def close_tab(self,index):
        self.ui.tabWidget.removeTab(index)

        if self.ui.tabWidget.count()==0:
            self.ui.toolBox.setCurrentIndex(0)
            self.show_home_window()

if __name__ == '__main__':
    import sys

    app= QApplication(sys.argv)

    window= MyWindow()
    window.show()
    sys.exit(app.exec())