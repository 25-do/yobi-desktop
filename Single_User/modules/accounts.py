from PySide6 import QtWidgets
from PySide6.QtWidgets import QTableWidgetItem
from main import *
import pandas as pd
import os
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
        "SELECT SUM(KSH) FROM transactions WHERE transactionsdate BETWEEN ? AND ? AND coa_id=?",
        (order_date,
         order_date2,
         "fixedexpenses"
         )).fetchone()

    var_sum = self.c.execute(
        "SELECT SUM(KSH) FROM transactions WHERE transactionsdate BETWEEN ? AND ? AND coa_id=?",
        (order_date,
         order_date2,
         "expenses"
         )).fetchone()
    self.c.execute(
        "INSERT INTO report_printing SELECT name, KSH FROM transactions WHERE transactionsdate BETWEEN ? AND ? AND coa_id=?",
        (order_date,
         order_date2,
         "fixedexpenses"
         ))
    self.connection.commit()
    self.c.execute(
        "INSERT INTO report_printing SELECT name, KSH FROM transactions WHERE transactionsdate BETWEEN ? AND ?",
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
        "SELECT name, amount FROM income WHERE income_date BETWEEN ? AND ?",
        (order_date,
         order_date2)).fetchall()
    self.c.execute(
        "INSERT INTO report_printing SELECT name, amount FROM income WHERE income_date BETWEEN ? AND ?",
        (order_date,
         order_date2))
    self.connection.commit()
    total_income = self.c.execute(
        "SELECT SUM(amount) FROM income WHERE income_date BETWEEN ? AND ?",
        (order_date,
         order_date2)).fetchone()
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
    alltb = self.c.execute(
        "SELECT SUM(paid) FROM payment WHERE payment_date BETWEEN ? AND ?",
        (order_date,
         order_date2)).fetchone()
    revenue_from_transactions = self.c.execute(
        "SELECT SUM(KSH) FROM transactions WHERE transactionsdate BETWEEN ? AND ?",
        (sale_date,
         sale_date2)).fetchone()
    self.c.execute('INSERT INTO report_printing VALUES (?,?)', ('Sales', ' '))
    self.connection.commit()
    print(type((alltb)))
    total_sales = self.c.execute(
        "SELECT SUM(paid_amount) FROM orders WHERE order_date BETWEEN ? AND ?",
        (sale_date,
         sale_date2)).fetchone()
    total_sales = float(''.join(map(str, total_sales)))
    alltb = (''.join(map(str, alltb)))

    if alltb == str(None):
        alltb = 0
    else:
        alltb = float(''.join(map(str, alltb)))

    total_revenue = str(total_sales + alltb)

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
        "SELECT SUM(total_amount) FROM sales_returns WHERE return_date BETWEEN ? AND ?",
        (order_date,
         order_date2)).fetchone()

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
        "SELECT * FROM sales_returns WHERE return_date BETWEEN ? AND ?",
        (order_date,
         order_date2)).fetchall()

    print(result)
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
        "SELECT * FROM transactions WHERE transactionsdate BETWEEN ? AND ?",
        (order_date,
         order_date2)).fetchall()
    cr = self.c.execute(
        "SELECT SUM(credit) FROM transactions WHERE transactionsdate BETWEEN ? AND ?",
        (order_date,
         order_date2)).fetchone()
    cr = float(''.join(map(str, cr)))
    dr = self.c.execute(
        "SELECT SUM(debit) FROM transactions WHERE transactionsdate BETWEEN ? AND ?",
        (order_date,
         order_date2)).fetchone()
    dr = float(''.join(map(str, dr)))
    dr1 = babel.numbers.format_currency(
        decimal.Decimal(dr), cash_label, locale='en_US')
    cr1 = babel.numbers.format_currency(
        decimal.Decimal(cr), cash_label, locale='en_US')
    self.ui.label_230.setText(str(cr1))
    self.ui.label_228.setText(str(dr1))
    if dr == cr:
        self.ui.label_231.setText("Balanced")
    else:
        self.ui.label_231.setText(" not balanced")

    print(result)
    self.ui.tableWidget_21.setRowCount(0)
    for row_number, row_data in enumerate(result):
        self.ui.tableWidget_21.insertRow(row_number)
        for column_number, data in enumerate(row_data):
            self.ui.tableWidget_21.setItem(
                row_number,
                column_number,
                QTableWidgetItem(
                    str(data)))


def export_table_sales(self):
    self.connection = sqlite3.connect(pathtodb + "\\yobi\\yobi_database.db")
    self.c = self.connection.cursor()
    self.c.execute("DELETE FROM sales_report")
    qdate = self.ui.dateEdit_16.date()
    order_date = qdate.toPython()

    qdate = self.ui.dateEdit_15.date()
    order_date2 = qdate.toPython()
    self.c.execute(
        "INSERT INTO sales_report SELECT * FROM sales WHERE sale_date BETWEEN ? AND ?",
        (order_date,
         order_date2)).fetchall()
    df = pd.read_sql_query("SELECT * FROM sales_report", self.connection)
    df.to_html("data.html")
    with open("data.html") as file:
        file = file.read()
    file = file.replace("<table ", "<table class='rwd-table'")
    with open("data.html", "w") as file_to_write:
        file_to_write.write(html + file)
    os.startfile("data.html")


def export_table_orders(self):
    self.connection = sqlite3.connect(pathtodb + "\\yobi\\yobi_database.db")
    self.c = self.connection.cursor()
    self.c.execute("DELETE FROM sales_report")
    qdate = self.ui.dateEdit_20.date()
    order_date = qdate.toPython()

    qdate = self.ui.dateEdit_19.date()
    order_date2 = qdate.toPython()
    data = self.c.execute(
        "SELECT code, discount,  paid_amount, client_name, grand_total, total_amount, payment_status,  order_date, due, order_date FROM orders WHERE order_date BETWEEN ? AND ?",
        (order_date,
         order_date2)).fetchall()
    df = pd.DataFrame(
        data=data,
        columns=[
            'code',
            'discount',
            'paid_amount',
            'client_name',
            'grand_total',
            'total_amount',
            'payment_status',
            'order_date',
            'due',
            'order_date'])

    df.to_csv(os.path.join(pathtodb, r'DataBD_Data.csv'))


def export_table_stock(self):
    self.connection = sqlite3.connect(pathtodb + "\\yobi\\yobi_database.db")
    self.c = self.connection.cursor()
    self.c.execute("DELETE FROM stock_report")
    qdate = self.ui.dateEdit_12.date()
    order_date = qdate.toPython()

    qdate = self.ui.dateEdit_11.date()
    order_date2 = qdate.toPython()

    self.c.execute(
        "INSERT INTO stock_report SELECT UPC , name , Buying_price , selling_price , Quantity , Supplier, category, reoder , vat, stockdate FROM stock WHERE stockdate BETWEEN ? AND ?",
        (order_date,
         order_date2)).fetchall()
    df = pd.read_sql_query("SELECT * FROM stock_report", self.connection)
    df.to_html("data.html")
    with open("data.html") as file:
        file = file.read()
    file = file.replace("<table ", "<table class='rwd-table'")
    with open("data.html", "w") as file_to_write:
        file_to_write.write(html + file)
    os.startfile("data.html")


def export_table_sales_return(self):
    self.connection = sqlite3.connect(pathtodb + "\\yobi\\yobi_database.db")
    self.c = self.connection.cursor()
    self.c.execute("DELETE FROM sales_returns_report")
    qdate = self.ui.dateEdit_10.date()
    order_date = qdate.toPython()
    qdate = self.ui.dateEdit_9.date()
    order_date2 = qdate.toPython()
    self.c.execute(
        "INSERT INTO sales_returns_report SELECT * FROM sales_returns WHERE return_date BETWEEN ? AND ?",
        (order_date,
         order_date2)).fetchall()
    df = pd.read_sql_query(
        "SELECT * FROM sales_returns_report",
        self.connection)
    df.to_html("data.html")
    with open("data.html") as file:
        file = file.read()
    file = file.replace("<table ", "<table class='rwd-table'")
    with open("data.html", "w") as file_to_write:
        file_to_write.write(html + file)
    os.startfile("data.html")


def export_table_general_ledger(self):
    self.connection = sqlite3.connect(pathtodb + "\\yobi\\yobi_database.db")
    self.c = self.connection.cursor()
    self.c.execute("DELETE FROM sales_report")
    qdate = self.ui.dateEdit_18.date()
    order_date = qdate.toPython()
    qdate = self.ui.dateEdit_17.date()
    order_date2 = qdate.toPython()
    self.c.execute(
        "INSERT INTO sales_report SELECT * FROM transactions WHERE transactionsdate BETWEEN ? AND ?",
        (order_date,
         order_date2)).fetchall()
    df = pd.read_sql_query("SELECT * FROM sales_report", self.connection)
    df.to_html("data.html")
    with open("data.html") as file:
        file = file.read()
    file = file.replace("<table ", "<table class='rwd-table'")
    with open("data.html", "w") as file_to_write:
        file_to_write.write(html + file)
    os.startfile("data.html")


def gross_pr(self):
    self.connection = sqlite3.connect(pathtodb + "\\yobi\\yobi_database.db")
    self.c = self.connection.cursor()
    qdate = self.ui.dateEdit_4.date()
    order_date = qdate.toPython()

    qdate = self.ui.dateEdit_5.date()
    order_date2 = qdate.toPython()
    alltb = self.c.execute(
        "SELECT SUM(total_amount) FROM sales_returns WHERE return_date BETWEEN ? AND ?",
        (order_date,
         order_date2)).fetchone()

    paid = self.c.execute(
        "SELECT SUM(paid) FROM payment WHERE payment_date BETWEEN ? AND ?",
        (order_date,
         order_date2)).fetchone()

    total_income = self.c.execute(
        "SELECT SUM(amount) FROM income WHERE income_date BETWEEN ? AND ?",
        (order_date,
         order_date2)).fetchone()
    total_income = float(''.join(map(str, total_income)))

    total_sales = self.c.execute(
        "SELECT SUM(paid_amount) FROM orders WHERE order_date BETWEEN ? AND ?",
        (order_date,
         order_date2)).fetchone()
    total_sales = float(''.join(map(str, total_sales)))
    paid = (''.join(map(str, paid)))

    alltb = (''.join(map(str, alltb)))
    if alltb == str(None):
        alltb = 0
    else:
        alltb = float(''.join(map(str, alltb)))

    if paid == str(None):
        paid = 0
    else:
        paid = float(''.join(map(str, paid)))

    gross_profit = ((total_income + total_sales + paid) - alltb)
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
            "SELECT SUM(total_amount) FROM sales_returns WHERE return_date BETWEEN ? AND ?",
            (order_date,
             order_date2)).fetchone()

        paid = self.c.execute(
            "SELECT SUM(paid) FROM payment WHERE payment_date BETWEEN ? AND ?",
            (order_date,
             order_date2)).fetchone()

        total_income = self.c.execute(
            "SELECT SUM(amount) FROM income WHERE income_date BETWEEN ? AND ?",
            (order_date,
             order_date2)).fetchone()
        total_income = float(''.join(map(str, total_income)))

        total_sales = self.c.execute(
            "SELECT SUM(paid_amount) FROM orders WHERE order_date BETWEEN ? AND ?",
            (order_date,
             order_date2)).fetchone()
        total_sales = float(''.join(map(str, total_sales)))
        fix_sum = self.c.execute(
            "SELECT SUM(KSH) FROM fix_expe WHERE fixdate BETWEEN ? AND ?",
            (order_date,
             order_date2)).fetchone()

        var_sum = self.c.execute(
            "SELECT SUM(KSH) FROM var_expe WHERE vardate BETWEEN ? AND ?",
            (order_date,
             order_date2)).fetchone()
        paid = (''.join(map(str, paid)))
        fix_sum = (''.join(map(str, fix_sum)))
        var_sum = (''.join(map(str, var_sum)))
        if var_sum == str(None):
            var_sum = 0.0
        else:
            var_sum = float(''.join(map(str, var_sum)))
        if fix_sum == str(None):
            fix_sum = 0.0
        else:
            fix_sum = float(''.join(map(str, fix_sum)))
        l = int(fix_sum + var_sum)

        alltb = (''.join(map(str, alltb)))

        if alltb == str(None):
            alltb = 0.0
        else:
            alltb = float(''.join(map(str, alltb)))

        if paid == str(None):
            paid = 0.0
        else:
            paid = float(''.join(map(str, paid)))

        net_profit = ((total_income + total_sales + paid + l) - alltb)
        gross = QtWidgets.QTreeWidgetItem(self.ui.treeWidget, ['Net Profit'])
        total_income71 = babel.numbers.format_currency(
            decimal.Decimal(net_profit), cash_label, locale='en_US')
        QtWidgets.QTreeWidgetItem(gross, ['Net profit', ' ', total_income71])
        return net_profit
    except Exception:
        print("net profit error")
