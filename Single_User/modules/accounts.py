import traceback
from PySide6 import QtWidgets
from PySide6.QtWidgets import QTableWidgetItem
from main import *
import os
import unittest
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
    c.close()
except Exception:
    cash_label = "$"


html = """<style>
@import "https://fonts.googleapis.com/css?family=Montserrat:300,400,700";
.rwd-table {
  margin: 1em 0;
  min-width: 300px;
}
.rwd-table tr {
  border-top: 1px solid #ddd;
  border-bottom: 1px solid #ddd;
}
.rwd-table th {
  display: none;
}
.rwd-table td {
  display: block;
}
.rwd-table td:first-child {
  padding-top: .5em;
}
.rwd-table td:last-child {
  padding-bottom: .5em;
}
.rwd-table td:before {
  content: attr(data-th) ": ";
  font-weight: bold;
  width: 6.5em;
  display: inline-block;
}
@media (min-width: 480px) {
  .rwd-table td:before {
    display: none;
  }
}
.rwd-table th, .rwd-table td {
  text-align: left;
}
@media (min-width: 480px) {
  .rwd-table th, .rwd-table td {
    display: table-cell;
    padding: .25em .5em;
  }
  .rwd-table th:first-child, .rwd-table td:first-child {
    padding-left: 0;
  }
  .rwd-table th:last-child, .rwd-table td:last-child {
    padding-right: 0;
  }
}


h1 {
  font-weight: normal;
  letter-spacing: -1px;
  color: #34495E;
}

.rwd-table {
  background: #ffffff;
  color: #00000c;
  border-radius: .4em;
  overflow: hidden;
}
.rwd-table tr {
  border-color: #46637f;
}
.rwd-table th, .rwd-table td {
  margin: .5em 1em;
}
@media (min-width: 480px) {
  .rwd-table th, .rwd-table td {
    padding: 1em !important;
  }
}
.rwd-table th, .rwd-table td:before {
  color: #00000c;
}
</style>
<script>
  window.console = window.console || function(t) {};
</script>
<script>
  if (document.location.search.match(/type=embed/gi)) {
    window.parent.postMessage("resize", "*");
  }
</script>"""


def profit_loss_account(self):
    self.connection = sqlite3.connect(pathtodb + "\\yobi\\yobi_database.db")
    self.c = self.connection.cursor()
    self.ui.treeWidget.clear()
    self.c.execute("DELETE FROM report_printing")
    self.connection.commit()
    sales(self)
    sales_returns(self)
    revenuet(self)
    gross_pr(self)

    qdate = self.ui.dateEdit_4.date()
    order_date = qdate.toPython()

    qdate = self.ui.dateEdit_5.date()
    order_date2 = qdate.toPython()

    alltb = self.c.execute(
        "SELECT name, KSH FROM transactions WHERE transactionsdate BETWEEN ? AND ? AND coa_id=?",
        (order_date,
         order_date2,
         "fixedexpenses"
         )).fetchall()
    var_expe = self.c.execute(
        "SELECT name, KSH FROM transactions WHERE transactionsdate BETWEEN ? AND ? AND coa_id=?",
        (order_date,
         order_date2,
         "expenses"
         )).fetchall()
    cogs = self.c.execute(
        "SELECT SUM(Buying_price) FROM stock WHERE stockdate BETWEEN ? AND ?",
        (order_date,
         order_date2)).fetchone()
    fix_sum = self.c.execute(
        "SELECT SUM(KSH) FROM transactions WHERE transactionsdate BETWEEN ? AND ? AND coa_id=? AND tx_type=?",
        (order_date,
         order_date2,
         "fixedexpenses",
         "debit"
         )).fetchone()

    var_sum = self.c.execute(
        "SELECT SUM(KSH) FROM transactions WHERE transactionsdate BETWEEN ? AND ? AND coa_id=? AND tx_type=?",
        (order_date,
         order_date2,
         "expenses",
         "debit"
         )).fetchone()
    self.c.execute(
        "INSERT INTO report_printing SELECT name, KSH FROM transactions WHERE transactionsdate BETWEEN ? AND ? AND coa_id=?",
        (order_date,
         order_date2,
         "fixedexpenses"
         ))
    self.connection.commit()
    self.c.execute(
        "INSERT INTO report_printing SELECT name, KSH FROM transactions WHERE transactionsdate BETWEEN ? AND ? AND coa_id=?",
        (order_date,
         order_date2,
         "expenses"
         ))
    self.connection.commit()
    cogs = (''.join(map(str, cogs)))
    if cogs == str(None):
        cogs = 0.0
    else:
        cogs = float(''.join(map(str, cogs)))
    total_cogs = babel.numbers.format_currency(
        decimal.Decimal(cogs), cash_label, locale='en_US')

    fix_sum = (''.join(map(str, fix_sum)))
    if fix_sum == str(None):
        fix_sum = 0.0
    else:
        fix_sum = float(''.join(map(str, fix_sum)))

    var_sum = (''.join(map(str, var_sum)))
    if var_sum == str(None):
        var_sum = 0.0
    else:
        var_sum = float(''.join(map(str, var_sum)))

    l = str(fix_sum + var_sum)
    total_expenses = babel.numbers.format_currency(
        decimal.Decimal(l), cash_label, locale='en_US')
    print("fixedexpenses", total_expenses)

    expenses = QtWidgets.QTreeWidgetItem(
        self.ui.treeWidget, ['Cost of Goods Sold'])
    fix_expenses = QtWidgets.QTreeWidgetItem(
        self.ui.treeWidget, ['Fixed Expenses'])
    orp_expenses = QtWidgets.QTreeWidgetItem(
        self.ui.treeWidget, ['Variable Expenses'])
    # revenue = QtWidgets.QTreeWidgetItem(self.ui.treeWidget, ['revenue'])
    for index, tuple in enumerate(alltb):
        li = list(map(str, tuple))
        print(li)
        ci = QtWidgets.QTreeWidgetItem(fix_expenses, li)
        # cv =
    for index, tuple in enumerate(var_expe):
        li1 = list(map(str, tuple))
        print(li1)
        ci1 = QtWidgets.QTreeWidgetItem(orp_expenses, li1)
        # cv =
    var_sum1 = babel.numbers.format_currency(
        decimal.Decimal(var_sum), cash_label, locale='en_US')
    fix_sum1 = babel.numbers.format_currency(
        decimal.Decimal(fix_sum), cash_label, locale='en_US')
    QtWidgets.QTreeWidgetItem(
        expenses, [
            'Cost of Goods Sold', ' ', total_cogs])
    QtWidgets.QTreeWidgetItem(
        fix_expenses, [
            'Total Fixed expenses', ' ', fix_sum1])
    QtWidgets.QTreeWidgetItem(
        orp_expenses, [
            'Total variable expenses', ' ', var_sum1])
    QtWidgets.QTreeWidgetItem(
        orp_expenses, [
            'Total expenses', ' ', total_expenses])
    net_pr(self)
    # except Exception:
    #print("error profit loss account")


def revenuet(self):
    self.connection = sqlite3.connect(pathtodb + "\\yobi\\yobi_database.db")
    self.c = self.connection.cursor()
    qdate = self.ui.dateEdit_4.date()
    order_date = qdate.toPython()

    qdate = self.ui.dateEdit_5.date()
    order_date2 = qdate.toPython()
    alltb = self.c.execute(
        "SELECT name, KSH FROM transactions WHERE transactionsdate BETWEEN ? AND ? AND coa_id=? AND tx_type=?",
        (order_date,
         order_date2, "revenue", "credit")).fetchall()
    self.c.execute(
        "INSERT INTO report_printing SELECT name, KSH FROM transactions WHERE transactionsdate BETWEEN ? AND ? AND coa_id=? AND tx_type=?",
        (order_date,
         order_date2, "revenue", "credit"))
    self.connection.commit()
    total_income = self.c.execute(
        "SELECT SUM(KSH) FROM transactions WHERE transactionsdate BETWEEN ? AND ? AND coa_id=? AND tx_type=?",
        (order_date,
         order_date2,
         "revenue", "credit")).fetchone()
    total_income = (''.join(map(str, total_income)))

    revenue = QtWidgets.QTreeWidgetItem(self.ui.treeWidget, ['revenue'])
    for index, tuple in enumerate(alltb):
        liv = list(map(str, tuple))
        # ci = QtWidgets.QTreeWidgetItem(expenses, li)
        cv = QtWidgets.QTreeWidgetItem(revenue, liv)
    total_income1 = babel.numbers.format_currency(
        decimal.Decimal(total_income), cash_label, locale='en_US')
    QtWidgets.QTreeWidgetItem(revenue, ['Total income', ' ', total_income1])


def sales(self):
    self.connection = sqlite3.connect(pathtodb + "\\yobi\\yobi_database.db")
    self.c = self.connection.cursor()
    qdate = self.ui.dateEdit_4.date()
    sale_date = qdate.toPython()

    qdate = self.ui.dateEdit_5.date()
    sale_date2 = qdate.toPython()
    sales_rev = self.c.execute(
        "SELECT SUM(KSH) FROM transactions WHERE transactionsdate BETWEEN ? AND ? AND name=? AND tx_type=?",
        (sale_date,
         sale_date2, "Product Sales", "credit")).fetchone()
    sales_rev = (''.join(map(str, sales_rev)))
    self.c.execute('INSERT INTO report_printing VALUES (?,?)', ('Sales', ' '))
    self.connection.commit()

    if sales_rev == str(None):
        sales_rev = 0
    else:
        sales_rev = float(''.join(map(str, sales_rev)))

    total_revenue = str(sales_rev)

    sale = QtWidgets.QTreeWidgetItem(self.ui.treeWidget, ['Sales'])
    total_revenue1 = babel.numbers.format_currency(
        decimal.Decimal(total_revenue), cash_label, locale='en_US')
    QtWidgets.QTreeWidgetItem(sale, ['Total Sales', ' ', total_revenue1])


def sales_returns(self):
    self.connection = sqlite3.connect(pathtodb + "\\yobi\\yobi_database.db")
    self.c = self.connection.cursor()
    qdate = self.ui.dateEdit_4.date()
    order_date = qdate.toPython()

    qdate = self.ui.dateEdit_5.date()
    order_date2 = qdate.toPython()
    alltb = self.c.execute(
        "SELECT SUM(KSH) FROM transactions WHERE transactionsdate BETWEEN ? AND ? AND name=? AND tx_type=?",
            (order_date,
            order_date2, "Sales Returns and Allowances", "credit")).fetchone()

    alltb = (''.join(map(str, alltb)))

    if alltb == str(None):
        alltb = 0
    else:
        alltb = float(''.join(map(str, alltb)))

    total_revenue = str(alltb)

    sale = QtWidgets.QTreeWidgetItem(self.ui.treeWidget, ['Sales Returns'])
    total_revenue1 = babel.numbers.format_currency(
        decimal.Decimal(total_revenue), cash_label, locale='en_US')
    QtWidgets.QTreeWidgetItem(
        sale, ['Total Sales returns', ' ', total_revenue1])


def sales_reports(self):
    self.connection = sqlite3.connect(pathtodb + "\\yobi\\yobi_database.db")
    self.c = self.connection.cursor()
    qdate = self.ui.dateEdit_16.date()
    order_date = qdate.toPython()

    qdate = self.ui.dateEdit_15.date()
    order_date2 = qdate.toPython()
    result = self.c.execute(
        "SELECT * FROM sales WHERE sale_date BETWEEN ? AND ?",
        (order_date,
         order_date2)).fetchall()
    if result == []:
        QMessageBox.warning(
            QMessageBox(),
            'Error',
            'no results found .')
    else:

        print(result)
        self.ui.tableWidget_20.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableWidget_20.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableWidget_20.setItem(
                    row_number,
                    column_number,
                    QTableWidgetItem(
                        str(data)))


def stock_reports(self):
    self.connection = sqlite3.connect(pathtodb + "\\yobi\\yobi_database.db")
    self.c = self.connection.cursor()
    qdate = self.ui.dateEdit_12.date()
    order_date = qdate.toPython()

    qdate = self.ui.dateEdit_11.date()
    order_date2 = qdate.toPython()
    result = self.c.execute(
        "SELECT UPC , name , Buying_price , selling_price , Quantity , Supplier, category, reoder , vat, stockdate FROM stock WHERE stockdate BETWEEN ? AND ?",
        (order_date,
         order_date2)).fetchall()
    if result == []:
        QMessageBox.warning(
            QMessageBox(),
            'Error',
            'no results found .')
    else:
        print(result)
        self.ui.tableWidget_19.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableWidget_19.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableWidget_19.setItem(
                    row_number,
                    column_number,
                    QTableWidgetItem(
                        str(data)))


def orrders_report(self):
    self.connection = sqlite3.connect(pathtodb + "\\yobi\\yobi_database.db")
    self.c = self.connection.cursor()
    qdate = self.ui.dateEdit_20.date()
    order_date = qdate.toPython()

    qdate = self.ui.dateEdit_19.date()
    order_date2 = qdate.toPython()
    result = self.c.execute(
        "SELECT code, client_name, grand_total, total_amount, payment_status,  order_date, due FROM orders WHERE order_date BETWEEN ? AND ?",
        (order_date,
         order_date2)).fetchall()
    if result == []:
        QMessageBox.warning(
            QMessageBox(),
            'Error',
            'no results found .')
    else:
        print(result)
        self.ui.tableWidget_22.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableWidget_22.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableWidget_22.setItem(
                    row_number,
                    column_number,
                    QTableWidgetItem(
                        str(data)))


def salereturns_report(self):
    self.connection = sqlite3.connect(pathtodb + "\\yobi\\yobi_database.db")
    self.c = self.connection.cursor()
    qdate = self.ui.dateEdit_10.date()
    order_date = qdate.toPython()

    qdate = self.ui.dateEdit_9.date()
    order_date2 = qdate.toPython()
    result = self.c.execute(
        "SELECT name, KSH, description, tx_type, transactionsdate FROM transactions WHERE transactionsdate BETWEEN ? AND ? AND name=?",
        (order_date,
         order_date2, "Sales Returns and Allowances")).fetchall()
    if result == []:
        QMessageBox.warning(
            QMessageBox(),
            'Error',
            'no results found .')
    else:
        self.ui.tableWidget_10.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableWidget_10.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableWidget_10.setItem(
                    row_number,
                    column_number,
                    QTableWidgetItem(
                        str(data)))


def general_report(self):
    self.connection = sqlite3.connect(pathtodb + "\\yobi\\yobi_database.db")
    self.c = self.connection.cursor()
    qdate = self.ui.dateEdit_18.date()
    order_date = qdate.toPython()

    qdate = self.ui.dateEdit_17.date()
    order_date2 = qdate.toPython()
    result = self.c.execute(
        "SELECT name, KSH, transactionsdate FROM transactions WHERE transactionsdate BETWEEN ? AND ? AND tx_type=?",
        (order_date,
         order_date2, "debit")).fetchall()
    result2 = self.c.execute(
        "SELECT name, KSH, transactionsdate FROM transactions WHERE transactionsdate BETWEEN ? AND ? AND tx_type=?",
        (order_date,
         order_date2, "credit")).fetchall()
    if result == []:
        QMessageBox.warning(
            QMessageBox(),
            'Error',
            'no results found .')
    else:

        cr = self.c.execute(
            "SELECT SUM(KSH) FROM transactions WHERE transactionsdate BETWEEN ? AND ? AND tx_type=?",
            (order_date,
            order_date2, "credit")).fetchone()
        cr = (''.join(map(str, cr)))
        if cr == str(None):
            cr = 0
        else:
            cr = float(''.join(map(str, cr)))
        dr = self.c.execute(
            "SELECT SUM(KSH) FROM transactions WHERE transactionsdate BETWEEN ? AND ? AND tx_type=?",
            (order_date,
            order_date2, "debit")).fetchone()
        dr = (''.join(map(str, dr)))
        if dr == str(None):
            dr = 0
        else:
            dr = float(''.join(map(str, dr)))
        dr1 = babel.numbers.format_currency(
            decimal.Decimal(dr), cash_label, locale='en_US')
        cr1 = babel.numbers.format_currency(
            decimal.Decimal(cr), cash_label, locale='en_US')
        self.ui.label_230.setText(str(cr1))
        self.ui.label_230.setFont(QFont("Times", 14))
        self.ui.label_228.setText(str(dr1))
        self.ui.label_228.setFont(QFont("Times", 14))
        if dr == cr:
            self.ui.label_231.setText("Balanced")
        else:
            self.ui.label_231.setText(" not balanced")

        
        self.ui.tableWidget_21.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableWidget_21.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableWidget_21.setItem(
                    row_number,
                    column_number,
                    QTableWidgetItem(
                        str(data)))
        
        self.ui.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result2):
            self.ui.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableWidget.setItem(
                    row_number,
                    column_number,
                    QTableWidgetItem(
                        str(data)))


def gross_pr(self):
    self.connection = sqlite3.connect(pathtodb + "\\yobi\\yobi_database.db")
    self.c = self.connection.cursor()
    qdate = self.ui.dateEdit_4.date()
    order_date = qdate.toPython()

    qdate = self.ui.dateEdit_5.date()
    order_date2 = qdate.toPython()
    alltb = self.c.execute(
        "SELECT SUM(KSH) FROM transactions WHERE transactionsdate BETWEEN ? AND ? AND coa_id=? AND tx_type=?",
        (order_date,
         order_date2, "Sales Returns and Allowances", "credit")).fetchone()

    sales_rev = self.c.execute(
        "SELECT SUM(KSH) FROM transactions WHERE transactionsdate BETWEEN ? AND ? AND name=? AND tx_type=?",
        (order_date,
         order_date2, "Product Sales", "credit")).fetchone()
    sales_rev = (''.join(map(str, sales_rev)))
    cogs = self.c.execute(
        "SELECT SUM(KSH) FROM transactions WHERE transactionsdate BETWEEN ? AND ? AND name=? AND tx_type=?",
        (order_date,
         order_date2, "cost of goods sold", "debit")).fetchone()
    cogs = (''.join(map(str, cogs)))

    alltb = (''.join(map(str, alltb)))
    if alltb == str(None):
        alltb = 0.00
    else:
        alltb = round(float(''.join(map(str, alltb))), 2)

    if sales_rev == str(None):
        sales_rev = 0.00
    else:
        sales_rev = round(float(''.join(map(str, sales_rev))), 2)
    if cogs == str(None):
        cogs = 0.00
    else:
        cogs = round(float(''.join(map(str, cogs))), 2)
    print(f"sales revenue>>{sales_rev} cost of goods>>{cogs} sales returns>>{alltb}")

    gross_profit = round((sales_rev - cogs - alltb), 2)
    print(f"gross profit ->>>>>>>>>>>>>>>>{gross_profit}")
    gross = QtWidgets.QTreeWidgetItem(self.ui.treeWidget, ['Gross Profit'])
    total_income7 = babel.numbers.format_currency(
        decimal.Decimal(gross_profit), cash_label, locale='en_US')
    QtWidgets.QTreeWidgetItem(gross, ['Gross profit', ' ', total_income7])
    return gross_profit


def net_pr(self):
    try:
        self.connection = sqlite3.connect(
            pathtodb + "\\yobi\\yobi_database.db")
        self.c = self.connection.cursor()
        qdate = self.ui.dateEdit_4.date()
        order_date = qdate.toPython()

        qdate = self.ui.dateEdit_5.date()
        order_date2 = qdate.toPython()
        alltb = self.c.execute(
            "SELECT SUM(KSH) FROM transactions WHERE transactionsdate BETWEEN ? AND ? AND coa_id=? AND tx_type=?",
            (order_date,
            order_date2, "Sales Returns and Allowances", "credit")).fetchone()


        total_income = self.c.execute(
            "SELECT SUM(KSH) FROM transactions WHERE transactionsdate BETWEEN ? AND ? AND coa_id=? AND tx_type=?",
            (order_date,
             order_date2, "revenue", "credit")).fetchone()
        total_income = float(''.join(map(str, total_income)))


        fix_sum = self.c.execute(
            "SELECT SUM(KSH) FROM transactions WHERE transactionsdate BETWEEN ? AND ? AND coa_id=? AND coa_id=? AND tx_type=?",
            (order_date,
             order_date2, "fixedexpenses", "expenses", "debit")).fetchone()

        fix_sum = (''.join(map(str, fix_sum)))
        if fix_sum == str(None):
            fix_sum = 0.0
        else:
            fix_sum = float(''.join(map(str, fix_sum)))

        alltb = (''.join(map(str, alltb)))

        if alltb == str(None):
            alltb = 0.0
        else:
            alltb = float(''.join(map(str, alltb)))
        net_profit = round((total_income + fix_sum) - alltb, 2)
        gross = QtWidgets.QTreeWidgetItem(self.ui.treeWidget, ['Net Profit'])
        total_income71 = babel.numbers.format_currency(
            decimal.Decimal(net_profit), cash_label, locale='en_US')
        QtWidgets.QTreeWidgetItem(gross, ['Net profit', ' ', total_income71])
        return net_profit
    except Exception:
        traceback.print_exc()
