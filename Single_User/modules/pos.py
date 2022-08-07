import os
import sqlite3
from PySide6 import QtGui
from PySide6.QtWidgets import QPushButton, QTableWidgetItem
from modules.tableclass import TableQt
basepath = os.path.expanduser('~/Documents')
pathtodb = str(basepath)
newpath = (pathtodb + "\\yobi")
if not os.path.exists(newpath):
    os.makedirs(newpath)

def pos(self):
    print(f"dict{self.point_OS}")
    database_connection = sqlite3.connect(
        pathtodb + "\\yobi\\yobi_database.db")
    cusr = database_connection.cursor()
    for key, value in self.point_OS.items():
        print(f"value ->{value}")
        print(f"key ->{key}")
        key2 = str(key)
        value2 = int(value)
        cusr.execute("UPDATE stock SET Quantity=? WHERE UPC=? ", (value2, key2))
        database_connection.commit()