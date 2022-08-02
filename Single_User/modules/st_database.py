import sqlite3
import os
from main import *
basepath = os.path.expanduser('~/Documents')
pathtodb = str(basepath)
newpath = (pathtodb + "\yobi")
if not os.path.exists(newpath):
    os.makedirs(newpath)
def stats_database(self):
    database_connection = sqlite3.connect(
                pathtodb + "\\yobi\\yobi_database.db")
    cusr = database_connection.cursor()
    cusr.execute("CREATE TABLE IF NOT EXISTS current_Asset(id_2 INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, KSH INTEGER, description TEXT, debit INTEGER, credit INTEGER, currAssetDate TIMESTAMP)")
    cusr.execute("CREATE TABLE IF NOT EXISTS fixed_Asset(id_8 INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, KSH INTEGER, description TEXT, debit INTEGER, credit INTEGER, fixAssetDate TIMESTAMP)")
    cusr.execute("CREATE TABLE IF NOT EXISTS short_term_lib(id_7 INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, KSH INTEGER, description TEXT, debit INTEGER, credit INTEGER, stlibdate TIMESTAMP)")
    cusr.execute("CREATE TABLE IF NOT EXISTS long_term_lib(id_6 INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, KSH INTEGER, description TEXT, debit INTEGER, credit INTEGER, ltlibdate TIMESTAMP)")
    cusr.execute("CREATE TABLE IF NOT EXISTS var_expe(id_5 INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, KSH INTEGER, description TEXT, debit INTEGER, credit INTEGER, vardate TIMESTAMP)")
    cusr.execute("CREATE TABLE IF NOT EXISTS fix_expe(id_1 INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, KSH INTEGER, description TEXT, debit INTEGER, credit INTEGER,fixdate TIMESTAMP)")
    # cusr.execute("CREATE TABLE IF NOT EXISTS sales(id_4 INTEGER PRIMARY KEY, name TEXT, KSH INTEGER, description TEXT, debit INTEGER, credit INTEGER,saledate TIMESTAMP)")
    cusr.execute("CREATE TABLE IF NOT EXISTS transactions(uuid TEXT, updated TIMESTAMP, created TIMESTAMP, coa_id TEXT, id_4 INTEGER PRIMARY KEY, journal_entry_id TEXT, ledger_id TEXT, name TEXT, KSH INTEGER, description TEXT, tx_type TEXT, transactionsdate TIMESTAMP, user_uuid TEXT)")
    cusr.execute("CREATE TABLE IF NOT EXISTS journal_entries(id TEXT, ledger_id TEXT, activity TEXT, description TEXT, posted TEXT, locked TEXT, journal_entrydate TIMESTAMP, user_uuid TEXT)")
    cusr.execute("CREATE TABLE IF NOT EXISTS ledgers(id TEXT, lg_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, locked TEXT, active TEXT, ledger_date TIMESTAMP, user_uuid TEXT)")

    cusr.execute("CREATE TABLE IF NOT EXISTS account_payable(id_17 INTEGER PRIMARY KEY, name TEXT, KSH INTEGER, description TEXT, debit INTEGER, credit INTEGER, ledgerdate TIMESTAMP, user_uuid TEXT)")
    cusr.execute("CREATE TABLE IF NOT EXISTS stock(UPC TEXT NOT NULL, name TEXT, Buying_price INTEGER NOT NULL, selling_price INTEGER NOT NULL, Quantity INTEGER NOT NULL, Supplier TEXT, category TEXT, reoder INTEGER, uom TEXT, Discount TEXT, vat INTEGER NOT NULL, stockdate TIMESTAMP, sold INTEGER, user_uuid TEXT)")
    cusr.execute("CREATE TABLE IF NOT EXISTS stock_report(UPC TEXT, name TEXT, Buying_price INTEGER, selling_price INTEGER, Quantity INTEGER, Supplier TEXT, category TEXT, reoder INTEGER, vat INTEGER, stockdate TIMESTAMP, user_uuid TEXT)")


    cusr.execute("CREATE TABLE IF NOT EXISTS most_sold(UPC TEXT , name TEXT, KSH TEXT)")
    cusr.execute("CREATE TABLE IF NOT EXISTS sales_count(count INTEGER)")
    cusr.execute("CREATE TABLE IF NOT EXISTS pos_table(sale_no INTEGER, UPC TEXT, name TEXT, discount INTEGER, category TEXT, Quantity INTEGER, KSH INTEGER, KSH2 INTEGER, VAT INTEGER, totalvat INTEGER, taxcode TEXT, buying_price INTEGER, sale_date TIMESTAMP)")
    cusr.execute("CREATE TABLE IF NOT EXISTS sales(sale_no INTEGER, UPC TEXT, name TEXT, category TEXT, Quantity INTEGER, KSH INTEGER, VAT INTEGER, totalvat INTEGER, taxcode TEXT, sale_date TIMESTAMP)")
    cusr.execute("CREATE TABLE IF NOT EXISTS sales_report(sale_no INTEGER, UPC TEXT, name TEXT, category TEXT, Quantity INTEGER, KSH INTEGER, VAT INTEGER, totalvat INTEGER, taxcode TEXT, sale_date TIMESTAMP)")

    cusr.execute("CREATE TABLE IF NOT EXISTS recipt(name TEXT, Quantity TEXT, KSH INTEGER)")
    cusr.execute("CREATE TABLE IF NOT EXISTS recip_detail(id_17 INTEGER PRIMARY KEY, business_name TEXT NOT NULL, pobox TEXT, contact TEXT, email TEXT, street_address TEXT, notes TEXT, footer TEXT, currency TEXT, profile_photo BLOB)")
    cusr.execute("CREATE TABLE IF NOT EXISTS tax_table(tax_name TEXT, tax_percentage INTEGER, tax_agent TEXT)")
    cusr.execute("CREATE TABLE IF NOT EXISTS clients(id_10 INTEGER PRIMARY KEY,  name TEXT, telno TEXT , address TEXT, email TEXT, date TIMESTAMP, balance INTEGER)")
    cusr.execute("CREATE TABLE IF NOT EXISTS orders(uuid TEXT, created TIMESTAMP, sale_no TEXT, updated TIMESTAMP, terms TEXT, id_13 INTEGER PRIMARY KEY AUTOINCREMENT, item_code TEXT NOT NULL, discount INTEGER,  paid_amount INTEGER NOT NULL, code TEXT, client_name TEXT NOT NULL, grand_total INTEGER, total_amount INTEGER, sub_total INTEGER, payment_type Text, payment_status Text,  order_date TIMESTAMP, due INTEGER, invoice_status TEXT, markdown_notes TEXT, ledger_uuid TEXT, user_uuid TEXT)")

    cusr.execute("CREATE TABLE IF NOT EXISTS payment(code TEXT,  client_name TEXT, payment_date TIMESTAMP , paid INTEGER, due INTEGER)")
    cusr.execute("CREATE TABLE IF NOT EXISTS chart_of_accounts(code TEXT, role TEXT, account TEXT, balance_type TEXT, locked INTEGER, active INTEGER)")
    cusr.execute("CREATE TABLE IF NOT EXISTS currency(currency TEXT)")
    cusr.execute("CREATE TABLE IF NOT EXISTS debt_payment(code TEXT,  supplier_name TEXT, payment_date TIMESTAMP , paid INTEGER, due INTEGER)")
    cusr.execute("CREATE TABLE IF NOT EXISTS income(name TEXT,  amount INTEGER, debit INTEGER, credit INTEGER, description TEXT , income_date TIMESTAMP)")
    cusr.execute("CREATE TABLE IF NOT EXISTS sales_returns(order_code TEXT NOT NULL,  item_name TEXT NOT NULL, description TEXT, quantity INTEGER NOT NULL, total_amount INTEGER , return_date TIMESTAMP)")
    cusr.execute("CREATE TABLE IF NOT EXISTS sales_returns_report(order_code TEXT,  item_name TEXT, description TEXT, quantity INTEGER, total_amount INTEGER , return_date TIMESTAMP)")
    cusr.execute("CREATE TABLE IF NOT EXISTS Purchase(purchase_code TEXT NOT NULL,  supplier TEXT NOT NULL, item TEXT NOT NULL, quantity INTEGER NOT NULL, total_amount INTEGER NOT NULL, transport INTEGER NOT NULL, owes INTEGER NOT NULL, date TIMESTAMP, user_uuid TEXT)")
    cusr.execute("CREATE TABLE IF NOT EXISTS supplier(created TIMESTAMP, updated TIMESTAMP, id_14 INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL,  tel1 TEXT NOT NULL, tel2 TEXT, addr1 TEXT NOT NULL, addr2 TEXT, email Text NOT NULL, site TEXT, country TEXT, date TIMESTAMP, user_uuid TEXT)")
    cusr.execute("CREATE TABLE IF NOT EXISTS report_printing(name TEXT, amount INTEGER)")
    cusr.execute("CREATE TABLE IF NOT EXISTS purchaseorder(uuid TEXT, created TIMESTAMP, updated TIMESTAMP, notes TEXT, po_number TEXT, po_date TIMESTAMP, po_title TEXT, po_amount_recived INTEGER, fulfilled TEXT, fulfillment_date TIMESTAMP, po_status TEXT, user_uuid TEXT)")
    cusr.execute("CREATE TABLE IF NOT EXISTS bill(uuid TEXT, created TIMESTAMP, updated TIMESTAMP, terms TEXT, amount_due INTEGER, amount_paid INTEGER, amount_recivable INTEGER, amount_unerned INTEGER, amount_earned INTEGER, paid INTEGER, paid_date TIMESTAMP, date TIMESTAMP, due_date TIMESTAMP, xref TEXT, accrue TEXT, bill_number TEXT, cash_account_id TEXT, ledger_id TEXT, prepaid_account_id TEXT, unearned_account_id TEXT, ispurchase_order TEXT, purchase_order_uuid TEXT, vendor_id TEXT, bill_status TEXT, markdown_notes TEXT, user_uuid TEXT)")
    cusr.execute("CREATE TABLE IF NOT EXISTS items_tb(uuid TEXT, created TIMESTAMP, updated TIMESTAMP, po_item_status TEXT, quantity INTEGER, unit_cost INTEGER, total_amount INTEGER, bill_model_id TEXT, invoice_model_id TEXT, item_model_id TEXT, po_model_id TEXT, po_quantity INTEGER, po_total_amount INTEGER, po_unit_cost INTEGER, user_uuid TEXT)")
    cusr.execute("CREATE TABLE IF NOT EXISTS bill_item(created TIMESTAMP, updated TIMESTAMP, uuid TEXT, bill_uuid TEXT, name TEXT, amount INTEGER, user_uuid TEXT)")
    cusr.execute("CREATE TABLE IF NOT EXISTS purchase_order_items(created TIMESTAMP, updated TIMESTAMP, uuid TEXT, bill_uuid TEXT, purchase_order_uuid TEXT, name TEXT, cogs INTEGER, quantity INTEGER, amount INTEGER, user_uuid TEXT)")
    cusr.execute("CREATE TABLE IF NOT EXISTS employee(created TIMESTAMP, updated TIMESTAMP, uuid TEXT, emp_code TEXT, first_name TEXT, last_name TEXT, mobile TEXT, email TEXT, address TEXT, gender TEXT, emmp_postion TEXT, department TEXT, joined TIMESTAMP, bank TEXT, salary INTEGER, user_uuid TEXT)")
    cusr.execute("CREATE TABLE IF NOT EXISTS admin(email TEXT, salt TEXT, hash TEXT, token TEXT, logged_in TEXT, password_set TEXT, user_uuid TEXT)")
    cusr.execute("CREATE TABLE IF NOT EXISTS department(created TIMESTAMP, updated TIMESTAMP, dep_name TEXT, id_dep INTEGER PRIMARY KEY AUTOINCREMENT, dep_code TEXT, dep_level TEXT, dep_description TEXT, dep_supirior TEXT, status TEXT, user_uuid TEXT)")
    cusr.execute("CREATE TABLE IF NOT EXISTS positions(created TIMESTAMP, updated TIMESTAMP, pos_name TEXT, id_dep INTEGER PRIMARY KEY AUTOINCREMENT, pos_code TEXT, pos_level TEXT, pos_description TEXT, pos_depertment TEXT, status TEXT, user_uuid TEXT)")
    cusr.execute("CREATE TABLE IF NOT EXISTS user_managment(created TIMESTAMP, updated TIMESTAMP, employee_name TEXT, username TEXT, password TEXT, role TEXT, salt TEXT, assign TEXT, status TEXT, user_uuid TEXT)")
    cusr.execute("CREATE TABLE IF NOT EXISTS uom(uom_id INTEGER PRIMARY KEY AUTOINCREMENT,created TIMESTAMP, updated TIMESTAMP, uom_uuid TEXT, unit_abbr TEXT, name TEXT, is_active TEXT, user_uuid TEXT)")
    cusr.close()