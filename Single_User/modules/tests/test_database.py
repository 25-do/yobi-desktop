from datetime import date
import sqlite3
from datetime import datetime as dt
class DbInit:
    def __init__(self):
        self.delete_trans()
        self.stats_database()
        self.transactions_add()
    def stats_database(self):
        database_connection = sqlite3.connect("test.db")
        cusr = database_connection.cursor()
        cusr.execute("CREATE TABLE IF NOT EXISTS transactions(updated TIMESTAMP, created TIMESTAMP, coa_id TEXT, name TEXT, KSH INTEGER, tx_type TEXT, transactionsdate TIMESTAMP)")
        
        cusr.close()
    def delete_trans(self):
        database_connection = sqlite3.connect("test.db")
        cusr = database_connection.cursor()
        cusr.execute("DELETE from transactions")
        database_connection.commit()
        cusr.close()
        database_connection.close()
    def transactions_add(self):
        database_connection = sqlite3.connect("test.db")
        cusr = database_connection.cursor()
        updated = dt.today()
        created = dt.today()
        transactionsdate = date.today()

        rows = [(updated, created, "currentassets", "inventory", 100000, "debit", transactionsdate),
                (updated, created, "currentassets", "cash and cash equivalents", 20000, "debit", transactionsdate),
                (updated, created, "currentassets", "bank", 100000, "debit", transactionsdate),
                (updated, created, "currentliabilities", "creditors", 60000, "credit", transactionsdate),
                (updated, created, "currentliabilities", "Accrued expenses", 20000, "credit", transactionsdate),
                (updated, created, "Longtermliabilities", "loan 10 year", 200000, "credit", transactionsdate),
                (updated, created, "Longtermliabilities", "3 years icdc loan", 100000, "credit", transactionsdate),
                (updated, created, "fixedassets", "land", 500000, "debit", transactionsdate),
                (updated, created, "fixedassets", "machinery", 300000, "debit", transactionsdate),
                (updated, created, "fixedassets", "plant", 200000, "debit", transactionsdate),
                (updated, created, "currentassets", "debtors", 60000,  "debit", transactionsdate),
                (updated, created, "expenses", "cost of goods sold", 75000,  "debit", transactionsdate),
                (updated, created, "expenses", "wages", 0,  "debit", transactionsdate),
                (updated, created, "expenses", "slaries", 25000,  "debit", transactionsdate),
                (updated, created, "expenses", "bad debts", 4500,  "debit", transactionsdate),
                (updated, created, "expenses", "rent of Building", 13000,  "debit", transactionsdate),
                (updated, created, "revenue", "Product Sales", 125000,  "credit", transactionsdate)
                ]
        cusr.executemany("INSERT INTO transactions VALUES (?,?,?,?,?,?,?)", rows)
        cusr.connection.commit()
DbInit()