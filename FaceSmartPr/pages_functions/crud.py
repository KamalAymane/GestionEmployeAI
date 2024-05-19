from PyQt5.QtWidgets import QWidget
from ui.CRUD import Ui_Form
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QFrame, QMessageBox, QTableWidgetItem
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIntValidator
from connect_database import ConnectDatabase
from PyQt5 import QtCore, QtGui, QtWidgets

class Crud(QWidget):
    def __init__(self):
        super(Crud, self).__init__()
        self.ui=Ui_Form()
        self.ui.setupUi(self)


        self.db = ConnectDatabase()

        # Connect UI elements to class variables
        self.employee_id = self.ui.idINP
        self.employee_id.setValidator(QIntValidator())  # Restrict input to integers

        self.first_name = self.ui.firstnameINP
        self.last_name = self.ui.lastnameINP
        self.departement = self.ui.departementINP
        self.position = self.ui.PositionINP
        self.working_hours = self.ui.hoursINP

        self.add_btn = self.ui.AddButton
        self.update_btn = self.ui.UpdateButton
        self.select_btn = self.ui.SelectButton
        self.search_btn = self.ui.SearchButton
        self.clear_btn = self.ui.ClearButton
        self.delete_btn = self.ui.DeleteButton

        self.result_table = self.ui.tableWidget
        self.result_table.setSortingEnabled(False)
        self.buttons_list = self.ui.widget.findChildren(QPushButton)

        # Initialize signal-slot connections
        self.init_signal_slot()

        # Populate the initial data in the table and state/city dropdowns
        self.search_info()
        self.update_departement_position()

    def init_signal_slot(self):
        # Connect buttons to their respective functions
        self.add_btn.clicked.connect(self.add_info)
        self.search_btn.clicked.connect(self.search_info)
        self.clear_btn.clicked.connect(self.clear_form_info)
        self.select_btn.clicked.connect(self.select_info)
        self.update_btn.clicked.connect(self.update_info)
        self.delete_btn.clicked.connect(self.delete_info)

    def disable_buttons(self):
        # Disable all buttons
        for button in self.buttons_list:
            button.setDisabled(True)

    def enable_buttons(self):
        # Enable all buttons
        for button in self.buttons_list:
            button.setDisabled(False)

    def add_info(self):
        # Function to add student information
        self.disable_buttons()

        employee_info = self.get_employee_info()

        if employee_info["employee_id"] and employee_info["first_name"]:
            check_result = self.check_employee_id(employee_id=int(employee_info["employee_id"]))

            if check_result:
                QMessageBox.information(self, "Warning", "Please input a new employee ID",
                                        QMessageBox.StandardButton.Ok)
                self.enable_buttons()
                return

            add_result = self.db.add_info(employee_id=int(employee_info["employee_id"]),
                                          first_name=employee_info["first_name"],
                                          last_name=employee_info["last_name"],
                                          departement=employee_info["departement"],
                                          position=employee_info["position"],
                                          working_hours=employee_info["working_hours"])

            if add_result:
                QMessageBox.information(self, "Warning", f"Add fail: {add_result}, Please try again.",
                                        QMessageBox.StandardButton.Ok)

        else:
            QMessageBox.information(self, "Warning", "Please input employee ID and first name.",
                                    QMessageBox.StandardButton.Ok)

        self.search_info()
        self.enable_buttons()

    def update_info(self):
        # Function to update student information
        new_employee_info = self.get_employee_info()

        if new_employee_info["employee_id"]:
            update_result = self.db.update_info(
                employee_id=new_employee_info["employee_id"],
                first_name=new_employee_info["first_name"],
                last_name=new_employee_info["last_name"],
                departement=new_employee_info["departement"],
                position=new_employee_info["position"],
                working_hours=new_employee_info["working_hours"]
            )

            if update_result:
                QMessageBox.information(self, "Warning",
                                        f"Fail to update the information: {update_result}. Please try again.",
                                        QMessageBox.StandardButton.Ok)
            else:
                self.search_info()
        else:
            QMessageBox.information(self, "Warning",
                                    f"Please select one employee to update.",
                                    QMessageBox.StandardButton.Ok)

    def select_info(self):
        # Function to select and populate student information in the form
        select_row = self.result_table.currentRow()
        if select_row != -1:
            self.employee_id.setEnabled(False)
            employee_id = self.result_table.item(select_row, 0).text().strip()
            fist_name = self.result_table.item(select_row, 1).text().strip()
            last_name = self.result_table.item(select_row, 2).text().strip()
            departement = self.result_table.item(select_row, 4).text().strip()
            position = self.result_table.item(select_row, 3).text().strip()
            working_hours = self.result_table.item(select_row, 5).text().strip()

            self.employee_id.setText(employee_id)
            self.first_name.setText(fist_name)
            self.last_name.setText(last_name)
            self.departement.setCurrentText(departement)
            self.position.setCurrentText(position)
            self.working_hours.setText(working_hours)
        else:
            QMessageBox.information(self, "Warning", "Please select one employee information",
                                    QMessageBox.StandardButton.Ok)

    def search_info(self):
        # Function to search for student information and populate the table
        self.update_departement_position()
        employee_info = self.get_employee_info()

        search_result = self.db.search_info(
            employee_id=employee_info["employee_id"],
            first_name=employee_info["first_name"],
            last_name=employee_info["last_name"],
            departement=employee_info["departement"],
            position=employee_info["position"],
            working_hours=employee_info["working_hours"]
        )

        self.show_data(search_result)

    def clear_form_info(self):
        # Function to clear the form
        self.update_departement_position()
        self.employee_id.clear()
        self.employee_id.setEnabled(True)
        self.first_name.clear()
        self.last_name.clear()
        self.working_hours.clear()
        self.departement.setCurrentText("")
        self.position.setCurrentText("")

    def delete_info(self):
        # Function to delete student information
        select_row = self.result_table.currentRow()
        if select_row != -1:
            selected_option = QMessageBox.warning(self, "Warning", "Are you Sure to delete it?",
                                                  QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)

            if selected_option == QMessageBox.StandardButton.Yes:
                employee_id = self.result_table.item(select_row, 0).text().strip()

                delete_result = self.db.delete_info(employee_id)

                if not delete_result:
                    self.search_info()
                else:
                    QMessageBox.information(self, "Warning",
                                            f"Fail to delete the information: {delete_result}. Please try again.",
                                            QMessageBox.StandardButton.Ok)

        else:
            QMessageBox.information(self, "Warning", "Please select one employee information to delete",
                                    QMessageBox.StandardButton.Ok)

    def show_data(self, result):
        # Function to populate the table with student information
        if result:
            self.result_table.setRowCount(0)
            self.result_table.setRowCount(len(result))

            for row, info in enumerate(result):
                info_list = [
                    info["idemployee"],
                    info["firstname"],
                    info["lastname"],
                    info["departement"],
                    info["position"],
                    info["workingHours"],
                ]

                for column, item in enumerate(info_list):
                    cell_item = QTableWidgetItem(str(item))
                    self.result_table.setItem(row, column, cell_item)

        else:
            self.result_table.setRowCount(0)
            return

    def get_employee_info(self):
        # Function to retrieve employee information from the form
        employee_id = self.employee_id.text().strip()
        first_name = self.first_name.text().strip()
        last_name = self.last_name.text().strip()
        working_hours = self.working_hours.text().strip()
        departement = self.departement.currentText().strip()
        position = self.position.currentText().strip()

        employee_info = {
            "employee_id": employee_id,
            "first_name": first_name,
            "last_name": last_name,
            "working_hours": working_hours,
            "departement": departement,
            "position": position,
        }

        return employee_info

    def check_employee_id(self, employee_id):
        # Function to check if a employee ID already exists
        result = self.db.search_info(employee_id=employee_id)
        return result

    def update_departement_position(self):
        # Function to populate the state and city dropdowns
        departement_result = self.db.get_all_departements()
        position_result = self.db.get_all_positions()

        self.departement.clear()
        self.position.clear()

        departement_list = [""]
        for item in departement_result:
            for k, v in item.items():
                if v != "":
                    departement_list.append(v)

        position_list = [""]
        for item in position_result:
            for k, v in item.items():
                if v != "":
                    position_list.append(v)

        if len(departement_list) > 1:
            self.departement.addItems(departement_list)

        if len(position_list) > 1:
            self.position.addItems(position_list)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = Crud()
    ui.show()
    sys.exit(app.exec_())