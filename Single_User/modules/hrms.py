from main import *
import os
from PySide6.QtWidgets import *
from modules.tableclass import TableQt

basepath = os.path.expanduser('~/Documents')
pathtodb = str(basepath)
newpath = (pathtodb + "\\yobi")
if not os.path.exists(newpath):
    os.makedirs(newpath)


def load_department_hrms(self):
    TableQt.loadtable(
        tablename = self.ui.tableWidget_39,
        column_num = [5], 
        funccalled = [ self.department_update_page],  
        sqlquery = "SELECT dep_code, dep_name, dep_level, dep_supirior, status FROM department",
        btn_name = ["update"])

def load_positions_hrms(self):
    TableQt.loadtable(
        tablename = self.ui.tableWidget_38,
        column_num = [4], 
        funccalled = [self.position_update_page], 
        sqlquery = "SELECT pos_code, pos_name, pos_level, status FROM positions",
        btn_name = ["update"])

def load_employee_hrms(self):
    TableQt.loadtable(
        tablename = self.ui.tableWidget_40,
        column_num = [5,6], 
        funccalled = [self.employee_profile_page, self.employee_update_page], 
        sqlquery = "SELECT emp_code, first_name, department, emmp_postion, joined FROM employee",
        btn_name = ["Details", "update"])
