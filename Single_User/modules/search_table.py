import os
import sqlite3
from PySide6.QtWidgets import QPushButton, QTableWidgetItem
from main import *
from modules.tableclass import TableQt
basepath = os.path.expanduser('~/Documents')
pathtodb = str(basepath)
newpath = (pathtodb + "\\yobi")
if not os.path.exists(newpath):
    os.makedirs(newpath)




        
def search_client(self):
    category = self.ui.lineEdit_11.text()
    database_connection = sqlite3.connect(
        pathtodb + "\\yobi\\yobi_database.db")
    if self.ui.comboBox_39.itemText(
            self.ui.comboBox_39.currentIndex()) == "client name":
        result = database_connection.execute(
            "SELECT * FROM ledgers WHERE name=?", (category,))
    elif self.ui.comboBox_39.itemText(self.ui.comboBox_39.currentIndex()) == "contacts":
        result = database_connection.execute(
            "SELECT * FROM ledgers WHERE telno=?", (category,))
    elif self.ui.comboBox_39.itemText(self.ui.comboBox_39.currentIndex()) == "email":
        result = database_connection.execute(
            "SELECT * FROM ledgers WHERE email=?", (category,))
    elif self.ui.comboBox_39.itemText(self.ui.comboBox_39.currentIndex()) == "adress":
        result = database_connection.execute(
            "SELECT * FROM ledgers WHERE address=?", (category,))
    self.ui.tableWidget_11.setRowCount(0)
    for row_number, row_data in enumerate(result):
        self.ui.tableWidget_11.insertRow(row_number)
        for column_number, data in enumerate(row_data):
            self.ui.tableWidget_11.setItem(
                row_number,
                column_number,
                QTableWidgetItem(
                    str(data)))