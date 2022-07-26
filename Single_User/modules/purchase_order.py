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

class PurchaseOrder:
    def purchase_order_load_table(self):
        TableQt.loadtable(
            self.ui.tableWidget_27,
            [6],
            [self.details_page],
            "SELECT po_number, po_title, po_date, po_status, fulfilled, po_amount_recived FROM purchaseorder",
            ["Details"]
        )
        # self.connection = sqlite3.connect(pathtodb + "\\yobi\\yobi_database.db")
        # query = "SELECT po_number, po_title, po_date, po_status, fulfilled, po_amount_recived FROM purchaseorder"
        # result = self.connection.execute(query).fetchall()

        # self.ui.tableWidget_27.setRowCount(0)
        # for row_number, row_data in enumerate(result):
        #     self.ui.tableWidget_27.insertRow(row_number)
        #     for column_number, data in enumerate(row_data):
        #         self.ui.tableWidget_27.setItem(
        #             row_number,
        #             column_number,
        #             QTableWidgetItem(
        #                 str(data)))
        #         btn = QPushButton("Details")
        #         font = QtGui.QFont()
        #         font.setPointSize(9)
        #         font.setBold(True)
        #         # font.setWeight(75)
        #         btn.setFont(font)
        #         btn.setStyleSheet("QPushButton{\n"
        #                         "    background-color: rgb(0, 255, 0);;\n"
        #                         "border-radius : 25px;\n"
        #                         "color : rgb(7, 7, 7); \n"
        #                         "}")
        #         self.ui.tableWidget_27.setCellWidget(row_number, 6, btn)
        #         btn.clicked.connect(self.details_page)
    def purchase_order_items_load_table(self):
        self.connection = sqlite3.connect(pathtodb + "\\yobi\\yobi_database.db")
        row = self.ui.tableWidget_27.currentRow()
        currentcode = (self.ui.tableWidget_27.item(row, 0).text())
        currentcode = (''.join(map(str, currentcode)))
        
        result = self.connection.execute("SELECT name , cogs, quantity, amount FROM purchase_order_items WHERE purchase_order_uuid=?", (currentcode,)).fetchall()
    
        self.ui.tableWidget_29.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableWidget_29.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableWidget_29.setItem(
                    row_number,
                    column_number,
                    QTableWidgetItem(
                        str(data)))
                btn = QPushButton("Delete")
                font = QtGui.QFont()
                font.setPointSize(9)
                font.setBold(True)
                # font.setWeight(75)
                btn.setFont(font)
                btn.setStyleSheet("QPushButton{\n"
                                "    background-color: rgb(208, 0, 0);;\n"
                                "border-radius : 25px;\n"
                                "color : rgb(7, 7, 7); \n"
                                "}")
                self.ui.tableWidget_29.setCellWidget(row_number, 4, btn)
                # btn.clicked.connect(self.details_page)
    
