import logging
import os
from modules.contextmanager.contex_manager import SQLite_CONTEX_MANAGER
basepath = os.path.expanduser('~/Documents')
pathtodb = str(basepath)
newpath = (pathtodb + "\\stats")
if not os.path.exists(newpath):
    os.makedirs(newpath)


class UPDATE_PAGE_SetWidgetsData:
    """calls a method update_page_set_data_widgets that sets
        data from database to the QLineEdits and QPlaintextedits

        Basic Usage
>>>        UPDATE_PAGE_SetWidgetsData.update_page_set_data_widgets(
                    stacked_Widget = self.ui.stackedWidget_4,
                    page = self.ui.page_48,
                    table_Widget = self.ui.tableWidget_40,
                    row_num = 0,
                    line_edits = [
                            self.ui.lineEdit_68,
                            self.ui.lineEdit_70],
                    sqlquery="SELECT %s FROM employee WHERE emp_code=? ",
                    column_list=["emp_code",
                                "first_name", 
                                "last_name", 
                                "mobile", 
                                "email", 
                                "address", 
                                "gender"],
                    plaintexteditsql=None,
            >>>     plaintextedit=None) 
    """
    def update_page_set_data_widgets(stacked_Widget, page, table_Widget, row_num:int, line_edits:list, sqlquery:str, column_list:list, plaintexteditsql:str=None, plaintextedit:str=None) -> None:
        logging.basicConfig(level=logging.INFO)
        with SQLite_CONTEX_MANAGER(file_name=pathtodb + "\\stats\\yobi_database.db") as cusr:
            stacked_Widget.setCurrentWidget(page)
            row = table_Widget.currentRow()
            currentcode = (table_Widget.item(row, row_num).text())
            currentcode = (''.join(map(str, currentcode)))
            for col, edits in zip(column_list, line_edits):
                var_y = cusr.execute(
                    sqlquery %
                    (str(
                        col,)), (currentcode,)).fetchone()
                var_y = (''.join(map(str, var_y)))
                edits.setText((var_y))
            if plaintextedit != None:
                notes = cusr.execute(plaintexteditsql, (currentcode,)).fetchone()
                notes = (''.join(map(str, notes)))
                plaintextedit.insertPlainText(notes)
