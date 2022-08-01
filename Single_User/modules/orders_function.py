from main import *
import sqlite3
from widgets import *
from PySide6.QtWidgets import *
from PySide6 import QtGui
from datetime import date
from PySide6.QtGui import QFont, QIcon
from PySide6.QtCore import QSize
from modules import st_database
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


def add_invoice(self):
    self.connection = sqlite3.connect(pathtodb + "\\yobi\\yobi_database.db")
    self.c = self.connection.cursor()
    self.posksh = self.c.execute("SELECT SUM(KSH) FROM pos_table").fetchone()
    self.posksh = float(''.join(map(str, self.posksh)))
    self.totalksh = float(str(self.ui.lineEdit_8.text()))
    
    discount = self.c.execute("SELECT SUM(discount) FROM pos_table").fetchone()
    discount = float(''.join(map(str, discount)))

    client_name = str(self.ui.lineEdit_14.text())
    self.total = self.c.execute("SELECT SUM(totalvat) FROM pos_table").fetchone()
    self.total = float(''.join(map(str, self.total)))
    print(f"........./...POS............../")
    print(f"TOTAL DISCOUNT ---> {discount}")
    

    # sub_total = self.totalksh
    total_amount = (self.total + self.posksh)

    discount2 = (discount / 100 * total_amount)
    grand_total = (total_amount - discount2)
    print(f"DISCOUNT ON product ---> {discount2}")
    print(f"Grand TOTAL AFTER DEDUCTION OF DISCOUNT ---> {grand_total}")
    total_no_tax = (self.posksh - discount2)
    amount_paid = float(str(self.ui.lineEdit_8.text()))
    due = (grand_total - amount_paid)
    print(f"DUE AMOUNT ---> {due}")
    due2 = (total_no_tax - amount_paid)
    if due < 0:
        QMessageBox.warning(
            QMessageBox(),
            'Error',
            'Due error, Due amount cant be less than 0')
    else:
        item_code = str(self.ui.lineEdit_33.text())
        payment_type = str(self.ui.comboBox_4.currentText())
        payment_status = str(self.ui.comboBox_5.currentText())

        code = str(self.ui.lineEdit_16.text())
        order_date = date.today()
        credit = "credit"
        debit = "debit"
        description = ("sold goods on credit to" + " " + client_name)
        description2 = ("sold goods on credit to" + " " + client_name)
        name = ("Debitor" + "," + " " + client_name + item_code)
        terms = str(self.ui.comboBox_20.currentText())
        invoice_status = str(self.ui.comboBox_21.currentText())
        ledger_uuid = uuid.uuid4().hex
        invoice_uuid = uuid.uuid4().hex
        combo1,combo2 = '0', '0'
        invoice_number = ('INVOICE-' + (''.join(random.choices(string.ascii_uppercase, k=12))))
        date_1 = date.today()
        created = dt.today()
        updated = dt.today()
        journal_uuid = uuid.uuid4().hex
        uuid1 = uuid.uuid4().hex
        uuid2 = uuid.uuid4().hex
        uuid3 = uuid.uuid4().hex
        markdown_notes = self.ui.plainTextEdit_5.document().toPlainText()

        try:
            self.c.execute(
                "INSERT INTO orders(uuid, created, sale_no, updated, terms, item_code, discount,  paid_amount, code, client_name, grand_total, total_amount, sub_total, payment_type, payment_status,  order_date, due, invoice_status, markdown_notes, ledger_uuid) "
                "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (
                    invoice_uuid,
                    created,
                    item_code,
                    updated,
                    terms,
                    invoice_number,
                    discount,
                    amount_paid,
                    invoice_number,
                    client_name,
                    grand_total,
                    total_amount,
                    self.posksh,
                    payment_type,
                    payment_status,
                    order_date,
                    due,
                    invoice_status,
                    markdown_notes,
                    ledger_uuid
                    ))
            self.connection.commit()
            
            self.c.execute("INSERT INTO ledgers(id, name, locked, active, ledger_date) VALUES (?,?,?,?,?)",(ledger_uuid, invoice_number,combo1,combo2,date_1))
            self.connection.commit()
            

            if due > 0:
                self.c.execute(
                    "INSERT INTO transactions(uuid, updated, created, coa_id, journal_entry_id, ledger_id, name, KSH, description, tx_type, transactionsdate) VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                    (uuid1,
                    created,
                    updated,
                    "currentassets",
                    journal_uuid,
                    ledger_uuid,
                    'Accounts Receivable',
                    due,
                    description,
                    debit,
                    order_date))
                self.connection.commit()
                self.c.execute(
                    "INSERT INTO transactions(uuid, updated, created, coa_id, journal_entry_id, ledger_id, name, KSH, description, tx_type, transactionsdate) VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                    (uuid2,
                    created,
                    updated,
                    "revenue",
                    journal_uuid,
                    ledger_uuid,
                    'Product Sales',
                    due2,
                    description,
                    credit,
                    order_date))
                self.connection.commit()
                self.c.execute("INSERT INTO journal_entries(id, ledger_id, activity, description, posted, locked, journal_entrydate) VALUES (?,?,?,?,?,?,?)",(journal_uuid, ledger_uuid, "other", description, "1", "0", order_date))
                self.connection.commit()
            else:
                self.c.execute(
                    "INSERT INTO transactions(uuid, updated, created, coa_id, journal_entry_id, ledger_id, name, KSH, description, tx_type, transactionsdate) VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                    (uuid2,
                    created,
                    updated,
                    "revenue",
                    journal_uuid,
                    ledger_uuid,
                    'Product Sales',
                    total_no_tax,
                    description2,
                    credit,
                    order_date))
                self.connection.commit()
                self.c.execute(
                        "INSERT INTO transactions(uuid, updated, created, coa_id, journal_entry_id, ledger_id, name, KSH, description, tx_type, transactionsdate) VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                        (uuid3,
                        created,
                        updated,
                        "currentassets",
                        journal_uuid,
                        ledger_uuid,
                        'cash and cash equivalents',
                        amount_paid,
                        description2,
                        debit,
                        order_date))
                self.connection.commit()
                self.c.execute("INSERT INTO journal_entries(id, ledger_id, activity, description, posted, locked, journal_entrydate) VALUES (?,?,?,?,?,?,?)",(journal_uuid, ledger_uuid, "other", description, "1", "0", order_date))
                self.connection.commit()

            self.c.execute(
                "INSERT INTO sales SELECT sale_no, UPC, name, category, Quantity, KSH, VAT, totalvat, taxcode, sale_date FROM pos_table")
            bn = self.c.execute("SELECT * FROM sales").fetchall()

            current_num = int(str(self.ui.lineEdit_33.text()))
            new_num = int(current_num + 1)
            new = str(current_num + 1)
            self.c.execute("UPDATE sales_count SET count=?", (new_num,))
            self.connection.commit()
            self.ui.lineEdit_33.setText((new))
            self.c.execute("DELETE FROM pos_table")
            self.poslist = []
            self.kshpos = []
            self.itempos = []
            self.ui.lineEdit_8.clear()
            self.ui.lineEdit_16.clear()
            # self.ui.label_126.clear()
            self.connection.commit()
            self.load_postable_data()
            setButtons(self)
            self.c.close()
            self.connection.close()
            QMessageBox.information(
                QMessageBox(),
                'Successful',
                'Item is added successfully to the database.')
        except Exception:
            QMessageBox.warning(
                QMessageBox(),
                'Error',
                'Could not add Item to the database, Make sure the VAT is set in the tax setting.')
        np = babel.numbers.format_currency(
            decimal.Decimal(grand_total), cash_label, locale='en_US')
        self.ui.label_114.setText(str(np))


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

    oreder_code = str(self.ui.lineEdit_28.text())
    item_name = str(self.ui.lineEdit_29.text())
    description = str(self.ui.lineEdit_30.text())
    quantity = float(self.ui.lineEdit_31.text())
    total_amount = float(self.ui.lineEdit_32.text())
    return_date = date.today()
    name = ("Return of order" + oreder_code)
    paid = 0

    try:
        self.c.execute(
            "INSERT INTO sales_returns(order_code ,  item_name , description , quantity , total_amount  , return_date  ) "
            "VALUES (?,?,?,?,?,?)", (oreder_code, item_name, description, quantity, total_amount, return_date))
        self.connection.commit()
        self.c.execute(
            "UPDATE stock SET Quantity=(Quantity+?) WHERE name=?",
            (quantity,
             item_name))
        self.connection.commit()
        if total_amount > 0:
            self.c.execute(
                "INSERT INTO income(name,  amount, debit, credit, description, income_date) VALUES (?,?,?,?,?,?)",
                (name,
                 total_amount,
                 total_amount,
                 paid,
                 description,
                 return_date))
            self.connection.commit()
            self.c.execute(
                "INSERT INTO transactions(name, KSH, description, debit, credit, transactionsdate) VALUES (?,?,?,?,?,?)",
                (name,
                 description,
                 total_amount,
                 paid,
                 total_amount,
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
