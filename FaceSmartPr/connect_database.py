import mysql.connector


class ConnectDatabase:
    def __init__(self):
        self._host = "127.0.0.1"
        self._port = 3306
        self._user = "root"
        self._password = "root"
        self._database = "facesmatdb"
        self.con = None
        self.cursor = None

    def connect_db(self):

        self.con = mysql.connector.connect(
            host=self._host,
            port=self._port,
            database=self._database,
            user=self._user,
            password=self._password
        )


        self.cursor = self.con.cursor(dictionary=True)

    def add_info(self, employee_id, first_name, last_name, departement, position, working_hours):

        self.connect_db()


        sql = f"""
            INSERT INTO employee (idemployee, firstname, lastname, departement, position, workingHours) 
	            VALUES ({employee_id}, '{first_name}', '{last_name}', '{departement}', '{position}', '{working_hours}');
        """

        try:

            self.cursor.execute(sql)
            self.con.commit()

        except Exception as E:

            self.con.rollback()
            return E

        finally:

            self.con.close()

    def update_info(self, employee_id, first_name, last_name, departement, position, working_hours):

        self.connect_db()

        sql = f"""
            UPDATE employee
                SET firstname='{first_name}', lastname='{last_name}', departement='{departement}', position='{position}', 
                    workingHours='{working_hours}'
                WHERE idemployee={employee_id};
        """

        try:

            self.cursor.execute(sql)
            self.con.commit()

        except Exception as E:

            self.con.rollback()
            return E

        finally:

            self.con.close()

    def delete_info(self, employee_id):

        self.connect_db()


        sql = f"""  
            DELETE FROM employee WHERE studentId={employee_id};
        """

        try:

            self.cursor.execute(sql)
            self.con.commit()

        except Exception as E:

            self.con.rollback()
            return E

        finally:

            self.con.close()

    def search_info(self, employee_id=None, first_name=None, last_name=None, departement=None, position=None, working_hours=None):

        self.connect_db()

        condition = ""
        if employee_id:
            condition += f"idemployee LIKE '%{employee_id}%'"
        else:
            if first_name:
                if condition:
                    condition += f" and firstname LIKE '%{first_name}%'"
                else:
                    condition += f"firstname LIKE '%{first_name}%'"

            if last_name:
                if condition:
                    condition += f" and lastname LIKE '%{last_name}%'"
                else:
                    condition += f"lastname LIKE '%{last_name}%'"

            if departement:
                if condition:
                    condition += f" and departement='{departement}'"
                else:
                    condition += f"departement='{departement}'"

            if position:
                if condition:
                    condition += f" and position='{position}'"
                else:
                    condition += f"position='{position}'"

            if working_hours:
                if condition:
                    condition += f" and workingHours LIKE '%{working_hours}%'"
                else:
                    condition += f"workingHours LIKE '%{working_hours}%'"

        if condition:

            sql = f"""
                SELECT * FROM employee WHERE {condition};
            """
        else:

            sql = f"""
                SELECT * FROM employee;
             """

        try:

            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            return result

        except Exception as E:
            return E

        finally:

            self.con.close()

    def get_all_departements(self):

        self.connect_db()


        sql = f"""  
            SELECT departement FROM employee GROUP BY departement;
        """

        try:

            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            return result

        except Exception as E:

            self.con.rollback()
            return E

        finally:

            self.con.close()

    def get_all_positions(self):

        self.connect_db()


        sql = f"""  
            SELECT position FROM employee GROUP BY position;
        """

        try:

            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            return result

        except Exception as E:

            self.con.rollback()
            return E

        finally:

            self.con.close()