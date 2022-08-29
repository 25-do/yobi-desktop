
from datetime import date
import random
import sqlite3
import string
import uuid
from datetime import datetime as dt


class POS:
    def __init__(self) -> None:
        self.point_OS = {}
        self.poslist = []
    def posappend(self, itemid):
        """
        it appends the item UPC to the list so  it can be used to remove an itame from
        pos table
        """
        self.poslist.append(itemid)
        print(itemid)
    def pointofsale_addto_postable(self, itemid:str, quantity:float, quantity2:int):
        if itemid == "":
            print('Error', 'no items to be invoiced')
        else:
            database_connection = sqlite3.connect("test.db")
            cusr = database_connection.cursor()
            upc_pos = cusr.execute("SELECT UPC FROM pos_table").fetchall()
            sale_no = int(str(self.ui.lineEdit_33.text()))
            upc_list = [item for t in upc_pos for item in t]
            out_of_stock = cusr.execute(
                    "SELECT Quantity FROM stock WHERE UPC=? ", (itemid,)).fetchone()
            out_of_stock = int(''.join(map(str, out_of_stock)))
            if out_of_stock < 0:
                print(f'The item is out of stock.')
            else:
                if itemid in upc_list:
                    print('item already exists.')
                else:
                    # try:
                    # item id from stock
                    # items quantity in stock table at quantity column
                    quantity = float(str(self.ui.lineEdit_7.text()))
                    quantity2 = int(str(self.ui.lineEdit_7.text()))
                    self.posappend(itemid)
                    var_y = cusr.execute(
                        "SELECT (Quantity - ?) FROM stock WHERE UPC=? ", (quantity, itemid)).fetchone()
                    var_j = cusr.execute(
                        "SELECT category FROM stock WHERE UPC=? ", (itemid,)).fetchone()
                    buying_price = cusr.execute(
                        "SELECT Buying_price FROM stock WHERE UPC=? ", (itemid,)).fetchone()
                    disc = cusr.execute(
                        "SELECT Discount FROM stock WHERE UPC=? ", (itemid,)).fetchone()
                    var_x = cusr.execute(
                        "SELECT name FROM stock WHERE UPC=? ",
                        (itemid,
                            )).fetchone()  # querys the name of item being sold
                    b = cusr.execute(
                        "SELECT (selling_price *?) FROM stock WHERE UPC=? ",
                        (quantity,
                            itemid)).fetchone()
                    b2 = cusr.execute(
                        "SELECT selling_price FROM stock WHERE UPC=? ", (itemid,)).fetchone()
                    var_f = cusr.execute(
                        "SELECT vat FROM stock WHERE UPC=?", (itemid,)).fetchone()
                    var_f = (''.join(map(str, var_f)))
                    try:
                        var_q = cusr.execute(
                            "SELECT tax_percentage FROM tax_table WHERE tax_name=?", (var_f,)).fetchone()
                        var_q = float(''.join(map(str, var_q)))
                    except Exception:
                        print(
                            'Error',
                            'Tax not set navigate to the stock page then press the tax button .')
                    var_y = float(''.join(map(str, var_y)))
                    # removes the brackets from the name queryed
                    var_x = (''.join(map(str, var_x)))
                    var_j = (''.join(map(str, var_j)))
                    buying_price = float(''.join(map(str, buying_price)))
                    disc = (''.join(map(str, disc)))
                    b = float(''.join(map(str, b)))
                    b2 = (''.join(map(str, b2)))
                    tp = b
                    # totalvat = cusr.execute(
                    #     "SELECT (? / (?+100)*100)*(?/100)FROM stock WHERE UPC=?",
                    #     (b,
                    #      var_q,
                    #      var_q,
                    #      itemid)).fetchone()
                    # totalvat = float(''.join(map(str, totalvat)))
                    totalvat = ((var_q / 100 * b))
                    sale_date = date.today()
                    self.pos = cusr.execute(
                        "INSERT INTO pos_table(sale_no, UPC, name, discount, category, Quantity, KSH, KSH2, VAT, totalvat, taxcode, buying_price, sale_date) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
                        (sale_no,
                            itemid,
                            var_x,
                            disc,
                            var_j,
                            quantity,
                            b,
                            b2,
                            var_q,
                            totalvat,
                            var_f,
                            buying_price,
                            sale_date))
                    cusr.execute(
                        "INSERT INTO most_sold(UPC, name, KSH) VALUES (?,?,?)", (itemid, var_x, tp))
                    self.point_OS[itemid] = quantity2
                    # var_t = cusr.execute(
                    #     "UPDATE stock SET Quantity=? WHERE UPC=? ", (var_y, itemid)).fetchone()
                    self.kshposappend(b)
                    self.itemposappend(itemid)
                    database_connection.commit()
                    cusr.close()
                    database_connection.close()
                    # except Exception:
                    #     QMessageBox.warning(
                    #         QMessageBox(),
                    #         'Error',
                    #         'enter valid details make sure TAX are set in tax setting ')

    def pos_details(self):
        self.ui.pushButton_20.clicked.connect(self.point_of_sale_function)


    def point_of_sale_function(self):
        try:
            database_connection = sqlite3.connect("test.db")
            cusr = database_connection.cursor()
            self.totalksh = cusr.execute(
                "SELECT SUM(KSH) FROM pos_table").fetchone()
            self.totalqua = cusr.execute(
                "SELECT SUM(Quantity) FROM pos_table").fetchone()
            self.totalksh = float(''.join(map(str, self.totalksh)))
            self.totalqua = float(''.join(map(str, self.totalqua)))
            for item in self.poslist:
                posupc = cusr.execute(
                    "SELECT KSH FROM pos_table WHERE UPC=?", (item,)).fetchone()
                posupc = float(''.join(map(str, posupc)))
                print("this is the item UPC", item)
                self.g = cusr.execute(
                    "UPDATE stock SET sold=(sold + ?) WHERE UPC=? ", (posupc, item)).fetchone()
            database_connection.commit()
            self.most_sold_table()
            self.add_invoice()
        except Exception:
            print('Error', 'please enter valid details')
    def add_invoice(self) -> float:
            self.connection = sqlite3.connect("test.db")
            self.c = self.connection.cursor()
            self.posksh = self.c.execute("SELECT SUM(KSH) FROM pos_table").fetchone()
            self.posksh = float(''.join(map(str, self.posksh)))
            self.totalksh = float(str(self.ui.lineEdit_8.text()))
            
            discount = self.c.execute("SELECT SUM(discount) FROM pos_table").fetchone()
            discount = float(''.join(map(str, discount)))
            buying_price = self.c.execute("SELECT SUM(buying_price) FROM pos_table").fetchone()
            buying_price = float(''.join(map(str, buying_price)))

            client_name = str(self.ui.lineEdit_14.text())
            self.total = self.c.execute("SELECT SUM(totalvat) FROM pos_table").fetchone()
            self.total = float(''.join(map(str, self.total)))
            print(f"........./...POS............../")
            print(f"TOTAL DISCOUNT ---> {discount}")
            # pos.pos(self)
            print(f"dict{self.point_OS}")
            for key, value in self.point_OS.items():
                print(f"value ->{value}")
                print(f"key ->{key}")
                key2 = str(key)
                value2 = int(value)
                self.c.execute("UPDATE stock SET Quantity=(Quantity-?) WHERE UPC=? ", (value2, key2))
                self.connection.commit()
            

            total_amount = (self.total + self.posksh)

            discount2 = (discount / 100 * total_amount)
            # discount3 = (discount / 100 * self.posksh)
            grand_total = round(total_amount - discount2, 2)
            print(f"DISCOUNT ON product ---> {discount2}")
            print(f"Grand TOTAL AFTER DEDUCTION OF DISCOUNT ---> {grand_total}")
            # total_no_tax = (self.posksh - discount3)
            amount_paid = round(float(str(self.ui.lineEdit_8.text())), 2)
            due = round(grand_total - amount_paid, 2)
            print(f"DUE AMOUNT ---> {due}")
            # due2 = round(total_no_tax - amount_paid, 2)
            if due < 0:
                print(
                    'Error',
                    'Due error, Due amount cant be less than 0')
            else:
                return grand_total
            