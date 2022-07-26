from main import *


def combo_orders(self):
    self.ui.comboBox_2.addItems(["code", "client_name", "payment type", "payment status"])


def searchstock(self):
    self.ui.comboBox_2.addItems(["code", "client_name", "payment type", "payment status"])
    category = self.ui.lineEdit_9.text()
    self.connection = sqlite3.connect("database.db")

    if self.ui.comboBox_2.itemText(self.ui.comboBox_2.currentIndex()) == "code":

        result = self.connection.execute("SELECT * FROM orders WHERE code=?", (category,))

    elif self.ui.comboBox_2.itemText(self.ui.comboBox_2.currentIndex()) == "client_name":
        result = self.connection.execute("SELECT * FROM orders WHERE client_name=?", (category,))

    elif self.ui.comboBox_2.itemText(self.ui.comboBox_2.currentIndex()) == "payment type":
        result = self.connection.execute("SELECT * FROM orders WHERE payment_type=?", (category,))

    elif self.ui.comboBox_2.itemText(self.ui.comboBox_2.currentIndex()) == "payment status":
        result = self.connection.execute("SELECT * FROM orders WHERE payment_status=?", (category,))

    self.ui.tableWidget_6.setRowCount(0)
    for row_number, row_data in enumerate(result):
        self.ui.tableWidget_6.insertRow(row_number)
        for column_number, data in enumerate(row_data):
            self.ui.tableWidget_6.setItem(row_number, column_number, QTableWidgetItem(str(data)))
