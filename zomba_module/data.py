# import psycopg2
#
# def insertion():
#     try:
#         connection = psycopg2.connect(user='postgres', password='12345678', host='localhost', port='5432',
#                                       database='zomba_malawi')
#         cursor = connection.cursor()
#         query = """INSERT INTO developer(plot_no, fname, lname) VALUES(%s, %s, %s);"""
#         record_to_insert = (12, 'ine', 'ndemwe')
#         cursor.execute(query, record_to_insert)
#
#         connection.commit()
#         count = cursor.rowcount
#         print(count, 'inserted successifully')
#
#     except(Exception, psycopg2.Error) as error:
#         if (connection):
#             print('faileed to connect', error)
#
#     finally:
#         '''closing database connection'''
#         if (connection):
#             cursor.close()
#             connection.close()
#             print("psql is closed")
#
# def updation(id, lname):
#     try:
#         connection = psycopg2.connect(user='postgres', password='12345678', host='localhost', port='5432',
#                                       database='zomba_malawi')
#         cursor = connection.cursor()
#         query = """SELECT * FROM developer WHERE id = %s;"""
#
#         cursor.execute(query, (id, ))
#         record = cursor.fetchone()
#         print(record)
#
#
#         #update single record
#         update_query = """UPDATE developer SET lname = %s WHERE id = %s;"""
#         cursor.execute(update_query, (lname, id, ))
#         connection.commit()
#         count = cursor.rowcount
#         print(count, 'record updated successifully')
#
#         print("table after update")
#         another_select_query = """SELECT * FROM developer WHERE id = %s"""
#         cursor.execute(another_select_query,(id, ))
#         record = cursor.fetchone()
#         print(record)
#
#     except(Exception, psycopg2.Error) as error:
#         if (connection):
#             print('Error in update opperation', error)
#
#     finally:
#         '''closing database connection'''
#         if (connection):
#             cursor.close()
#             connection.close()
#             print("psql is closed")
# # id = 1
# # lname = 'misomali'
# # updation(id,lname)
#
# def deleteMethod(id):
#     try:
#         connection = psycopg2.connect(user='postgres', password='12345678', host='localhost', port='5432',
#                                       database='zomba_malawi')
#         cursor = connection.cursor()
#         delete_query = """DELETE FROM developer WHERE id = %s;"""
#
#         cursor.execute(delete_query, (id, ))
#
#         connection.commit()
#         count = cursor.rowcount
#         print(count, 'record deleted successifully')
#
#     except(Exception, psycopg2.Error) as error:
#         if (connection):
#             print('Error in delete opperation', error)
#
#     finally:
#         '''closing database connection'''
#         if (connection):
#             cursor.close()
#             connection.close()
#             print("psql is closed")
# # id = 4
# # deleteMethod(8)
from PyQt5.QtSql import *
from PyQt5.QtWidgets import *
from  PyQt5.uic import *
import sys

app = QApplication(sys.argv)

class ProbTable(QWidget):
    def __init__(self, parent = None):
        super(ProbTable, self).__init__(parent)
        db = QSqlDatabase('QPSQL')
        if db.isValid():
            db.setHostName('localhost')
            db.setDatabaseName('zomba_malawi')
            db.setUserName('postgres')
            db.setPassword('12345678')
            db.setPort(5432)
            print('connected')
        else:
            QMessageBox.critical(None,"Database Error", db.lastError().text())
        self.db = db
        self.model = QSqlTableModel(self, self.db)
        self.model.setTable("abela1")
        self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.model.select()
        self.view = QTableView(self)

        self.view.setModel(self.model)

if __name__ == '__main__':
    view = ProbTable()
    view.setSizePolicy(300,300)
    view.show()
    sys.exit(app.exec_())