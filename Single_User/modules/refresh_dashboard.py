from main import *
try:
    conn = sqlite3.connect(pathtodb + "\yobi\yobi_database.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS recip_detail(id_17 INTEGER PRIMARY KEY, business_name TEXT, pobox TEXT, contact TEXT, email TEXT, street_address TEXT, notes TEXT, footer TEXT, currency TEXT, profile_photo BLOB)")
    cash_label = c.execute("SELECT currency FROM recip_detail WHERE id_17=1").fetchone()
    cash_label = (''.join(map(str, cash_label)))
    c.close()
except Exception:
    cash_label = "$"

def refreshdashboard(self):
    self.total_income()

    self.capital_employed()
    self.total_liability()
    
    self.total_expenses()
    self.total_asset()
    self.coa_load()
    self.gross_profit()
    self.net_profit()
    self.working_capital()
    self.debt_ratio()
    self.current_ratio()
    self.most_sold_table()
    #self.debt_percentage()
    #self.Netprofit_Margin()
    self.scroll()
    #self.debt_percentage()
    
    