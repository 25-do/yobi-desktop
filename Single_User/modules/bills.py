import os
import sqlite3
import logging
import babel.numbers
import decimal
from modules.contextmanager.contex_manager import SQLite_CONTEX_MANAGER
from PySide6 import QtGui
from PySide6 import QtCore
from PySide6.QtWidgets import QPushButton, QTableWidgetItem
from modules.tableclass import TableQt
basepath = os.path.expanduser('~/Documents')
pathtodb = str(basepath)
newpath = (pathtodb + "\\yobi")
if not os.path.exists(newpath):
    os.makedirs(newpath)
try:
    conn = sqlite3.connect(pathtodb + "\\yobi\\yobi_database.db")
    c = conn.cursor()
    cash_label = c.execute(
            "SELECT currency FROM recip_detail WHERE id_17=1").fetchone()
    cash_label = (''.join(map(str, cash_label)))
    c.close()
except Exception:
    cash_label = "$"

class Bill:
    def bill_load_table(self):
        TableQt.loadtable(
            self.ui.tableWidget_30,
            [5,6],
            [self.bill_details_page, self.bill_update_page],
            "SELECT bill_number, date, vendor_id, amount_due, amount_paid FROM bill",
            ["Details", "Update"]
        )

    def billed_items_load_table(self):
        logging.basicConfig(level=logging.INFO)
        with SQLite_CONTEX_MANAGER(file_name=pathtodb + "\\yobi\\yobi_database.db") as cusr:
            row = self.ui.tableWidget_30.currentRow()
            currentcode = (self.ui.tableWidget_30.item(row, 0).text())
            currentcode = (''.join(map(str, currentcode)))
            currentcode2 = cusr.execute("SELECT uuid FROM bill WHERE bill_number=?", (currentcode,)).fetchone()
            print(currentcode2)
            currentcode2 = (''.join(map(str, currentcode2)))
            TableQt.load_table_no_buttons(
                self.ui.tableWidget_33,
                "SELECT name, amount FROM bill_item WHERE bill_uuid=?",
                currentcode2
            )

    def bill_items_load_table(self):
        database_connection = sqlite3.connect(
                pathtodb + "\\yobi\\yobi_database.db")
        cusr = database_connection.cursor()
        row = self.ui.tableWidget_30.currentRow()
        currentcode = (self.ui.tableWidget_30.item(row, 0).text())
        currentcode = (''.join(map(str, currentcode)))
        currentcode2 = cusr.execute("SELECT uuid FROM bill WHERE bill_number=?", (currentcode,)).fetchone()
        print(currentcode2)
        currentcode2 = (''.join(map(str, currentcode2)))
        result = cusr.execute("SELECT name, amount FROM bill_item WHERE bill_uuid=?", (currentcode2,)).fetchall()
        print("##", result)

        self.ui.tableWidget_31.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableWidget_31.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableWidget_31.setItem(
                    row_number,
                    column_number,
                    QTableWidgetItem(
                        str(data)))

    def bill_transaction_load_table(self):
        try:
            database_connection = sqlite3.connect(
                    pathtodb + "\\yobi\\yobi_database.db")
            cusr = database_connection.cursor()
            row = self.ui.tableWidget_30.currentRow()
            currentcode = (self.ui.tableWidget_30.item(row, 0).text())
            currentcode = (''.join(map(str, currentcode)))
            currentcode2 = cusr.execute("SELECT uuid FROM bill WHERE bill_number=?", (currentcode,)).fetchone()
            print(currentcode2)
            currentcode2 = (''.join(map(str, currentcode2)))
        
            b = cusr.execute('SELECT id FROM ledgers WHERE name=?', (currentcode,)).fetchone()
            b = (''.join(map(str, b)))
            journal_entries_id = cusr.execute('SELECT id FROM journal_entries WHERE ledger_id=?', (b,)).fetchone()
            journal_entries_id = (''.join(map(str, journal_entries_id)))
            result = cusr.execute("SELECT transactionsdate, name,  description, debit , credit FROM transactions WHERE journal_entry_id=?", (journal_entries_id,)).fetchall()
            print("##", result)

            self.ui.tableWidget_32.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.ui.tableWidget_32.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.ui.tableWidget_32.setItem(
                        row_number,
                        column_number,
                        QTableWidgetItem(
                            str(data)))

                    btn = QPushButton("Details")
                    font = QtGui.QFont()
                    font.setPointSize(9)
                    font.setBold(True)
                    # font.setWeight(75)
                    btn.setFont(font)
                    btn.setStyleSheet(u"QPushButton{\n"
                                        "\n"
                                        "border-radius : 20px;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "	background-color: rgb(85, 170, 255);\n"
                                        "}")
                    push = QPushButton("Update")
                    push.setStyleSheet(u"QPushButton{\n"
                                        "\n"
                                        "border-radius : 20px;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "	background-color: rgb(85, 170, 255);\n"
                                        "}")
                    # self.ui.tableWidget_26.setCellWidget(row_number, 3, btn)
                    # self.ui.tableWidget_26.setCellWidget(row_number, 4, push)
                    # btn.clicked.connect(self.jornal_entry_transactions)
                    # push.clicked.connect(self.jornal_entry_update_page)
        except Exception:
            print("#@", "This bill has not yet been Posted", "#@")
        
    def BILL_UPDATE_page(self):
        self.ui.plainTextEdit_3.clear()
        logging.basicConfig(level=logging.INFO)
        with SQLite_CONTEX_MANAGER(file_name=pathtodb + "\\yobi\\yobi_database.db") as cusr:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_39)
            Bill.billed_items_load_table(self)
            row = self.ui.tableWidget_30.currentRow()
            currentcode = (self.ui.tableWidget_30.item(row, 2).text())
            currentcode = (''.join(map(str, currentcode)))

            currentcode2 = (self.ui.tableWidget_30.item(row, 0).text())
            currentcode2 = (''.join(map(str, currentcode2)))

            self.ui.label_275.setText(currentcode)
            self.ui.label_275.setAlignment(QtCore.Qt.AlignCenter)
            self.ui.label_275.setFont(QtGui.QFont("Times", 20))
            column_list = ["addres", "contact", "email"]
            labels = [
                self.ui.label_277,
                self.ui.label_276,
                self.ui.label_278
            ]
            for col, edits in zip(column_list, labels):
                var_y = cusr.execute(
                    "SELECT %s FROM supplier WHERE name=? " %
                    (str(
                        col,)), (currentcode,)).fetchone()
                var_y = (''.join(map(str, var_y)))
                edits.setText((var_y))
                edits.setFont(QtGui.QFont("Times", 17))
            expense = "expenses"
            amount_paid = cusr.execute("SELECT amount_paid FROM bill WHERE bill_number=?", (currentcode2,)).fetchone()
            amount_paid = (''.join(map(str, amount_paid)))
            amount_due = cusr.execute("SELECT amount_due FROM bill WHERE bill_number=?", (currentcode2,)).fetchone()
            amount_due = (''.join(map(str, amount_due)))
            
            external_refrence = cusr.execute("SELECT xref FROM bill WHERE bill_number=?", (currentcode2,)).fetchone()
            external_refrence = (''.join(map(str, external_refrence)))
            external_refrence = cusr.execute("SELECT xref FROM bill WHERE bill_number=?", (currentcode2,)).fetchone()
            external_refrence = (''.join(map(str, external_refrence)))
            terms_bill = cusr.execute("SELECT terms FROM bill WHERE bill_number=?", (currentcode2,)).fetchone()
            terms_bill = (''.join(map(str, terms_bill)))
            bill_status = cusr.execute("SELECT bill_status FROM bill WHERE bill_number=?", (currentcode2,)).fetchone()
            bill_status = (''.join(map(str, bill_status)))
            notes = cusr.execute("SELECT markdown_notes FROM bill WHERE bill_number=?", (currentcode2,)).fetchone()
            notes = (''.join(map(str, notes)))
            
            # paid_date = cusr.execute("SELECT paid_date FROM bill WHERE bill_number=?", (currentcode2,)).fetchone()
            # paid_date = (''.join(map(str, paid_date)))
            # paid_date_re = (re.sub("[-]", ",", paid_date))
            # print('@@@@@@@@@@@@@@@@@@@@@@@@', paid_date_re)
            if amount_paid == str(None):
                amount_paid = 0.0
            if amount_due == str(None):
                amount_due = 0.0
            if external_refrence == str(None):
                external_refrence = 0.0
            self.ui.lineEdit_45.setText(amount_paid)
            self.ui.lineEdit_58.setText(amount_due)
            self.ui.lineEdit_59.setText(external_refrence)
            self.ui.comboBox_17.setCurrentText(terms_bill)
            self.ui.comboBox_18.setCurrentText(bill_status)
            self.ui.plainTextEdit_3.insertPlainText(notes)
            # da = QDate(int(paid_date_re))
            # print("daaaaaaaaaaaaaa", da)
            # self.ui.dateEdit_8.setDate(da)


    def BILL_DETAILS_page(self):
        """displays in detail the statuts of a bill i.e if its paid, approved, due date etc
            and sets data to labes on this page
        """
        self.ui.label_298.clear()
        self.ui.textEdit_4.clear()
        database_connection = sqlite3.connect(
                pathtodb + "\\yobi\\yobi_database.db")
        cusr = database_connection.cursor()
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_38) # sets the details page
        row = self.ui.tableWidget_30.currentRow()
        currentcode = (self.ui.tableWidget_30.item(row, 2).text())
        currentcode = (''.join(map(str, currentcode)))

        currentcode2 = (self.ui.tableWidget_30.item(row, 0).text())
        currentcode2 = (''.join(map(str, currentcode2)))
        # for loop to set different labels in details page with data such as vendor info
        ispurchase_order = cusr.execute("SELECT ispurchase_order FROM bill WHERE bill_number=?", (currentcode2,)).fetchone()
        ispurchase_order = (''.join(map(str, ispurchase_order)))
        print("###############################", ispurchase_order)
        if ispurchase_order == '1':
            self.ui.label_298.setText("PO")
            self.ui.label_298.setAlignment(QtCore.Qt.AlignCenter)
            self.ui.label_298.setFont(QtGui.QFont("Times", 20))
        else:
            print("not purchase order")
        column_list = ["addr1", "tel1", "email"]
        labels = [
            self.ui.label_254,
            self.ui.label_255,
            self.ui.label_258,
            self.ui.label_259
        ]
        for col, edits in zip(column_list, labels):
            var_y = cusr.execute(
                "SELECT %s FROM supplier WHERE name=? " %
                (str(
                    col,)), (currentcode,)).fetchone()
            var_y = (''.join(map(str, var_y)))
            edits.setText((var_y))
            edits.setFont(QtGui.QFont("Times", 17))
        self.ui.label_253.setText(currentcode)
        self.ui.label_253.setAlignment(QtCore.Qt.AlignCenter)
        self.ui.label_253.setFont(QtGui.QFont("Times", 20))

        amount_paid = cusr.execute("SELECT amount_paid FROM bill WHERE bill_number=?", (currentcode2,)).fetchone()
        amount_paid = (''.join(map(str, amount_paid)))
        np = babel.numbers.format_currency(
            decimal.Decimal(amount_paid), cash_label, locale='en_US')

        self.ui.label_250.setText(np)
        self.ui.label_250.setAlignment(QtCore.Qt.AlignCenter)
        self.ui.label_250.setFont(QtGui.QFont("Times", 20))
        self.ui.label_268.setText(np)
        self.ui.label_268.setAlignment(QtCore.Qt.AlignCenter)
        self.ui.label_268.setFont(QtGui.QFont("Times", 20))
        stauts = cusr.execute("SELECT bill_status FROM bill WHERE bill_number=?", (currentcode2,)).fetchone()
        stauts = (''.join(map(str, stauts)))

        amount_due = cusr.execute("SELECT amount_due FROM bill WHERE bill_number=?", (currentcode2,)).fetchone()
        amount_due = float(''.join(map(str, amount_due)))
        amount_p = cusr.execute("SELECT amount_paid FROM bill WHERE bill_number=?", (currentcode2,)).fetchone()
        amount_p = float(''.join(map(str, amount_p)))
        amount_due1 = (amount_due - amount_p)


        np2 = babel.numbers.format_currency(
            decimal.Decimal(amount_due1), cash_label, locale='en_US')
            

        self.ui.label_241.setText(stauts)
        self.ui.label_241.setAlignment(QtCore.Qt.AlignCenter)
        self.ui.label_241.setFont(QtGui.QFont("Times", 20))
        self.ui.label_269.setText(np2)
        self.ui.label_269.setAlignment(QtCore.Qt.AlignCenter)
        self.ui.label_269.setFont(QtGui.QFont("Times", 20))

        notes = cusr.execute("SELECT markdown_notes FROM bill WHERE bill_number=?", (currentcode2,)).fetchone()
        notes = (''.join(map(str, notes)))
        Bill.unearned_account(self)
        Bill.prepaid_expenses(self)
        Bill.BILL_TRANSACTIONS_details_page_table(self)
        self.ui.textEdit_4.insertPlainText(notes)
        Bill.bill_items_load_table(self)
        Bill.bill_transaction_load_table(self)

    def unearned_account(self):
        try:

            logging.basicConfig(level=logging.INFO)
            with SQLite_CONTEX_MANAGER(file_name=pathtodb + "\\yobi\\yobi_database.db") as cusr:
                row = self.ui.tableWidget_30.currentRow()
                currentcode = (self.ui.tableWidget_30.item(row, 0).text())
                currentcode = (''.join(map(str, currentcode)))
                b = cusr.execute('SELECT id FROM ledgers WHERE name=?', (currentcode,)).fetchone()
                b = (''.join(map(str, b)))
                unearned_acc = "Deferred Revenue"
                unearned_account = cusr.execute("SELECT SUM(KSH) FROM transactions WHERE name=? AND ledger_id=?", (unearned_acc, b)).fetchone()
                unearned_account = (''.join(map(str, unearned_account)))
                unearned = babel.numbers.format_currency(
                decimal.Decimal(unearned_account), cash_label, locale='en_US')

                self.ui.label_293.setText(unearned)
                self.ui.label_293.setAlignment(QtCore.Qt.AlignCenter)
                self.ui.label_293.setFont(QtGui.QFont("Times", 20))
        except Exception:
            print(f"this is the exception {Exception}")
            # dave@gmail.com
    def prepaid_expenses(self):
        try:
            logging.basicConfig(level=logging.INFO)
            with SQLite_CONTEX_MANAGER(file_name=pathtodb + "\\yobi\\yobi_database.db") as cusr:
                row = self.ui.tableWidget_30.currentRow()
                currentcode = (self.ui.tableWidget_30.item(row, 0).text())
                currentcode = (''.join(map(str, currentcode)))
                b = cusr.execute('SELECT id FROM ledgers WHERE name=?', (currentcode,)).fetchone()
                b = (''.join(map(str, b)))
                unearned_acc = "prepaid Expenses"
                prepaid_expenses = cusr.execute("SELECT SUM(KSH) FROM transactions WHERE name=? AND ledger_id=?", (unearned_acc, b)).fetchone()
                prepaid_expenses = (''.join(map(str, prepaid_expenses)))
                unearned = babel.numbers.format_currency(
                decimal.Decimal(prepaid_expenses), cash_label, locale='en_US')

                self.ui.label_291.setText(unearned)
                self.ui.label_291.setAlignment(QtCore.Qt.AlignCenter)
                self.ui.label_291.setFont(QtGui.QFont("Times", 20))
                # dave@gmail.com
        except Exception:
            print("this is another excepfi")
        
    
    def BILL_TRANSACTIONS_details_page_table(self):
        logging.basicConfig(level=logging.INFO)
        with SQLite_CONTEX_MANAGER(file_name=pathtodb + "\\yobi\\yobi_database.db") as cusr:
            row = self.ui.tableWidget_30.currentRow()
            currentcode = (self.ui.tableWidget_30.item(row, 0).text())
            currentcode = (''.join(map(str, currentcode)))
            b = cusr.execute('SELECT id FROM ledgers WHERE name=?', (currentcode,)).fetchone()
            b = (''.join(map(str, b)))
            result = cusr.execute("SELECT transactionsdate, coa_id, name, tx_type, description FROM transactions WHERE ledger_id=?", (b,)).fetchall()

            self.ui.tableWidget_32.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.ui.tableWidget_32.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.ui.tableWidget_32.setItem(
                        row_number,
                        column_number,
                        QTableWidgetItem(
                            str(data)))
                    btn = QPushButton("TXS")
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
                    self.ui.tableWidget_26.setCellWidget(row_number, 4, btn)
                    btn.clicked.connect(self.jouranal_entry_transaction)
                # dave@gmail.com