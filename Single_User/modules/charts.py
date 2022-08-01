from main import *
from PySide6.QtCharts import QChart
import datetime
from PySide6 import QtCharts
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtCore import Qt
from PySide6.QtGui import (QPainter, QPen)
import os

basepath = os.path.expanduser('~/Documents')
pathtodb = str(basepath)
newpath = (pathtodb + "\\yobi")
if not os.path.exists(newpath):
    os.makedirs(newpath)


def create_bar(self):
    self.connection = sqlite3.connect(pathtodb + "\\yobi\\yobi_database.db")
    self.c = self.connection.cursor()

    month_list_2 = [
        '01',
        '02',
        '03',
        '04',
        '05',
        '06',
        '07',
        '08',
        '09',
        '10',
        '11',
        '12']

    date_y = datetime.date.today()
    year_td = date_y.strftime("%Y")

    empty = []
    empty2 = []

    for month_list in month_list_2:
        all_due_orders = self.c.execute(
            "SELECT SUM(due) FROM orders WHERE strftime('%Y', order_date)=? AND strftime('%m', order_date)=?",
            (str(year_td),
             month_list)).fetchone()
        all_due_orders = (''.join(map(str, all_due_orders)))
        if all_due_orders == str(None):
            all_due_orders = 0.0
        else:
            all_due_orders = float(''.join(map(str, all_due_orders)))

        total_paid = self.c.execute(
            "SELECT SUM(paid) FROM payment WHERE strftime('%Y', payment_date)=? AND strftime('%m', payment_date)=?",
            (str(year_td),
             month_list)).fetchone()
        total_paid = (''.join(map(str, total_paid)))
        if total_paid == str(None):
            total_paid = 0.0
        else:
            total_paid = float(''.join(map(str, total_paid)))

        amount_paid = self.c.execute(
            "SELECT SUM(paid_amount) FROM orders WHERE strftime('%Y', order_date)=? AND strftime('%m', order_date)=?",
            (str(year_td),
             month_list)).fetchone()
        amount_paid = (''.join(map(str, amount_paid)))

        if amount_paid == str(None):
            amount_paid = 0.0
        else:
            amount_paid = float(''.join(map(str, amount_paid)))

        td = float(amount_paid + total_paid)
        empty2.append(all_due_orders)
        empty.append(td)

    # The QBarSet class represents a set of bars in the bar chart.
    # It groups several bars into a bar set

    set0 = QtCharts.QBarSet("Amount Paid")
    set1 = QtCharts.QBarSet("Amount due")

    set0 << empty[0] << empty[1] << empty[2] << empty[3] << empty[4] << empty[
        5] << empty[6] << empty[7] << empty[8] << empty[9] << empty[10] << empty[11]
    set1 << empty2[0] << empty2[1] << empty2[2] << empty2[3] << empty2[4] << empty2[
        5] << empty2[6] << empty2[7] << empty2[8] << empty2[9] << empty2[10] << empty2[11]

    # load data to chart
    series = QtCharts.QBarSeries()
    series.append(set0)
    series.append(set1)
    # initialize chart
    chart = QChart()
    chart.addSeries(series)
    #chart.setBackgroundBrush(QtGui.QColor(34, 34, 34, 34))
    chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)

    categories = [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "july",
        " Agu",
        "Sept",
        "Oct",
        "Nov",
        "Dec"]
    axis = QtCharts.QBarCategoryAxis()
    axis.append(categories)
    axisY = QtCharts.QValueAxis()
    chart.addAxis(axisY, QtCore.Qt.AlignLeft)
    series.attachAxis(axisY)
    b = max(empty)
    m = max(empty2)
    ra = (b + m)
    axisY.setRange(0, ra)
    chart.setAxisX(axis, series)

    chart.legend().setVisible(True)
    chart.legend().setAlignment(Qt.AlignBottom)

    self.place = QtWidgets.QVBoxLayout(self)
    self.place = QtWidgets.QVBoxLayout(self.ui.widget_6)
    self.place.setContentsMargins(0, 0, 0, 0)
    self.chartview = QtCharts.QChartView(chart)
    self.chartview.setRenderHint(QPainter.Antialiasing)
    self.chartview.setContentsMargins(0, 0, 0, 0)
    self.place.addWidget(self.chartview)


def pie(self):
    self.connection = sqlite3.connect(pathtodb + "\\yobi\\yobi_database.db")
    self.c = self.connection.cursor()

    date_y = datetime.date.today()
    year_td = date_y.strftime("%Y")

    all_due_orders = self.c.execute(
        "SELECT SUM(due) FROM orders WHERE strftime('%Y', order_date)=?",
        (str(year_td),
         )).fetchone()
    all_due_orders = (''.join(map(str, all_due_orders)))
    if all_due_orders == str(None):
        all_due_orders = 0.0
    else:
        all_due_orders = float(''.join(map(str, all_due_orders)))

    total_paid = self.c.execute(
        "SELECT SUM(paid) FROM payment WHERE strftime('%Y', payment_date)=?",
        (str(year_td),
         )).fetchone()
    total_paid = (''.join(map(str, total_paid)))
    if total_paid == str(None):
        total_paid = 0.0
    else:
        total_paid = float(''.join(map(str, total_paid)))

    amount_paid = self.c.execute(
        "SELECT SUM(paid_amount) FROM orders WHERE strftime('%Y', order_date)=?",
        (str(year_td),
         )).fetchone()
    amount_paid = (''.join(map(str, amount_paid)))

    if amount_paid == str(None):
        amount_paid = 0.0
    else:
        amount_paid = float(''.join(map(str, amount_paid)))

    td = float(amount_paid + total_paid)
    pieseries = QtCharts.QPieSeries()  # Define PieSeries
    pieseries.append("Amount Paid", td)  # insert the first element
    pieseries.append("Amount due", all_due_orders)

    # Get a slice of an element of the pie chart, which is the first one
    slic = pieseries.slices()[0]
    slic.setExploded()  # is set to exploded
    slic.setLabelVisible()
    slic.setPen(QPen(Qt.black, 1))  # Set the brush type
    slic.setBrush(Qt.red)
    slic.label()

    # Get a slice of an element of the pie chart, which is the first one
    slic2 = pieseries.slices()[1]
    slic2.setExploded()

    # is set to exploded
    slic2.setLabelVisible()
    slic2.setPen(QPen(Qt.black, 1))  # Set the brush type
    slic2.setBrush(Qt.yellow)
    # Set brush
    chart = QtCharts.QChart()  # Define QChart
    chart.addSeries(pieseries)  # Add pieseries to the chart

    chart.legend().setAcceptHoverEvents(True)
    chart.legend().setAlignment(Qt.AlignRight)

    # Set the title of the char
    # sets the legend of char to hidden
    #chart.setBackgroundBrush(QtGui.QColor(34, 34, 34, 34))

    keep = QtWidgets.QVBoxLayout(self.ui.widget_7)

    chaw = QtCharts.QChartView(chart, self)
    chaw.setGeometry(0, 0, self.width(), self.height())
    chaw.setRenderHint(QPainter.Antialiasing)
    keep.addWidget(chaw)
    chaw.show()


def pie2(self):
    self.connection = sqlite3.connect(pathtodb + "\\yobi\\yobi_database.db")
    self.c = self.connection.cursor()

    date_y = datetime.date.today()
    year_td = date_y.strftime("%Y")
    income = self.c.execute(
        "SELECT SUM(KSH) FROM transactions WHERE strftime('%Y', transactionsdate)=? AND coa_id=?",
        (str(year_td), "revenue"
         )).fetchone()
    income = (''.join(map(str, income)))
    if income == str(None):
        income = 0.0
    else:
        income = float(''.join(map(str, income)))

    var_expe = self.c.execute(
        "SELECT SUM(KSH) FROM transactions WHERE strftime('%Y', transactionsdate)=? AND coa_id=? AND coa_id=?",
        (str(year_td), "fixedexpenses", "expenses")).fetchone()
    var_expe = (''.join(map(str, var_expe)))
    if var_expe == str(None):
        var_expe = 0.0
    else:
        var_expe = float(''.join(map(str, var_expe)))

    td = float(income)
    expe = float(var_expe)

    pieseries = QtCharts.QPieSeries()  # Define PieSeries
    pieseries.append("Total Revenue", td)  # insert the first element
    pieseries.append("Total Expenses", expe)

    # Get a slice of an element of the pie chart, which is the first one
    slic = pieseries.slices()[0]
    slic.setExploded()  # is set to exploded
    slic.setLabelVisible()
    slic.setPen(QPen(Qt.black, 1))  # Set the brush type
    slic.setBrush(Qt.red)
    slic.label()

    # Get a slice of an element of the pie chart, which is the first one
    slic2 = pieseries.slices()[1]
    slic2.setExploded()

    # is set to exploded
    slic2.setLabelVisible()
    slic2.setPen(QPen(Qt.black, 1))  # Set the brush type
    slic2.setBrush(Qt.yellow)
    # Set brush
    chart = QtCharts.QChart()  # Define QChart
    chart.addSeries(pieseries)  # Add pieseries to the chart

    chart.legend().setAcceptHoverEvents(True)
    chart.legend().setAlignment(Qt.AlignRight)

    # Set the title of the char
    # sets the legend of char to hidden
    #chart.setBackgroundBrush(QtGui.QColor(34, 34, 34, 34))

    keep = QtWidgets.QVBoxLayout(self.ui.widget_9)

    chaw = QtCharts.QChartView(chart, self)
    chaw.setGeometry(0, 0, self.width(), self.height())
    chaw.setRenderHint(QPainter.Antialiasing)
    keep.addWidget(chaw)
    chaw.show()


def create_bar2(self):
    self.connection = sqlite3.connect(pathtodb + "\\yobi\\yobi_database.db")
    self.c = self.connection.cursor()

    month_list_2 = [
        '01',
        '02',
        '03',
        '04',
        '05',
        '06',
        '07',
        '08',
        '09',
        '10',
        '11',
        '12']

    date_y = datetime.date.today()
    year_td = date_y.strftime("%Y")

    empty = []
    empty2 = []

    for month_list in month_list_2:
        income = self.c.execute(
            "SELECT SUM(KSH) FROM transactions WHERE strftime('%Y', transactionsdate)=? AND strftime('%m', transactionsdate)=? AND coa_id=?",
            (str(year_td),
             month_list, 'revenue')).fetchone()
        income = (''.join(map(str, income)))
        if income == str(None):
            income = 0.0
        else:
            income = float(''.join(map(str, income)))

        var_expe = self.c.execute(
            "SELECT SUM(KSH) FROM transactions WHERE strftime('%Y', transactionsdate)=? AND strftime('%m', transactionsdate)=? AND coa_id=?",
            (str(year_td),
             month_list, "expenses")).fetchone()
        var_expe = (''.join(map(str, var_expe)))
        if var_expe == str(None):
            var_expe = 0.0
        else:
            var_expe = float(''.join(map(str, var_expe)))

        fix_expe = self.c.execute(
            "SELECT SUM(KSH) FROM transactions WHERE strftime('%Y', transactionsdate)=? AND strftime('%m', transactionsdate)=? AND coa_id=?",
            (str(year_td),
             month_list, "fixedexpenses")).fetchone()
        fix_expe = (''.join(map(str, fix_expe)))
        if fix_expe == str(None):
            fix_expe = 0.0
        else:
            fix_expe = float(''.join(map(str, fix_expe)))

        td = float(income)
        expe = float(fix_expe + var_expe)
        empty2.append(expe)
        empty.append(td)

    # The QBarSet class represents a set of bars in the bar chart.
    # It groups several bars into a bar set

    set0 = QtCharts.QBarSet("Total Revenue")
    set1 = QtCharts.QBarSet("Total Expense")

    set0 << empty[0] << empty[1] << empty[2] << empty[3] << empty[4] << empty[
        5] << empty[6] << empty[7] << empty[8] << empty[9] << empty[10] << empty[11]
    set1 << empty2[0] << empty2[1] << empty2[2] << empty2[3] << empty2[4] << empty2[
        5] << empty2[6] << empty2[7] << empty2[8] << empty2[9] << empty2[10] << empty2[11]

    # load data to chart
    series = QtCharts.QBarSeries()
    series.append(set0)
    series.append(set1)
    # initialize chart
    chart = QChart()
    chart.addSeries(series)
    #chart.setBackgroundBrush(QtGui.QColor(34, 34, 34, 34))
    chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)

    categories = [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "july",
        " Agu",
        "Sept",
        "Oct",
        "Nov",
        "Dec"]
    axis = QtCharts.QBarCategoryAxis()
    axis.append(categories)
    axisY = QtCharts.QValueAxis()
    chart.addAxis(axisY, QtCore.Qt.AlignLeft)
    series.attachAxis(axisY)
    b = max(empty)
    m = max(empty2)
    ra = (b + m)
    axisY.setRange(0, ra)
    chart.setAxisX(axis, series)

    chart.legend().setVisible(True)
    chart.legend().setAlignment(Qt.AlignBottom)

    self.place = QtWidgets.QVBoxLayout(self)
    self.place = QtWidgets.QVBoxLayout(self.ui.widget_8)
    self.place.setContentsMargins(0, 0, 0, 0)
    self.chartview = QtCharts.QChartView(chart)
    self.chartview.setRenderHint(QPainter.Antialiasing)
    self.chartview.setContentsMargins(0, 0, 0, 0)
    self.place.addWidget(self.chartview)
