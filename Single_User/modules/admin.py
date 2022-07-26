from main import *
import os
from PySide6.QtWidgets import *
from modules.tableclass import TableQt

basepath = os.path.expanduser('~/Documents')
pathtodb = str(basepath)
newpath = (pathtodb + "\\yobi")
if not os.path.exists(newpath):
    os.makedirs(newpath)


def load_user_managment(self):
    TableQt.loadtable(
        tablename = self.ui.tableWidget_41,
        column_num = [5], 
        funccalled = [ self.department_update_page],  
        sqlquery = "SELECT employee_name, username, status, role, assign FROM user_managment",
        btn_name = ["update"])

