import os
import sqlite3
from PySide6.QtWidgets import QPushButton, QTableWidgetItem
basepath = os.path.expanduser('~/Documents')
pathtodb = str(basepath)
newpath = (pathtodb + "\\yobi")
if not os.path.exists(newpath):
    os.makedirs(newpath)


class TableQt:
    """loads data to the hrms tables i.e employee, department and positions
    Basic Usage
     
    >>> TableQt.loadtable(
            tablename = self.ui.tableWidget_39,
            column_num = [5], 
            funccalled = [ self.department_update_page],  
            sqlquery = "SELECT dep_name, dep_code, dep_level, dep_supirior, status FROM department",
    >>>     btn_name = ["update"])
     
    """
    def loadtable(tablename : str, column_num : list, funccalled:list, sqlquery : str, btn_name : list[str]) -> None:
        connection = sqlite3.connect(pathtodb + "\\yobi\\yobi_database.db")
        query = sqlquery
        result = connection.execute(query).fetchall()

        tablename.setRowCount(0)
        for row_number, row_data in enumerate(result):
            tablename.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                tablename.setItem(
                    row_number,
                    column_number,
                    QTableWidgetItem(
                        str(data)))
                for cn_num, b_name, func_called in zip(column_num, btn_name, funccalled):
                    b_name = QPushButton(b_name)
                    b_name.setStyleSheet(u"QPushButton{\n"
                                        "\n"
                                        "border-radius : 20px;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "	background-color: rgb(85, 170, 255);\n"
                                        "}")
                    tablename.setCellWidget(row_number, cn_num, b_name)
                    b_name.clicked.connect(func_called)
    def load_search_table(tablename : str, column_num : list, funccalled:list, sqlquery : str, btn_name : list[str]) -> None:
        connection = sqlite3.connect(pathtodb + "\\yobi\\yobi_database.db")
        query = sqlquery
        result = query

        tablename.setRowCount(0)
        for row_number, row_data in enumerate(result):
            tablename.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                tablename.setItem(
                    row_number,
                    column_number,
                    QTableWidgetItem(
                        str(data)))
                for cn_num, b_name, func_called in zip(column_num, btn_name, funccalled):
                    b_name = QPushButton(b_name)
                    b_name.setStyleSheet(u"QPushButton{\n"
                                        "\n"
                                        "border-radius : 20px;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "	background-color: rgb(85, 170, 255);\n"
                                        "}")
                    tablename.setCellWidget(row_number, cn_num, b_name)
                    b_name.clicked.connect(func_called)
    def loadtable_query(tablename : str, column_num : list, funccalled:list, sqlquery : str, btn_name : list[str], query_var : str) -> None:
        connection = sqlite3.connect(pathtodb + "\\yobi\\yobi_database.db")
        query = sqlquery
        result = connection.execute(query,(query_var,)).fetchall()

        tablename.setRowCount(0)
        for row_number, row_data in enumerate(result):
            tablename.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                tablename.setItem(
                    row_number,
                    column_number,
                    QTableWidgetItem(
                        str(data)))
                for cn_num, b_name, func_called in zip(column_num, btn_name, funccalled):
                    b_name = QPushButton(b_name)
                    b_name.setStyleSheet(u"QPushButton{\n"
                                        "\n"
                                        "border-radius : 20px;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "	background-color: rgb(85, 170, 255);\n"
                                        "}")
                    tablename.setCellWidget(row_number, cn_num, b_name)
                    b_name.clicked.connect(func_called)

    def load_table_no_buttons(tablename : str, sqlquery : str, ID) -> None:
        connection = sqlite3.connect(pathtodb + "\\yobi\\yobi_database.db")
        query = sqlquery
        result = connection.execute(query, (ID,)).fetchall()

        tablename.setRowCount(0)
        for row_number, row_data in enumerate(result):
            tablename.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                tablename.setItem(
                    row_number,
                    column_number,
                    QTableWidgetItem(
                        str(data)))
