from main import *
from datetime import datetime, date
import sqlite3
from widgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6 import QtCore
from PySide6.QtWidgets import QTableWidgetItem, QMessageBox
basepath = os.path.expanduser('~/Documents')
pathtodb = str(basepath)
newpath = (pathtodb + "\\yobi")
if not os.path.exists(newpath):
    os.makedirs(newpath)


def get_selected_row_details(self):
    row = self.ui.tableWidget_6.currentRow()
    currentcode = (self.ui.tableWidget_6.item(row, 0).text())
    currentcode = (''.join(map(str, currentcode)))
    value = self.ui.dateEdit_3.date()
    print(value)

    self.connection = sqlite3.connect(pathtodb + "\\yobi\\yobi_database.db")
    self.c = self.connection.cursor()
    client_nm = self.c.execute(
        "SELECT client_name FROM orders WHERE code=?", (currentcode,)).fetchone()
    client_nm = (''.join(map(str, client_nm)))

    due_orders = self.c.execute(
        "SELECT due FROM orders WHERE code=?", (currentcode,)).fetchone()
    due_orders = float(''.join(map(str, due_orders)))
    ledger_uuid = self.c.execute(
        "SELECT ledger_uuid FROM orders WHERE code=?", (currentcode,)).fetchone()
    ledger_uuid = (''.join(map(str, ledger_uuid)))

    paid = float(str(self.ui.lineEdit_17.text()))
    due = (due_orders - paid)

    qdate = self.ui.dateEdit_3.date()
    order_date = qdate.toPython()
    cash = float(str(self.ui.lineEdit_17.text()))
    description = (client_nm + " " + "paid" + " " + str(paid))
    created = dt.today()
    updated = dt.today()
    journal_uuid = uuid.uuid4().hex
    uuid1 = uuid.uuid4().hex
    uuid3 = uuid.uuid4().hex

    # order_date = date.today()
    self.g = self.c.execute(
        "UPDATE orders SET due=? WHERE code=? ", (due, currentcode))
    self.connection.commit()
    try:
        self.c.execute(
            "INSERT INTO payment(code,  client_name, payment_date , paid , due ) "
            "VALUES (?,?,?,?,?)", (currentcode, client_nm, order_date, paid, due))
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
            cash,
            description,
            "debit",
            order_date))
        self.connection.commit()
        self.c.execute(
            "INSERT INTO transactions(uuid, updated, created, coa_id, journal_entry_id, ledger_id, name, KSH, description, tx_type, transactionsdate) VALUES (?,?,?,?,?,?,?,?,?,?,?)",
            (uuid1,
            created,
            updated,
            "currentassets",
            journal_uuid,
            ledger_uuid,
            'Accounts Receivable',
            cash,
            description,
            "credit",
            order_date))
        self.connection.commit()
        self.c.execute("INSERT INTO journal_entries(id, ledger_id, activity, description, posted, locked, journal_entrydate) VALUES (?,?,?,?,?,?,?)",(journal_uuid, ledger_uuid, "other", description, "1", "0", order_date))
        self.connection.commit()
        self.c.close()
        self.connection.close()
        QMessageBox.information(
            QMessageBox(),
            'Successful',
            'payment made successfully.')
    except Exception:
        QMessageBox.warning(
            QMessageBox(),
            'Error',
            'Could not add Item to the database.')


def supllier_payment(self):
    row = self.ui.tableWidget_14.currentRow()
    currentcode = (self.ui.tableWidget_14.item(row, 0).text())
    currentcode = (''.join(map(str, currentcode)))
    self.connection = sqlite3.connect(pathtodb + "\\yobi\\yobi_database.db")
    self.c = self.connection.cursor()
    supplier_name = self.c.execute(
        "SELECT name FROM supplier WHERE id_14=?", (currentcode,)).fetchone()
    supplier_name = (''.join(map(str, supplier_name)))

    due_orders = self.c.execute(
        "SELECT owes FROM supplier WHERE id_14=?", (currentcode,)).fetchone()
    due_orders = float(''.join(map(str, due_orders)))

    paid = float(str(self.ui.lineEdit_44.text()))
    due = (due_orders - paid)

    qdate = self.ui.dateEdit_7.date()
    order_date = qdate.toPython()

    debit = 0
    cash = float(str(self.ui.lineEdit_44.text()))
    description = ("paid" + " " + str(paid) + "to" + supplier_name)
    name = ("creditor" + "," + supplier_name)

    # order_date = date.today()
    self.g = self.c.execute(
        "UPDATE supplier SET owes=? WHERE id_14=? ", (due, currentcode))
    self.connection.commit()
    try:
        self.c.execute(
            "INSERT INTO debt_payment(code,  supplier_name, payment_date , paid , due ) "
            "VALUES (?,?,?,?,?)", (currentcode, supplier_name, order_date, paid, due))
        self.c.execute(
            "INSERT INTO short_term_lib(name, KSH, description, debit, credit, stlibdate) VALUES (?,?,?,?,?,?)",
            (name,
             cash,
             description,
             paid,
             debit,
             order_date))
        self.connection.commit()
        self.c.execute(
            "INSERT INTO transactions(name, KSH, description, debit, credit, transactionsdate) VALUES (?,?,?,?,?,?)",
            (name,
             cash,
             description,
             paid,
             debit,
             order_date))
        self.connection.commit()

        if self.ui.comboBox_10.itemText(
                self.ui.comboBox_10.currentIndex()) == 'cash at hand':
            self.c.execute(
                "INSERT INTO current_Asset(name, KSH, description, debit, credit, currAssetDate) VALUES (?,?,?,?,?,?)",
                (name,
                 cash,
                 description,
                 debit,
                 paid,
                 order_date))
            self.connection.commit()
            self.c.execute(
                "INSERT INTO transactions(name, KSH, description, debit, credit, transactionsdate) VALUES (?,?,?,?,?,?)",
                (name,
                 cash,
                 description,
                 debit,
                 paid,
                 order_date))
            self.connection.commit()
            self.c.close()
            self.connection.close()

        elif self.ui.comboBox_10.itemText(self.ui.comboBox_10.currentIndex()) == 'cash from till/paybill':
            self.c.execute(
                "INSERT INTO current_Asset(name, KSH, description, debit, credit, currAssetDate) VALUES (?,?,?,?,?,?)",
                (name,
                 cash,
                 description,
                 debit,
                 paid,
                 order_date))
            self.connection.commit()
            self.c.execute(
                "INSERT INTO transactions(name, KSH, description, debit, credit, transactionsdate) VALUES (?,?,?,?,?,?)",
                (name,
                 cash,
                 description,
                 debit,
                 paid,
                 order_date))
            self.connection.commit()
            self.c.close()
            self.connection.close()

        elif self.ui.comboBox_10.itemText(self.ui.comboBox_10.currentIndex()) == 'cash from creditor':
            self.c.execute(
                "INSERT INTO current_Asset(name, KSH, description, debit, credit, currAssetDate) VALUES (?,?,?,?,?,?)",
                (name,
                 cash,
                 description,
                 debit,
                 paid,
                 order_date))
            self.connection.commit()
            self.c.execute(
                "INSERT INTO transactions(name, KSH, description, debit, credit, transactionsdate) VALUES (?,?,?,?,?,?)",
                (name,
                 cash,
                 description,
                 debit,
                 paid,
                 order_date))
            self.connection.commit()
            self.c.close()
            self.connection.close()

        elif self.ui.comboBox_10.itemText(self.ui.comboBox_10.currentIndex()) == 'cash in bank':
            self.c.execute(
                "INSERT INTO current_Asset(name, KSH, description, debit, credit, currAssetDate) VALUES (?,?,?,?,?,?)",
                (name,
                 cash,
                 description,
                 debit,
                 paid,
                 order_date))
            self.connection.commit()
            self.c.execute(
                "INSERT INTO transactions(name, KSH, description, debit, credit, transactionsdate) VALUES (?,?,?,?,?,?)",
                (name,
                 cash,
                 description,
                 debit,
                 paid,
                 order_date))
            self.connection.commit()
            self.c.close()
            self.connection.close()

        elif self.ui.comboBox_10.itemText(self.ui.comboBox_10.currentIndex()) == 'loan from bank(exeeding a year)':
            self.c.execute(
                "INSERT INTO long_term_lib(name, KSH, description, debit, credit, ltlibdate) VALUES (?,?,?,?,?,?)",
                (name,
                 cash,
                 description,
                 debit,
                 paid,
                 order_date))
            self.connection.commit()
            self.c.close()
            self.connection.close()

        elif self.ui.comboBox_10.itemText(self.ui.comboBox_10.currentIndex()) == 'loan from bank(less than a year)':
            self.c.execute(
                "INSERT INTO short_term_lib(name, KSH, description, debit, credit, stlibdate) VALUES (?,?,?,?,?,?)",
                (name,
                 cash,
                 description,
                 debit,
                 paid,
                 order_date))
            self.connection.commit()
            self.c.execute(
                "INSERT INTO transactions(name, KSH, description, debit, credit, transactionsdate) VALUES (?,?,?,?,?,?)",
                (name,
                 cash,
                 description,
                 debit,
                 paid,
                 order_date))
            self.connection.commit()
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
            'Could not add Item to the database.')


def combo_payments(self):
    self.connection = sqlite3.connect(pathtodb + "\\yobi\\yobi_database.db")
    self.c = self.connection.cursor()
    acc = 'expenses'
    fix_expe = 'fixedexpenses'
    acc_asset_fixed = "fixedassets"
    acc_asset_current = "currentassets"
    acc_lib_short = "currentliabilities"
    acc_lib_long = "Longtermliabilities"
    acc_revenue = "revenue"
    role = [
        "fixedassets",
        "currentassets",
        "currentliabilities",
        "Longtermliabilities",
        "revenue",
        "expenses"
    ]

    fixed_expenses = [
        'mortages',
        'rent',
        'strata fee',
        'vehicle insuarrance',
        'house/tenant insuarance',
        'utility bills(cabel, electricity, water etc.']
    source_of_payments = [
        'cash at hand',
        'loan from bank(exeeding a year)',
        'loan from bank(less than a year)',
        'cash from till/paybill',
        'cash from creditor',
        'cash in bank']

    tx_type = [
        'debit',
        'credit'
    ]

    d = self.c.execute(
        "SELECT account FROM chart_of_accounts WHERE role=?", (acc,)).fetchall()
    fix_expes = self.c.execute(
        "SELECT account FROM chart_of_accounts WHERE role=?", (fix_expe,)).fetchall()
    acc_fix = self.c.execute(
        "SELECT account FROM chart_of_accounts WHERE role=?", (acc_asset_fixed,)).fetchall()
    acc_curr = self.c.execute(
        "SELECT account FROM chart_of_accounts WHERE role=?", (acc_asset_current,)).fetchall()
    acc_short = self.c.execute(
        "SELECT account FROM chart_of_accounts WHERE role=?", (acc_lib_short,)).fetchall()
    acc_long = self.c.execute(
        "SELECT account FROM chart_of_accounts WHERE role=?", (acc_lib_long,)).fetchall()
    acc_rev = self.c.execute(
        "SELECT account FROM chart_of_accounts WHERE role=?", (acc_revenue,)).fetchall()

    b = [item for t in d for item in t]
    fix_expes_combo = [item for t in fix_expes for item in t]
    acc_fix1 = [item for t in acc_fix for item in t]
    acc_curr1 = [item for t in acc_curr for item in t]
    acc_short1 = [item for t in acc_short for item in t]
    acc_long1 = [item for t in acc_long for item in t]
    acc_rev1 = [item for t in acc_rev for item in t]

    self.ui.comboBox_6.addItems(b)
    self.ui.comboBox_22.addItems(b)
    self.ui.comboBox_22.addItems(fix_expes_combo)
    self.ui.comboBox_22.addItems(acc_rev1)
    self.ui.comboBox_22.addItems(acc_fix1)
    self.ui.comboBox_22.addItems(acc_long1)
    self.ui.comboBox_22.addItems(acc_curr1)
    self.ui.comboBox_22.addItems(acc_short1)
    self.ui.comboBox_46.addItems(acc_rev1)
    self.ui.comboBox_46.addItems(acc_fix1)
    self.ui.comboBox_46.addItems(acc_long1)
    self.ui.comboBox_46.addItems(acc_curr1)
    self.ui.comboBox_46.addItems(acc_short1)
    self.ui.comboBox_23.addItems(tx_type)
    self.ui.comboBox_47.addItems(tx_type)
    self.ui.comboBox_50.addItems(tx_type)
    self.ui.comboBox_7.addItems(source_of_payments)
    self.ui.comboBox_10.addItems(source_of_payments)
    self.ui.comboBox_11.addItems(source_of_payments)
    self.ui.comboBox_48.addItems(role)


def automatic_acc(self):
    self.connection = sqlite3.connect(pathtodb + "\\yobi\\yobi_database.db")
    self.c = self.connection.cursor()
    acc = 'fixedassets'
    acc1 = 'currentassets'
    acc2 = 'currentliabilities'
    acc3 = 'Longtermliabilities'
    acc4 = 'fixedexpenses'

    d = self.c.execute(
        "SELECT account FROM chart_of_accounts WHERE role=?", (acc,)).fetchall()
    a = self.c.execute(
        "SELECT account FROM chart_of_accounts WHERE role=?", (acc1,)).fetchall()
    f = self.c.execute(
        "SELECT account FROM chart_of_accounts WHERE role=?", (acc2,)).fetchall()
    c = self.c.execute(
        "SELECT account FROM chart_of_accounts WHERE role=?", (acc3,)).fetchall()
    e = self.c.execute(
        "SELECT account FROM chart_of_accounts WHERE role=?", (acc4,)).fetchall()

    b = [item for t in d for item in t]
    b1 = [item for t in a for item in t]
    b2 = [item for t in f for item in t]
    b3 = [item for t in c for item in t]
    b4 = [item for t in e for item in t]

    name = str(self.ui.comboBox_6.currentText())

    KSH = float(str(self.ui.lineEdit_20.text()))
    credit = float(str(self.ui.lineEdit_20.text()))
    debit = 0
    daate = date.today()
    deb_asset = float(str(self.ui.lineEdit_20.text()))
    cred_asset = 0
    description = str(self.ui.lineEdit_21.text())

    if self.ui.comboBox_6.itemText(self.ui.comboBox_6.currentIndex()) in b:
        self.c.execute(
            "INSERT INTO fixed_Asset(name, KSH, description, debit, credit, fixAssetDate) VALUES (?,?,?,?,?,?)",
            (name,
             KSH,
             description,
             deb_asset,
             cred_asset,
             daate))
        self.connection.commit()
        self.c.execute(
            "INSERT INTO transactions(name, KSH, description, debit, credit, transactionsdate) VALUES (?,?,?,?,?,?)",
            (name,
             KSH,
             description,
             debit,
             credit,
             daate))
        self.connection.commit()
        self.c.execute(
            "INSERT INTO account_payable(name, KSH, description, debit, credit, ledgerdate) VALUES (?,?,?,?,?,?)",
            (name,
             KSH,
             description,
             deb_asset,
             cred_asset,
             daate))
        self.connection.commit()
        self.c.close()
        self.connection.close()
    elif self.ui.comboBox_6.itemText(self.ui.comboBox_6.currentIndex()) in b1:
        self.c.execute(
            "INSERT INTO current_Asset(name, KSH, description, debit, credit, currAssetDate) VALUES (?,?,?,?,?,?)",
            (name,
             KSH,
             description,
             deb_asset,
             cred_asset,
             daate))
        self.connection.commit()
        self.c.execute(
            "INSERT INTO transactions(name, KSH, description, debit, credit, transactionsdate) VALUES (?,?,?,?,?,?)",
            (name,
             KSH,
             description,
             debit,
             credit,
             daate))
        self.connection.commit()
        self.c.execute(
            "INSERT INTO account_payable(name, KSH, description, debit, credit, ledgerdate) VALUES (?,?,?,?,?,?)",
            (name,
             KSH,
             description,
             deb_asset,
             cred_asset,
             daate))
        self.connection.commit()
        self.c.close()
        self.connection.close()

    elif self.ui.comboBox_6.itemText(self.ui.comboBox_6.currentIndex()) in b2:
        self.c.execute(
            "INSERT INTO short_term_lib(name, KSH, description, debit, credit, stlibdate) VALUES (?,?,?,?,?,?)",
            (name,
             KSH,
             description,
             deb_asset,
             cred_asset,
             daate))
        self.connection.commit()
        self.c.execute(
            "INSERT INTO transactions(name, KSH, description, debit, credit, transactionsdate) VALUES (?,?,?,?,?,?)",
            (name,
             KSH,
             description,
             debit,
             credit,
             daate))
        self.connection.commit()
        self.c.execute(
            "INSERT INTO account_payable(name, KSH, description, debit, credit, ledgerdate) VALUES (?,?,?,?,?,?)",
            (name,
             KSH,
             description,
             deb_asset,
             cred_asset,
             daate))
        self.connection.commit()
        self.c.close()
        self.connection.close()

    elif self.ui.comboBox_6.itemText(self.ui.comboBox_6.currentIndex()) in b3:
        self.c.execute(
            "INSERT INTO long_term_lib(name, KSH, description, debit, credit, ltlibdate) VALUES (?,?,?,?,?,?)",
            (name,
             KSH,
             description,
             deb_asset,
             cred_asset,
             daate))
        self.connection.commit()
        self.c.execute(
            "INSERT INTO transactions(name, KSH, description, debit, credit, transactionsdate) VALUES (?,?,?,?,?,?)",
            (name,
             KSH,
             description,
             debit,
             credit,
             daate))
        self.connection.commit()
        self.c.execute(
            "INSERT INTO account_payable(name, KSH, description, debit, credit, transactionsdate) VALUES (?,?,?,?,?,?)",
            (name,
             KSH,
             description,
             deb_asset,
             cred_asset,
             daate))
        self.connection.commit()
        self.c.close()
        self.connection.close()

        # result = self.connection.execute("SELECT * FROM stock WHERE category=?", (category,))
    elif self.ui.comboBox_6.itemText(self.ui.comboBox_6.currentIndex()) in b4:
        self.c.execute(
            "INSERT INTO fix_expe(name, KSH, description, debit, credit, fixdate) VALUES (?,?,?,?,?,?)",
            (name,
             KSH,
             description,
             debit,
             credit,
             daate))
        self.connection.commit()
        self.c.execute(
            "INSERT INTO transactions(name, KSH, description, debit, credit, transactionsdate) VALUES (?,?,?,?,?,?)",
            (name,
             KSH,
             description,
             debit,
             credit,
             daate))
        self.connection.commit()
        self.c.execute(
            "INSERT INTO account_payable(name, KSH, description, debit, credit, transactionsdate) VALUES (?,?,?,?,?,?)",
            (name,
             KSH,
             description,
             debit,
             credit,
             daate))
        self.connection.commit()

    else:
        print("noooooooooooooooooooooooooooooo")

        # result = self.connection.execute("SELECT * FROM stock WHERE name=?", (category,))
    payment_source(self)


def payment_source(self):
    source_of_payments = [
        'cash at hand',
        'loan from bank(exeeding a year)',
        'loan from bank(less than a year)',
        'cash from till/paybill',
        'cash from creditor',
        'cash in bank']
    self.connection = sqlite3.connect(pathtodb + "\\yobi\\yobi_database.db")
    self.c = self.connection.cursor()
    name = str(self.ui.comboBox_6.currentText())

    KSH = float(str(self.ui.lineEdit_20.text()))
    daate = date.today()
    description = str(self.ui.lineEdit_21.text())
    deb_asset = 0
    cred_asset = float(str(self.ui.lineEdit_20.text()))
    if self.ui.comboBox_7.itemText(
            self.ui.comboBox_7.currentIndex()) == 'cash at hand':
        self.c.execute(
            "INSERT INTO current_Asset(name, KSH, description, debit, credit, currAssetDate) VALUES (?,?,?,?,?,?)",
            (name,
             KSH,
             description,
             deb_asset,
             cred_asset,
             daate))
        self.connection.commit()
        self.c.execute(
            "INSERT INTO transactions(name, KSH, description, debit, credit, transactionsdate) VALUES (?,?,?,?,?,?)",
            (name,
             KSH,
             description,
             deb_asset,
             cred_asset,
             daate))
        self.connection.commit()

        self.c.close()
        self.connection.close()

    elif self.ui.comboBox_7.itemText(self.ui.comboBox_7.currentIndex()) == 'cash from till/paybill':
        self.c.execute(
            "INSERT INTO current_Asset(name, KSH, description, debit, credit, currAssetDate) VALUES (?,?,?,?,?,?)",
            (name,
             KSH,
             description,
             deb_asset,
             cred_asset,
             daate))
        self.connection.commit()
        self.c.execute(
            "INSERT INTO transactions(name, KSH, description, debit, credit, transactionsdate) VALUES (?,?,?,?,?,?)",
            (name,
             KSH,
             description,
             deb_asset,
             cred_asset,
             daate))
        self.connection.commit()
        self.c.close()
        self.connection.close()

    elif self.ui.comboBox_7.itemText(self.ui.comboBox_7.currentIndex()) == 'cash from creditor':
        self.c.execute(
            "INSERT INTO current_Asset(name, KSH, description, debit, credit, currAssetDate) VALUES (?,?,?,?,?,?)",
            (name,
             KSH,
             description,
             deb_asset,
             cred_asset,
             daate))
        self.connection.commit()
        self.c.execute(
            "INSERT INTO transactions(name, KSH, description, debit, credit, transactionsdate) VALUES (?,?,?,?,?,?)",
            (name,
             KSH,
             description,
             deb_asset,
             cred_asset,
             daate))
        self.connection.commit()
        self.c.close()
        self.connection.close()

    elif self.ui.comboBox_7.itemText(self.ui.comboBox_7.currentIndex()) == 'cash in bank':
        self.c.execute(
            "INSERT INTO current_Asset(name, KSH, description, debit, credit, currAssetDate) VALUES (?,?,?,?,?,?)",
            (name,
             KSH,
             description,
             deb_asset,
             cred_asset,
             daate))
        self.connection.commit()
        self.c.execute(
            "INSERT INTO transactions(name, KSH, description, debit, credit, transactionsdate) VALUES (?,?,?,?,?,?)",
            (name,
             KSH,
             description,
             deb_asset,
             cred_asset,
             daate))
        self.connection.commit()
        self.c.close()
        self.connection.close()

    elif self.ui.comboBox_7.itemText(self.ui.comboBox_7.currentIndex()) == 'loan from bank(exeeding a year)':
        self.c.execute(
            "INSERT INTO long_term_lib(name, KSH, description, debit, credit, ltlibdate) VALUES (?,?,?,?,?,?)",
            (name,
             KSH,
             description,
             deb_asset,
             cred_asset,
             daate))
        self.connection.commit()
        self.c.close()
        self.connection.close()

    elif self.ui.comboBox_7.itemText(self.ui.comboBox_7.currentIndex()) == 'loan from bank(less than a year)':
        self.c.execute(
            "INSERT INTO short_term_lib(name, KSH, description, debit, credit, stlibdate) VALUES (?,?,?,?,?,?)",
            (name,
             KSH,
             description,
             deb_asset,
             cred_asset,
             daate))
        self.connection.commit()
        self.c.execute(
            "INSERT INTO transactions(name, KSH, description, debit, credit, transactionsdate) VALUES (?,?,?,?,?,?)",
            (name,
             KSH,
             description,
             deb_asset,
             cred_asset,
             daate))
        self.connection.commit()
        self.c.close()
        self.connection.close()


def payment_source_001(self):
    try:

        self.connection = sqlite3.connect(
            pathtodb + "\\yobi\\yobi_database.db")
        self.c = self.connection.cursor()
        supplier = str(self.ui.lineEdit_37.text())

        cred_asset = float(str(self.ui.lineEdit_35.text()))

        qdate = self.ui.dateEdit_6.date()
        daate = qdate.toPython()
        name = (" Creditor" + "," + supplier)
        description = ("paid goods on credit to" + " " + supplier)
        deb_asset = 0
        if self.ui.comboBox_11.itemText(
                self.ui.comboBox_11.currentIndex()) == 'cash at hand':
            self.c.execute(
                "INSERT INTO current_Asset(name, KSH, description, debit, credit, currAssetDate) VALUES (?,?,?,?,?,?)",
                (name,
                 cred_asset,
                 description,
                 deb_asset,
                 cred_asset,
                 daate))
            self.connection.commit()
            self.c.execute(
                "INSERT INTO transactions(name, KSH, description, debit, credit, transactionsdate) VALUES (?,?,?,?,?,?)",
                (name,
                 cred_asset,
                 description,
                 deb_asset,
                 cred_asset,
                 daate))
            self.connection.commit()
            self.c.close()
            self.connection.close()

        elif self.ui.comboBox_11.itemText(self.ui.comboBox_11.currentIndex()) == 'cash from till/paybill':
            self.c.execute(
                "INSERT INTO current_Asset(name, KSH, description, debit, credit, currAssetDate) VALUES (?,?,?,?,?,?)",
                (name,
                 cred_asset,
                 description,
                 deb_asset,
                 cred_asset,
                 daate))
            self.connection.commit()
            self.c.execute(
                "INSERT INTO transactions(name, KSH, description, debit, credit, transactionsdate) VALUES (?,?,?,?,?,?)",
                (name,
                 cred_asset,
                 description,
                 deb_asset,
                 cred_asset,
                 daate))
            self.connection.commit()
            self.c.close()
            self.connection.close()

        elif self.ui.comboBox_11.itemText(self.ui.comboBox_11.currentIndex()) == 'cash from creditor':
            self.c.execute(
                "INSERT INTO current_Asset(name, KSH, description, debit, credit, currAssetDate) VALUES (?,?,?,?,?,?)",
                (name,
                 cred_asset,
                 description,
                 deb_asset,
                 cred_asset,
                 daate))
            self.connection.commit()
            self.c.execute(
                "INSERT INTO transactions(name, KSH, description, debit, credit, transactionsdate) VALUES (?,?,?,?,?,?)",
                (name,
                 cred_asset,
                 description,
                 deb_asset,
                 cred_asset,
                 daate))
            self.connection.commit()
            self.c.close()
            self.connection.close()

        elif self.ui.comboBox_11.itemText(self.ui.comboBox_11.currentIndex()) == 'cash in bank':
            self.c.execute(
                "INSERT INTO current_Asset(name, KSH, description, debit, credit, currAssetDate) VALUES (?,?,?,?,?,?)",
                (name,
                 cred_asset,
                 description,
                 deb_asset,
                 cred_asset,
                 daate))
            self.connection.commit()
            self.c.execute(
                "INSERT INTO transactions(name, KSH, description, debit, credit, transactionsdate) VALUES (?,?,?,?,?,?)",
                (name,
                 cred_asset,
                 description,
                 deb_asset,
                 cred_asset,
                 daate))
            self.connection.commit()
            self.c.close()
            self.connection.close()

        elif self.ui.comboBox_11.itemText(self.ui.comboBox_11.currentIndex()) == 'loan from bank(exeeding a year)':
            self.c.execute(
                "INSERT INTO long_term_lib(name, KSH, description, debit, credit, ltlibdate) VALUES (?,?,?,?,?,?)",
                (name,
                 cred_asset,
                 description,
                 deb_asset,
                 cred_asset,
                 daate))
            self.connection.commit()
            self.c.close()
            self.connection.close()

        elif self.ui.comboBox_11.itemText(self.ui.comboBox_11.currentIndex()) == 'loan from bank(less than a year)':
            self.c.execute(
                "INSERT INTO short_term_lib(name, KSH, description, debit, credit, stlibdate) VALUES (?,?,?,?,?,?)",
                (name,
                 cred_asset,
                 description,
                 deb_asset,
                 cred_asset,
                 daate))
            self.connection.commit()
            self.c.execute(
                "INSERT INTO transactions(name, KSH, description, debit, credit, transactionsdate) VALUES (?,?,?,?,?,?)",
                (name,
                 cred_asset,
                 description,
                 deb_asset,
                 cred_asset,
                 daate))
            self.connection.commit()
            self.c.close()
            self.connection.close()
    except Exception:
        print("source of payment")


def purchase_order_payment(self):
    self.connection = sqlite3.connect(pathtodb + "\\yobi\\yobi_database.db")
    self.c = self.connection.cursor()

    supplier = str(self.ui.lineEdit_37.text())
    item = str(self.ui.lineEdit_38.text())
    quantity = float(str(self.ui.lineEdit_36.text()))
    purchase_code = str(self.ui.lineEdit_26.text())
    transportation = float(str(self.ui.lineEdit_34.text()))
    cost_items = float(str(self.ui.lineEdit_35.text()))
    owes = float(str(self.ui.lineEdit.text()))

    qdate = self.ui.dateEdit_6.date()
    order_date = qdate.toPython()
    name = (" Creditor" + "," + supplier)
    description = (supplier + "sold goods to you on credit")
    debit = 0

    #self.g = self.c.execute("UPDATE orders SET due=? WHERE code=? ", (due, currentcode))
    try:
        self.c.execute(
            "INSERT INTO Purchase(purchase_code ,  supplier , item , quantity, total_amount , transport, owes, date) VALUES (?,?,?,?,?,?,?,?)",
            ((purchase_code,
              supplier,
              item,
              quantity,
              cost_items,
              transportation,
              owes,
              order_date)))
        self.y = self.c.execute(
            "SELECT (Quantity + ?) FROM stock WHERE name=? ", (quantity, item)).fetchone()
        self.y = float(''.join(map(str, self.y)))
        self.c.execute(
            "UPDATE stock SET Quantity=? WHERE UPC=?", (self.y, item))
        self.connection.commit()
        if owes > 0:
            b = self.c.execute(
                "SELECT owes FROM supplier WHERE name=?", (supplier,)).fetchone()
            b = float(''.join(map(str, b)))
            self.c.execute(
                "UPDATE supplier SET owes=(owes+?) WHERE name=?", (owes, supplier))
            self.connection.commit()
            self.c.execute(
                "INSERT INTO short_term_lib(name, KSH, description, debit, credit, stlibdate) VALUES (?,?,?,?,?,?)",
                (name,
                 owes,
                 description,
                 debit,
                 owes,
                 order_date))
            self.connection.commit()
            self.c.execute(
                "INSERT INTO transactions(name, KSH, description, debit, credit, transactionsdate) VALUES (?,?,?,?,?,?)",
                (name,
                 owes,
                 description,
                 debit,
                 owes,
                 order_date))
            self.connection.commit()
        payment_source_001(self)

        self.connection.close()
        QMessageBox.information(
            QMessageBox(),
            'Successful',
            'Item is added successfully to the database.')
    except Exception:
        QMessageBox.warning(
            QMessageBox(),
            'Error',
            'Could not add Item to the database.')


def ledger_load(self):
    try:
        self.connection = sqlite3.connect(
            pathtodb + "\\yobi\\yobi_database.db")
        query = "SELECT * FROM account_payable"
        result = self.connection.execute(query).fetchall()
        self.ui.tableWidget_17.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableWidget_17.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableWidget_17.setItem(
                    row_number,
                    column_number,
                    QTableWidgetItem(
                        str(data)))
    except Exception:
        print("transactions loading")


def add_coa(self):
    self.connection = sqlite3.connect(pathtodb + "\\yobi\\yobi_database.db")
    self.c = self.connection.cursor()
    b = self.c.execute("SELECT * FROM chart_of_accounts").fetchone()

    if b is None:
        rows = [(1550, 'fixedassets', 'Buildings', 'debit', 0, 1),
                (1511, 'fixedassets', 'computer equipment', 'debit', 0, 1),
                (1512, 'fixedassets', 'computer software', 'debit', 0, 1),
                (1500, 'fixedassets', 'funiture and fixtures', 'debit', 0, 1),
                (1920, 'fixedassets', 'intagible asset', 'debit', 0, 1),
                (1520, 'fixedassets', 'machinery', 'debit', 0, 1),
                (1510, 'fixedassets', 'office equipment', 'debit', 0, 1),
                (1570, 'fixedassets', 'leasehold improvements', 'debit', 0, 1),
                (1560, 'fixedassets', 'construction in progress', 'debit', 0, 1),
                (1690, 'fixedassets', 'land', 'debit', 0, 1),
                (1010, 'currentassets', 'cash and cash equivalents', 'debit', 0, 1),
                (1420, 'currentassets', 'marketable Securities', 'debit', 0, 1),
                (1100, 'currentassets', 'Accounts Receivable', 'debit', 0, 1),
                (1205, 'currentassets', 'supplies', 'debit', 0, 1),
                (1206, 'currentassets', 'debtors', 'debit', 0, 1),
                (1400, 'currentassets', 'prepaid Expenses', 'debit', 0, 1),
                (1200, 'currentassets', 'inventory', 'debit', 0, 1),
                (1000, 'currentassets', 'petty cash', 'debit', 0, 1),
                (1410, 'currentassets', 'Employee Advances', 'debit', 0, 1),
                (2000, 'currentliabilities', 'accounts payable', 'credit', 0, 1),
                (2330, 'currentliabilities', 'credit lines', 'credit', 0, 1),
                (2320, 'currentliabilities', 'salaries', 'credit', 0, 1),
                (2030, 'currentliabilities', 'intrest payable', 'credit', 0, 1),
                (2390, 'currentliabilities', 'income taxes payable', 'credit', 0, 1),
                (2370, 'currentliabilities', 'bills payble', 'credit', 0, 1),
                (2450, 'currentliabilities', 'short term loans', 'credit', 0, 1),
                (2300, 'currentliabilities', 'accured expenses', 'credit', 0, 1),
                (2460, 'currentliabilities', 'bank account overdrafts', 'credit', 0, 1),
                (2480, 'currentliabilities', 'creditors', 'credit', 0, 1),
                (2490, 'currentliabilities', 'Deferred Revenue', 'credit', 0, 1),
                (2704, 'Longtermliabilities', 'mortages or bonds', 'credit', 0, 1),
                (2702, 'Longtermliabilities', 'capital lease', 'credit', 0, 1),
                (2740, 'Longtermliabilities', 'Bonds Payable', 'credit', 0, 1),
                (2700, 'Longtermliabilities', 'Notes Payable', 'credit', 0, 1),
                (6001, 'fixedexpenses', 'mortages', 'debit', 0, 1),
                (7400, 'fixedexpenses', 'rent', 'debit', 0, 1),
                (7440, 'fixedexpenses', 'strata fee', 'debit', 0, 1),
                (6730, 'fixedexpenses', 'vehicle insuarrance', 'debit', 0, 1),
                (6630, 'fixedexpenses', 'house/tenant insuarance', 'debit', 0, 1),
                (7800, 'fixedexpenses', 'utilities bills(cabel)', 'debit', 0, 1),
                (6000, 'expenses', 'Default Purchase Expense', 'debit', 0, 1),
                (6010, 'expenses', 'Advertising Expense', 'debit', 0, 1),
                (6011, 'expenses', 'cost of goods sold', 'debit', 0, 1),
                (6050, 'expenses', 'Amortization Expense', 'debit', 0, 1),
                (6300, 'expenses', 'Charitable Contributions Expense', 'debit', 0, 1),
                (6100, 'expenses', 'Auto Expense', 'debit', 0, 1),
                (6150, 'expenses', 'Bad Debt Expense', 'debit', 0, 1),
                (6250, 'expenses', 'Cash Over and Short ', 'debit', 0, 1),
                (6200, 'expenses', 'Bank fees ', 'debit', 0, 1),
                (6350, 'expenses', 'Commissions and Fees expenses ', 'debit', 0, 1),
                (6400, 'expenses', 'Depreciation expenses ', 'debit', 0, 1),
                (6450, 'expenses', 'Dues and Subscriptions expenses ', 'debit', 0, 1),
                (6500, 'expenses', 'Employee Benefit Expense, Health Insurance ', 'debit', 0, 1),
                (6510, 'expenses', 'Employee Benefit Expense,Pension Plans ', 'debit', 0, 1),
                (6520, 'expenses', 'Employee Benefit Expense,Profit Sharing Plans ', 'debit', 0, 1),
                (6530, 'expenses', 'Employee Benefit Expense,Other ', 'debit', 0, 1),
                (6550, 'expenses', 'Freight Expense ', 'debit', 0, 1),
                (6600, 'expenses', 'Gifts Expense ', 'debit', 0, 1),
                (6650, 'expenses', 'Income Tax Expense,Federal ', 'debit', 0, 1),
                (6660, 'expenses', 'Income Tax Expense,State ', 'debit', 0, 1),
                (6670, 'expenses', 'Income Tax Expense,Local ', 'debit', 0, 1),
                (6700, 'expenses', 'Insurance Expense,Product Liability ', 'debit', 0, 1),
                (6710, 'expenses', 'Insurance Expense,Vehicle ', 'debit', 0, 1),
                (6750, 'expenses', 'Intrest Expense ', 'debit', 0, 1),
                (6800, 'expenses', 'Laundry and Dry Cleaning Expense ', 'debit', 0, 1),
                (6850, 'expenses', 'Legal and Professional Expense ', 'debit', 0, 1),
                (6900, 'expenses', 'Licenses Expense ', 'debit', 0, 1),
                (6950, 'expenses', 'Loss on NSF Checks ', 'debit', 0, 1),
                (7000, 'expenses', 'Maintanance Expence', 'debit', 0, 1),
                (7050, 'expenses', 'Meals and Entertainment Expense', 'debit', 0, 1),
                (4000, 'revenue', 'Product Sales', 'credit', 0, 1),
                (4060, 'revenue', 'interest income', 'credit', 0, 1),
                (4080, 'revenue', 'other income', 'credit', 0, 1),
                (4540, 'revenue', 'Finance charge income', 'credit', 0, 1),
                (4550, 'revenue', 'Shipping  Charges Reimbbursed', 'credit', 0, 1),
                (4800, 'revenue', 'Sales Returns and Allowances', 'credit', 0, 1),
                (4900, 'revenue', 'Sales Discounts', 'credit', 0, 1),]
                
        self.c.executemany("INSERT INTO chart_of_accounts VALUES (?,?,?,?,?,?)", rows)
        self.connection.commit()
    else:
        print("chart_of_accounts is full")