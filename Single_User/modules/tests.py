import os
from decimal import Decimal as D
import sqlite3
from main import *
import names
import random
from random import randint, choices
import datetime
basepath = os.path.expanduser('~/Documents')
pathtodb = str(basepath)
newpath = (pathtodb + "\yobi")
if not os.path.exists(newpath):
    os.makedirs(newpath)


def testing_orders(self):
    for i in range(1, 50):
        print("##########################==", i)
        self.connection = sqlite3.connect(pathtodb + "\yobi\yobi_database.db")
        self.c = self.connection.cursor()
        
        payment_type = "cash"
        payment_status = "Fully paid"

        self.posksh = float(random.randint(1000, 10000))
        self.totalksh = float(random.randint(100, 1000))

        item_code = ("GUM" + str(random.randint(0, 1000)))
        due = float(random.randint(100, 1000))
        discount = 0.0
        
        client_name = str(names.get_full_name())
        vat = 12
        
        # sub_total = self.totalksh
        total_amount = (((vat/100) * (self.posksh)) + self.posksh)
        discount2 = (discount/100 * total_amount)
        grand_total = (total_amount - discount2)
        code = ("INVOICE" + str(random.randint(0, 1000)))
        order_date = datetime.date(randint(2022,2022), randint(1,12),randint(1,28))

        credit = 0
        cash = float(random.randint(100, 1000))
        amount_paid = float(random.randint(100, 1000))
        description = ("sold goods on credit to" + " " + client_name)
        name = ("Debitor" + "," + " " + client_name + item_code)
        uuid1 = uuid.uuid4().hex
        locked= '0'
        active = '1'
        updated = dt.today()
        created = dt.today()

        
        self.c.execute("INSERT INTO orders(item_code, discount,  paid_amount, code, client_name, grand_total, total_amount, sub_total, payment_type, payment_status,  order_date, due ) "
                        "VALUES (?,?,?,?,?,?,?,?,?,?,?,?)", (item_code, discount, amount_paid, code, client_name, grand_total, total_amount, self.posksh,  payment_type, payment_status,  order_date, due))
        self.connection.commit()
        self.c.execute("INSERT INTO current_Asset(name, KSH, description, debit, credit, currAssetDate) VALUES (?,?,?,?,?,?)", (name, cash, description, 
        due, credit, order_date))
        self.connection.commit()
        self.c.execute("INSERT INTO ledgers(id, name , locked , active , ledger_date) VALUES (?,?,?,?,?)", (uuid1, name, locked, active, order_date))
        self.connection.commit()
        self.c.execute("INSERT INTO income(name,  amount, debit, credit, description, income_date) VALUES (?,?,?,?,?,?)", (name, cash, credit, due, description, order_date))
        self.connection.commit()
        

        self.c.execute("INSERT INTO sales SELECT sale_no, UPC, name, category, Quantity, KSH, VAT, totalvat, taxcode, sale_date FROM pos_table")
        self.connection.commit()
        # self.c.execute("INSERT INTO long_term_lib(name, KSH, description, debit, credit, ltlibdate) VALUES (?,?,?,?,?,?)", (name, cash, description, due, credit, order_date))
        # self.connection.commit()
        # self.c.execute("INSERT INTO short_term_lib(name, KSH, description, debit, credit, stlibdate) VALUES (?,?,?,?,?,?)", (name, cash, description, due, credit, order_date))
        # self.connection.commit()
        self.c.execute("INSERT INTO var_expe(name, KSH, description, debit, credit,vardate) VALUES (?,?,?,?,?,?)", (name, cash, description, due, credit, order_date))
        self.connection.commit()
        self.c.close()
        self.connection.close()

def accounting_test_bud(self):
    for i in range(1, 50):
        self.connection = sqlite3.connect(pathtodb + "\yobi\yobi_database.db")
        self.c = self.connection.cursor()
        code = ("INVOICE" + str(random.randint(0, 1000)))
        order_date = datetime.date(randint(2022,2022), randint(1,12),randint(1,28))
        client_name = str(names.get_full_name())
        item_code = ("GUM" + str(random.randint(0, 1000)))

        credit = 0
        cash = float(random.randint(100, 1000))
        amount_paid = float(random.randint(100, 1000))
        description = ("sold goods on credit to" + " " + client_name)
        due = float(random.randint(100, 1000))
        name = ("Debitor" + "," + " " + client_name + item_code)

        activity = choices([
            'Operating',
            'Financing',
            'Investing',
            'other'])
        activity = (''.join(map(str, activity)))
        journal_uuid = uuid.uuid4().hex
        print(journal_uuid, i)
        bill_uuid = uuid.uuid4().hex    
        ledger_uuid = uuid.uuid4().hex    
        uuid1 = uuid.uuid4().hex    
        created = dt.today()
        updated = dt.today()
        terms = choices(["Fully paid", "Installments", "Not Paid"])
        terms = (''.join(map(str, terms)))
        amount_due = float(random.randint(1000, 10000))
        amount_paid = float(random.randint(1000, 10000))
        amount_recivable = float(random.randint(1000, 10000))
        amount_unerned = float(random.randint(1000, 10000))
        amount_earned = float(random.randint(1000, 10000))
        paid = float(random.randint(1000, 10000))
        paid_date = datetime.date(randint(2022,2022), randint(1,12),randint(1,28))
        date_1 = datetime.date(randint(2022,2022), randint(1,12),randint(1,28))
        due_date = datetime.date(randint(2022,2022), randint(1,12),randint(1,28))
        xref = "testing"
        accrue = ' '
        bill_number = ('BILL-' + (''.join(random.choices(string.ascii_uppercase, k=15))))
        code = '1010'
        code2 = '1400'
        code3 = '2490'
        contact = str("+254 " + str(random.randint(1, 10)))
        ispurchase_order = '0'
        purchase_order_bill_uuid_list = ' '

        cash_account_id = self.c.execute(
        "SELECT id FROM chart_of_accounts WHERE code=? ", (code,)).fetchone()
        cash_account_id = (''.join(map(str, cash_account_id)))

        prepaid_account_id = self.c.execute(
        "SELECT id FROM chart_of_accounts WHERE code=? ", (code2,)).fetchone()
        prepaid_account_id = (''.join(map(str, prepaid_account_id)))

        unearned_account_id = self.c.execute(
        "SELECT id FROM chart_of_accounts WHERE code=? ", (code3,)).fetchone()
        unearned_account_id = (''.join(map(str, unearned_account_id)))
        vendor_id = str(names.get_full_name())
        # print("#####", vendor_id)
        email = str(vendor_id + "@gmail.com")
        addres = choices(["Nairobi, moi avenue", "Kisumu, Road", "Nakuru, Njoro Street", "Mombasa, Port"])
        addres = (''.join(map(str, addres)))
        combo1,combo2 = '0', '0'
        bill_status = choices(["Draft", "Inreview", "Approved"])
        bill_status = (''.join(map(str, bill_status)))
        markdown_notes = 'test bud notes '
        owes = 2.0
        posted, locked = "1", "0"
        self.c.execute("INSERT INTO bill(created, updated, terms, amount_due, amount_paid, amount_recivable, amount_unerned, amount_earned, paid, paid_date, date, due_date, xref, accrue, uuid, bill_number, cash_account_id, ledger_id, prepaid_account_id, unearned_account_id, ispurchase_order, purchase_order_uuid, vendor_id, bill_status, markdown_notes) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(
            created,
            updated,
            terms,
            amount_due,
            amount_paid,
            amount_recivable,
            amount_unerned,
            amount_earned,
            paid,
            paid_date,
            date_1,
            due_date,
            xref,
            accrue,
            bill_uuid,
            bill_number,
            cash_account_id,
            ledger_uuid,
            prepaid_account_id,
            unearned_account_id,
            ispurchase_order,
            purchase_order_bill_uuid_list,
            vendor_id,
            bill_status,
            markdown_notes))
        self.connection.commit()
        self.c.execute("INSERT INTO ledgers(id, name, locked, active, ledger_date) VALUES (?,?,?,?,?)",(ledger_uuid, bill_number,combo1,combo2,date_1))
        self.connection.commit()
        self.c.execute("INSERT INTO supplier(name,  addres, contact, email, owes) VALUES (?,?,?,?,?)",(vendor_id, addres, contact,email,owes))
        self.connection.commit()
        self.c.execute("INSERT INTO journal_entries(id, ledger_id, activity, description, posted, locked, journal_entrydate) VALUES (?,?,?,?,?,?,?)",(journal_uuid, ledger_uuid, activity,markdown_notes,posted,locked,date_1))
        self.connection.commit()
        self.c.execute("INSERT INTO purchase_order_items(created, updated, uuid, bill_uuid, purchase_order_uuid, name, cogs, quantity, amount) VALUES (?,?,?,?,?,?,?,?,?)", (updated, created, uuid1, bill_uuid, name, cash, credit, due, description))
        self.connection.commit()
        self.c.execute("INSERT INTO department(created, updated, dep_name, dep_code, dep_level, dep_description, dep_supirior, status) VALUES (?,?,?,?,?,?,?,?)", (updated, created, uuid1, bill_uuid, name, cash, credit, due, description))
        self.connection.commit()