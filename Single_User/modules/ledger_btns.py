import os
import sqlite3
from PySide6.QtWidgets import QMessageBox
basepath = os.path.expanduser('~/Documents')
pathtodb = str(basepath)
newpath = (pathtodb + "\\yobi")
if not os.path.exists(newpath):
    os.makedirs(newpath)

class LEDGERBUTTONS:
    def lock_bill_invoice_ledger(tablename, message : str, error_message : str, status : str) -> None:
        """function that bills a ledger at the bills update page
        checks if the bill is posted if true it raises an exception if false it post it to the ledger
        """
        database_connection = sqlite3.connect(
                pathtodb + "\\yobi\\yobi_database.db")
        cusr = database_connection.cursor()
        row = tablename.currentRow()
        currentcode = (tablename.item(row, 0).text())
        currentcode = (''.join(map(str, currentcode)))

        
        ledger_locked = cusr.execute("SELECT locked FROM ledgers WHERE name=?", (currentcode,)).fetchone() # get all ledgers name
        ledger_locked = (''.join(map(str, ledger_locked))) # convert data into list
        # check if ledger_name is in the ledger table to avoid duplicates of bills in ledgers
        if ledger_locked == status:
            QMessageBox.warning(
                QMessageBox(), 'Error', error_message)
        else:
            combo2 = status # post the ledger by default
            cusr.execute("UPDATE ledgers SET locked=? WHERE name=? ", (combo2, currentcode)).fetchone()
            database_connection.commit()
            QMessageBox.information(QMessageBox(),'Successfull', message)
            
    def bill_ledger_journal_entries(tablename, message : str, error_message : str, status : str) -> None:
        """function that bills a ledger at the bills update page
        checks if the bill is posted if true it raises an exception if false it post it to the ledger
        """
        database_connection = sqlite3.connect(
                pathtodb + "\\yobi\\yobi_database.db")
        cusr = database_connection.cursor()
        row = tablename.currentRow()
        currentcode = (tablename.item(row, 0).text())
        currentcode = (''.join(map(str, currentcode)))

        
        ledger_locked = cusr.execute("SELECT active FROM ledgers WHERE name=?", (currentcode,)).fetchone() # get all ledgers name
        ledger_locked = (''.join(map(str, ledger_locked))) # convert data into list
        # check if ledger_name is in the ledger table to avoid duplicates of bills in ledgers
        if ledger_locked == status:
            QMessageBox.warning(
                QMessageBox(), 'Error', error_message)
        else:
            combo2 = status # post the ledger by default
            cusr.execute("UPDATE ledgers SET active=? WHERE name=? ", (combo2, currentcode)).fetchone()
            database_connection.commit()
            QMessageBox.information(QMessageBox(),'Successfull', message)
