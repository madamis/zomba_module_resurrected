from PyQt5 import QtSql, QtCore
from PyQt5.QtWidgets import QMessageBox

class Developer:
    #initialize model
    def __init__(self,widget, db):
        self.db = db
        self.wid = widget
        self.model = QtSql.QSqlTableModel()

    #selecting data
    def select_data(self):
        self.model.setTable('field')
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        self.model.select()
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "id")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Name")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Surname")
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, "DOB")
        self.model.setHeaderData(4, QtCore.Qt.Horizontal, "Phone")
        self.dlg.tableWidget.setModel(self.model)

    #Insert Data:
    def insert_data(self):
        self.model.insertRows(self.i, 1)
        self.model.setData(self.model.index(self.i, 1), self.dlg.lineEdit.text())
        self.model.setData(self.model.index(self.i, 2), self.dlg.lineEdit_2.text())
        self.model.setData(self.model.index(self.i, 4), self.dlg.lineEdit_3.text())
        self.model.setData(self.model.index(self.i, 3), self.dlg.dateEdit.text())
        self.model.submitAll()

    #Update Data:
    def update_data(self):
        if self.dlg.tableWidget.currentIndex().row() > -1:
            record = self.model.record(self.dlg.tableWidget.currentIndex().row())
            record.setValue("Name", self.dlg.lineEdit.text())
            record.setValue("Surname", self.dlg.lineEdit_2.text())
            record.setValue("DOB", self.dlg.dateEdit.text())
            record.setValue("Phone", self.dlg.lineEdit_3.text())
            self.model.setRecord(self.dlg.tableWidget.currentIndex().row(), record)
        else:
            QMessageBox.question(self, 'Message', "Please select a row would you like to update", QMessageBox.Ok)
            self.show()

    #Delete Data:
    def delete_data(self):
        if self.dlg.tableWidget.currentIndex().row() > -1:
            self.model.removeRow(self.dlg.tableWidget.currentIndex().row())
            self.i -= 1
            self.model.select()
            self.dlg.lcdNumber.display(self.i)
        else:
            QMessageBox.question(self, 'Message', "Please select a row would you like to delete", QMessageBox.Ok)
            self.show()