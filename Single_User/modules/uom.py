from main import *
import os
from PySide6.QtWidgets import *
from modules.tableclass import TableQt

basepath = os.path.expanduser('~/Documents')
pathtodb = str(basepath)
newpath = (pathtodb + "\\yobi")
if not os.path.exists(newpath):
    os.makedirs(newpath)


def load_uom(self):
    TableQt.loadtable(
        tablename = self.ui.tableWidget_42,
        column_num = [3], 
        funccalled = [ self.uom_update_page],  
        sqlquery = "SELECT name, unit_abbr FROM uom",
        btn_name = ["update"])