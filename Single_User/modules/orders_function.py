from main import *
import sqlite3
from widgets import *
from PySide6.QtWidgets import *
from PySide6 import QtGui
from datetime import date
from PySide6.QtGui import QFont, QIcon
from PySide6.QtCore import QSize
from modules import st_database, pos
import os

import babel.numbers
import decimal
basepath = os.path.expanduser('~/Documents')
pathtodb = str(basepath)
newpath = (pathtodb + "\\yobi")
if not os.path.exists(newpath):
    os.makedirs(newpath)
try:
    conn = sqlite3.connect(pathtodb + "\\yobi\\yobi_database.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS recip_detail(id_17 INTEGER PRIMARY KEY, business_name TEXT, pobox TEXT, contact TEXT, email TEXT, street_address TEXT, notes TEXT, footer TEXT, currency TEXT, profile_photo BLOB)")
    cash_label = c.execute(
        "SELECT currency FROM recip_detail WHERE id_17=1").fetchone()
    cash_label = (''.join(map(str, cash_label)))
    print("*********************************", cash_label)
    c.close()
except Exception:
    cash_label = "$"


def setButtons(self):
    self.connection = sqlite3.connect(pathtodb + "\\yobi\\yobi_database.db")
    query = "SELECT code, client_name, grand_total, total_amount, payment_status,  order_date, due FROM orders ORDER BY id_13 DESC LIMIT 20"
    result = self.connection.execute(query).fetchall()

    self.ui.tableWidget_6.setRowCount(0)
    for row_number, row_data in enumerate(result):
        self.ui.tableWidget_6.insertRow(row_number)
        for column_number, data in enumerate(row_data):
            self.ui.tableWidget_6.setItem(
                row_number,
                column_number,
                QTableWidgetItem(
                    str(data)))
            btn = QPushButton("$$$")
            font = QtGui.QFont()
            font.setPointSize(9)
            font.setBold(True)
            # font.setWeight(75)
            btn.setFont(font)
            btn.setStyleSheet("QPushButton{\n"
                              "    background-color: rgb(0, 255, 0);;\n"
                              "border-radius : 25px;\n"
                              "color : rgb(7, 7, 7); \n"
                              "}")
            rtn = QPushButton("Details")
            font = QtGui.QFont()
            font.setPointSize(9)
            font.setBold(True)
            # font.setWeight(75)
            rtn.setFont(font)
            rtn.setStyleSheet(u"QPushButton{\n"
                              "\n"
                              "border-radius : 20px;\n"
                              "}\n"
                              "QPushButton:hover {\n"
                              "	background-color: rgb(85, 170, 255);\n"
                              "}")

            self.push = QPushButton()

            self.push.setStyleSheet(u"QPushButton{\n"
                                    "\n"
                                    "border-radius : 20px;\n"
                                    "}\n"
                                    "QPushButton:hover {\n"
                                    "	background-color: rgb(85, 170, 255);\n"
                                    "}")
            icon5 = QIcon()
            icon5.addFile(
                u":/icons/images/icons/cil-pen-alt.png",
                QSize(),
                QIcon.Normal,
                QIcon.Off)
            self.push.setIcon(icon5)
            self.push.setIconSize(QSize(40, 40))

            deletebtn = QPushButton()

            deletebtn.setStyleSheet(u"QPushButton{\n"
                                    "\n"
                                    "border-radius : 20px;\n"
                                    "}\n"
                                    "QPushButton:hover {\n"
                                    "	background-color: rgb(85, 170, 255);\n"
                                    "}")
            icon7 = QIcon()
            icon7.addFile(
                u":/icons/images/icons/cil-remove.png",
                QSize(),
                QIcon.Normal,
                QIcon.Off)
            deletebtn.setIcon(icon7)
            deletebtn.setIconSize(QSize(40, 40))
            btn.clicked.connect(self.btn_triger)

            self.ui.tableWidget_6.setCellWidget(row_number, 7, btn)
            self.ui.tableWidget_6.setCellWidget(row_number, 8, self.push)
            self.ui.tableWidget_6.setCellWidget(row_number, 9, deletebtn)
            self.ui.tableWidget_6.setCellWidget(row_number, 10, rtn)
            # deletebtn.clicked.connect(self.deleteorders)
            self.push.clicked.connect(self.update_orders_page)
            rtn.clicked.connect(self.set_return_orders)


def setButtons2(self):
    self.connection = sqlite3.connect(pathtodb + "\\yobi\\yobi_database.db")
    query = "SELECT code, client_name, grand_total, total_amount, payment_status,  order_date, due FROM orders ORDER BY id_13 DESC LIMIT 20"
    result = self.connection.execute(query).fetchall()

    self.ui.tableWidget_6.setRowCount(0)
    for row_number, row_data in enumerate(result):
        self.ui.tableWidget_6.insertRow(row_number)
        for column_number, data in enumerate(row_data):
            self.ui.tableWidget_6.setItem(
                row_number,
                column_number,
                QTableWidgetItem(
                    str(data)))
            btn = QPushButton("$$$")
            font = QtGui.QFont()
            font.setPointSize(9)
            font.setBold(True)
            # font.setWeight(75)
            btn.setFont(font)
            btn.setStyleSheet("QPushButton{\n"
                              "    background-color: rgb(0, 255, 0);;\n"
                              "border-radius : 25px;\n"
                              "color : rgb(7, 7, 7); \n"
                              "}")
            rtn = QPushButton("Details")
            font = QtGui.QFont()
            font.setPointSize(9)
            font.setBold(True)
            # font.setWeight(75)
            rtn.setFont(font)
            rtn.setStyleSheet(u"QPushButton{\n"
                              "\n"
                              "border-radius : 20px;\n"
                              "}\n"
                              "QPushButton:hover {\n"
                              "	background-color: rgb(85, 170, 255);\n"
                              "}")

            self.push = QPushButton()

            self.push.setStyleSheet(u"QPushButton{\n"
                                    "\n"
                                    "border-radius : 20px;\n"
                                    "}\n"
                                    "QPushButton:hover {\n"
                                    "	background-color: rgb(85, 170, 255);\n"
                                    "}")
            icon5 = QIcon()
            icon5.addFile(
                u":/icons/images/icons/cil-pen-alt.png",
                QSize(),
                QIcon.Normal,
                QIcon.Off)
            self.push.setIcon(icon5)
            self.push.setIconSize(QSize(40, 40))

            deletebtn = QPushButton()

            deletebtn.setStyleSheet(u"QPushButton{\n"
                                    "\n"
                                    "border-radius : 20px;\n"
                                    "}\n"
                                    "QPushButton:hover {\n"
                                    "	background-color: rgb(85, 170, 255);\n"
                                    "}")
            icon7 = QIcon()
            icon7.addFile(
                u":/icons/images/icons/cil-remove.png",
                QSize(),
                QIcon.Normal,
                QIcon.Off)
            deletebtn.setIcon(icon7)
            deletebtn.setIconSize(QSize(40, 40))
            btn.clicked.connect(self.btn_triger)

            self.ui.tableWidget_6.setCellWidget(row_number, 7, btn)
            self.ui.tableWidget_6.setCellWidget(row_number, 8, self.push)
            self.ui.tableWidget_6.setCellWidget(row_number, 9, deletebtn)
            self.ui.tableWidget_6.setCellWidget(row_number, 10, rtn)
            # deletebtn.clicked.connect(self.deleteorders)
            self.push.clicked.connect(self.update_orders_page)
            rtn.clicked.connect(self.set_return_orders)





def auto_completer(self):
    self.connection = sqlite3.connect(pathtodb + "\\yobi\\yobi_database.db")
    self.c = self.connection.cursor()
    self.x = self.c.execute("SELECT name FROM clients").fetchall()
    self.y = [item for t in self.x for item in t]
    self.completer = QCompleter(self.y)
    self.ui.lineEdit_14.setCompleter(self.completer)


def orders_label(self):

    try:
        self.connection = sqlite3.connect(
            pathtodb + "\\yobi\\yobi_database.db")
        self.c = self.connection.cursor()

        all_due_orders = self.c.execute(
            "SELECT SUM(due) FROM orders").fetchone()
        all_due_orders = (''.join(map(str, all_due_orders)))
        if all_due_orders == str(None):
            all_due_orders = 0.0
        else:
            all_due_orders = float(''.join(map(str, all_due_orders)))

        total_orders = self.c.execute(
            "SELECT SUM(grand_total) FROM orders").fetchone()
        total_orders = (''.join(map(str, total_orders)))
        if total_orders == str(None):
            total_orders = 0
        else:
            float(''.join(map(str, total_orders)))

        total_paid = self.c.execute("SELECT SUM(paid) FROM payment").fetchone()
        total_paid = (''.join(map(str, total_paid)))

        if total_paid == str(None):
            total_paid = 0.0
        else:
            total_paid = float(''.join(map(str, total_paid)))

        amount_paid = self.c.execute(
            "SELECT SUM(paid_amount) FROM orders").fetchone()
        amount_paid = (''.join(map(str, amount_paid)))

        if amount_paid == str(None):
            amount_paid = 0.0
        else:
            amount_paid = float(''.join(map(str, amount_paid)))

        td = (amount_paid + total_paid)

        total_revenue2 = self.c.execute(
            "SELECT SUM(KSH) FROM transactions WHERE coa_id=? AND name=?", ("revenue", "Product Sales")).fetchone()
        total_revenue2 = (''.join(map(str, total_revenue2)))

        total_revenue = self.c.execute(
            "SELECT SUM(KSH) FROM transactions WHERE coa_id=? ", ("revenue",)).fetchone()
        total_revenue = (''.join(map(str, total_revenue)))

        if total_revenue2 == str(None):
            total_revenue2 = 0.0
        else:
            total_revenue2 = float(''.join(map(str, total_revenue2)))

        tp = babel.numbers.format_currency(
            decimal.Decimal(all_due_orders), cash_label, locale='en_US')

        self.ui.label_79.setText(str(tp))
        self.ui.label_79.setFont(QFont("Times", 23))
        self.ui.label_79.setStyleSheet(
            "QLabel { color : rgb(203, 203, 203); }")

        tp_m = babel.numbers.format_currency(
            decimal.Decimal(td), cash_label, locale='en_US')
        self.ui.label_78.setText(str(tp_m))
        self.ui.label_78.setFont(QFont("Times", 23))
        self.ui.label_78.setStyleSheet(
            "QLabel { color : rgb(203, 203, 203); }")

        b = babel.numbers.format_currency(
            decimal.Decimal(total_revenue2), cash_label, locale='en_US')
        self.ui.label_77.setText(str(b))
        self.ui.label_77.setFont(QFont("Times", 23))
        self.ui.label_77.setStyleSheet(
            "QLabel { color : rgb(203, 203, 203); }")

        f = babel.numbers.format_currency(
            decimal.Decimal(all_due_orders), cash_label, locale='en_US')

        self.ui.label_27.setText(str(f))
        self.ui.label_27.setFont(QFont("Times", 20))
        self.ui.label_27.setStyleSheet(
            "QLabel { color : rgb(203, 203, 203); }")

        l = babel.numbers.format_currency(
            decimal.Decimal(total_revenue), cash_label, locale='en_US')
        self.ui.label_37.setText(str(l))
        self.ui.label_37.setFont(QFont("Times", 20))
        self.ui.label_37.setStyleSheet(
            "QLabel { color : rgb(203, 203, 203); }")

    except Exception:
        print("labels order")


def total_cogs(self) -> float:
    try:
        self.connection = sqlite3.connect(
            pathtodb + "\\yobi\\yobi_database.db")
        self.c = self.connection.cursor()
        total_cogs = self.c.execute(
            "SELECT SUM(Buying_price) FROM stock").fetchone()
        total_cogs = float(''.join(map(str, total_cogs)))
        cogs = babel.numbers.format_currency(
            decimal.Decimal(total_cogs), cash_label, locale='en_US')
        self.ui.label_181.setText(str(cogs))
        self.ui.label_181.setFont(QFont("Times", 20))
        self.ui.label_181.setStyleSheet(
            "QLabel { color : rgb(203, 203, 203); }")
    except Exception:
        print("labels order")


def total_orders(self):
    try:
        self.connection = sqlite3.connect(
            pathtodb + "\\yobi\\yobi_database.db")
        self.c = self.connection.cursor()
        res = self.c.execute("SELECT * FROM orders").fetchall()
        self.ui.label_74.setText(str(len(res)))
        self.ui.label_74.setFont(QFont("Times", 26))
        self.ui.label_74.setStyleSheet(
            "QLabel { color : rgb(203, 203, 203); }")
    except ValueError:
        print("labels order")


def total_stock(self):
    try:
        self.connection = sqlite3.connect(
            pathtodb + "\\yobi\\yobi_database.db")
        self.c = self.connection.cursor()
        res2 = self.c.execute("SELECT * FROM stock").fetchall()
        self.ui.label_178.setText(str(len(res2)))
        self.ui.label_178.setFont(QFont("Times", 26))
        self.ui.label_178.setStyleSheet(
            "QLabel { color : rgb(203, 203, 203); }")
    except Exception:
        print("labels stock")


def items_worth(self):
    try:
        self.connection = sqlite3.connect(
            pathtodb + "\\yobi\\yobi_database.db")
        self.c = self.connection.cursor()

        total_items_worth = self.c.execute(
            "SELECT SUM(selling_price) FROM stock").fetchone()
        total_items_worth = float(''.join(map(str, total_items_worth)))
        items_worth = babel.numbers.format_currency(
            decimal.Decimal(total_items_worth), cash_label, locale='en_US')
        self.ui.label_176.setText(str(items_worth))
        self.ui.label_176.setFont(QFont("Times", 20))
        self.ui.label_176.setStyleSheet(
            "QLabel { color : rgb(203, 203, 203); }")
    except Exception:
        print("labels stock")


def return_order(self):
    self.connection = sqlite3.connect(pathtodb + "\\yobi\\yobi_database.db")
    self.c = self.connection.cursor()
    row = self.ui.tableWidget_6.currentRow()
    currentcode = (self.ui.tableWidget_6.item(row, 0).text())
    currentcode = (''.join(map(str, currentcode)))
    ledger_uuid = self.c.execute("SELECT ledger_uuid FROM orders WHERE item_code=?", (currentcode,)).fetchone()
    ledger_uuid = (''.join(map(str, ledger_uuid)))

    oreder_code = str(self.ui.lineEdit_28.text())
    item_name = str(self.ui.lineEdit_29.text())
    description = str(self.ui.lineEdit_30.text())
    quantity = float(self.ui.lineEdit_31.text())
    total_amount = float(self.ui.lineEdit_32.text())
    return_date = date.today()
    uuid1 = uuid.uuid4().hex
    uuid2 = uuid.uuid4().hex
    name = ("Return of order" + oreder_code)
    paid = 0
    created = dt.today()
    updated = dt.today()
    journal_uuid = uuid.uuid4().hex


    try:
        self.c.execute(
            "UPDATE stock SET Quantity=(Quantity+?) WHERE name=?",
            (quantity,
             item_name))
        self.connection.commit()
        if total_amount > 0:
            self.c.execute("INSERT INTO journal_entries(id, ledger_id, activity, description, posted, locked, journal_entrydate) VALUES (?,?,?,?,?,?,?)",(journal_uuid, ledger_uuid, "other", description, "1", "0", return_date))
            self.connection.commit()
            self.c.execute(
                "INSERT INTO transactions(uuid, updated, created, coa_id, journal_entry_id, ledger_id, name, KSH, description, tx_type, transactionsdate) VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                (uuid1,
                created,
                updated,
                "revenue",
                journal_uuid,
                ledger_uuid,
                "Sales Returns and Allowances",
                 total_amount,
                 description,
                 "debit",
                 return_date))
            self.connection.commit()
            self.c.execute(
                "INSERT INTO transactions(uuid, updated, created, coa_id, journal_entry_id, ledger_id, name, KSH, description, tx_type, transactionsdate) VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                (uuid2,
                created,
                updated,
                "currentassets",
                journal_uuid,
                ledger_uuid,
                "inventory",
                 total_amount,
                 description,
                 "debit",
                 return_date))
            self.connection.commit()
            self.c.execute(
                "INSERT INTO transactions(uuid, updated, created, coa_id, journal_entry_id, ledger_id, name, KSH, description, tx_type, transactionsdate) VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                (uuid2,
                created,
                updated,
                "expenses",
                journal_uuid,
                ledger_uuid,
                "cost of goods sold",
                 total_amount,
                 description,
                 "credit",
                 return_date))
            self.connection.commit()
        else:
            print("on credit")
        self.c.close()
        self.connection.close()
        QMessageBox.information(
            QMessageBox(),
            'Successful',
            'return of item is a success.')
        sales_return_reload(self)
    except Exception:
        QMessageBox.warning(
            QMessageBox(),
            'Error',
            'Could not return Item CHECK if all fields are valid, If the problem persists consult us .')


def sales_return_reload(self):
    self.connection = sqlite3.connect(pathtodb + "\\yobi\\yobi_database.db")
    query = "SELECT * FROM account_payable"
    result = self.connection.execute(query).fetchall()

    self.ui.tableWidget_9.setRowCount(0)
    for row_number, row_data in enumerate(result):
        self.ui.tableWidget_9.insertRow(row_number)
        for column_number, data in enumerate(row_data):
            self.ui.tableWidget_9.setItem(
                row_number,
                column_number,
                QTableWidgetItem(
                    str(data)))


def setButtons_suppliers(self):
    self.connection = sqlite3.connect(pathtodb + "\\yobi\\yobi_database.db")
    query = "SELECT id_14, name, addr1, tel1, email FROM supplier ORDER BY id_14 DESC"
    result = self.connection.execute(query).fetchall()

    self.ui.tableWidget_14.setRowCount(0)
    for row_number, row_data in enumerate(result):
        self.ui.tableWidget_14.insertRow(row_number)
        for column_number, data in enumerate(row_data):
            self.ui.tableWidget_14.setItem(
                row_number,
                column_number,
                QTableWidgetItem(
                    str(data)))
            btn = QPushButton("Bills")
            font = QtGui.QFont()
            font.setPointSize(9)
            font.setBold(True)
            # font.setWeight(75)
            btn.setFont(font)
            btn.setStyleSheet("QPushButton{\n"
                              "    background-color: rgb(0, 255, 0);;\n"
                              "border-radius : 25px;\n"
                              "color : rgb(7, 7, 7); \n"
                              "}")
            self.push = QPushButton()

            self.push.setStyleSheet(u"QPushButton{\n"
                                    "\n"
                                    "border-radius : 20px;\n"
                                    "}\n"
                                    "QPushButton:hover {\n"
                                    "	background-color: rgb(85, 170, 255);\n"
                                    "}")
            icon9 = QIcon()
            icon9.addFile(
                u":/icons/images/icons/cil-pen-alt.png",
                QSize(),
                QIcon.Normal,
                QIcon.Off)
            self.push.setIcon(icon9)
            self.push.setIconSize(QSize(40, 40))

            edit = QPushButton()

            edit.setStyleSheet(u"QPushButton{\n"
                               "\n"
                               "border-radius : 20px;\n"
                               "}\n"
                               "QPushButton:hover {\n"
                               "	background-color: rgb(85, 170, 255);\n"
                               "}")

            deletebtn = QPushButton()

            deletebtn.setStyleSheet(u"QPushButton{\n"
                                    "\n"
                                    "border-radius : 20px;\n"
                                    "}\n"
                                    "QPushButton:hover {\n"
                                    "	background-color: rgb(85, 170, 255);\n"
                                    "}")
            icon7 = QIcon()
            icon7.addFile(
                u":/icons/images/icons/cil-remove.png",
                QSize(),
                QIcon.Normal,
                QIcon.Off)
            deletebtn.setIcon(icon7)
            deletebtn.setIconSize(QSize(40, 40))

            self.ui.tableWidget_14.setCellWidget(row_number, 7, btn)
            self.ui.tableWidget_14.setCellWidget(row_number, 8, self.push)
            self.ui.tableWidget_14.setCellWidget(row_number, 9, deletebtn)

            btn.clicked.connect(self.vendor_bills)
            self.push.clicked.connect(self.update_supplier_page)
            deletebtn.clicked.connect(self.delete_supplier)
