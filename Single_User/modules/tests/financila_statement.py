import sqlite3

class Finacial:
    def net_profit(self) -> float:
        """_calculates the net profit_

        Returns:
            _float_: _net profit_
        """
        try:
            if self.total_revenue() > self.total_expenses():
                n_p = self.total_revenue() - self.total_expenses()
                return n_p
            else:
                n_p = self.total_revenue() - self.total_expenses()
                return n_p
        except Exception:
            print("print net profit error")

    def total_revenue(self):
        try:
            database_connection = sqlite3.connect("test.db")
            cusr = database_connection.cursor()
            total_rev = cusr.execute("SELECT SUM(KSH) FROM transactions WHERE coa_id=? AND tx_type=?", ("revenue", "credit")).fetchone()
            total_rev = (''.join(map(str, total_rev)))
            if total_rev == str(None):
                total_rev = 0.00
            else:
                total_rev = round(float(''.join(map(str, total_rev))), 2)
            return total_rev
        except BaseException:
            print("total sales error")
    
    def sum_cogs_exp(self):
        """calculates total variable expenses

        Returns:
            _float_: _sum variable expense_
        """
        database_connection = sqlite3.connect("test.db")
        cusr = database_connection.cursor()
        coa_account = "expenses"
        var_x = cusr.execute("SELECT SUM(KSH) FROM transactions WHERE coa_id=? AND tx_type=? AND name=?", (coa_account, "debit", "cost of goods sold")).fetchone()
        var_x = (''.join(map(str, var_x)))
        if var_x == str(None):
            var_x = 0.00
        else:
            var_x = round(float(''.join(map(str, var_x))), 2)
        return var_x

    def gross_profit(self):
        try:
            if self.total_sales() > self.sum_cogs_exp():
                g_p = round(self.total_sales() - self.sum_cogs_exp(), 2)
                return g_p
            else:
                g_p = round(self.total_sales() - self.sum_cogs_exp(), 2)
                return g_p
        except BaseException:
            print("gross profit error")

    def total_sales(self):
        try:
            database_connection = sqlite3.connect(
                "test.db")
            cusr = database_connection.cursor()
            total_paid = cusr.execute(
            "SELECT SUM(KSH) FROM transactions WHERE name=? AND tx_type=?",
            ("Product Sales", "credit")).fetchone()
            total_paid = (''.join(map(str, total_paid)))
            if total_paid == str(None):
                total_paid = 0.00
            else:
                total_paid = round(float(''.join(map(str, total_paid))), 2)
            return total_paid
        except BaseException:
            print("total sales error")

    def total_expenses(self):
        try:
            self.z = round(self.sum_fix_exp() + self.sum_var_exp(), 2)
            return self.z
        except Exception:
            # self.ui.label_113.setText("fixed expense or variable expense is empty ")
            print('total expense.')

    def total_liability(self):
        """calculates total liabilities
        Returns:
            _float_: _short term liabilities + long term liabilities_
        """
        try:
            self.z = round(self.sum_short_term() + self.sum_long_term(), 2)
            return self.z
        except Exception:
            print("total liabilities error")

    def total_asset(self):
        """calculates total assets

        Returns:
            _float_: _sum of fixed and current asset_
        """
        try:
            self.z = round(self.sumCurrent_asset() + self.sumfixed_asset(), 2)
            return self.z
        except Exception:
            print("total assets error")

    def sum_var_exp(self):
        """calculates total variable expenses

        Returns:
            _float_: _sum variable expense_
        """
        database_connection = sqlite3.connect(
            "test.db")
        cusr = database_connection.cursor()
        coa_account = "expenses"
        var_x = cusr.execute("SELECT SUM(KSH) FROM transactions WHERE coa_id=? AND tx_type=?", (coa_account, "debit")).fetchone()
        var_x = (''.join(map(str, var_x)))
        if var_x == str(None):
            var_x = 0.00
        else:
            var_x = round(float(''.join(map(str, var_x))), 2)
        return var_x

    def sum_fix_exp(self):
        """calculates sum of fixed expense

        Returns:
            _float_: _total fixed expenses_
        """
        try:
            database_connection = sqlite3.connect("test.db")
            cusr = database_connection.cursor()
            coa_account = "fixedexpenses"
            var_x = cusr.execute("SELECT SUM(KSH) FROM transactions WHERE coa_id=? AND tx_type=?", (coa_account, "debit")).fetchone()
            var_x = (''.join(map(str, var_x)))
            if var_x == str(None):
                var_x = 0.00
            else:
                var_x = round(float(''.join(map(str, var_x))), 2)
            return var_x
        except Exception:
            print("sum fix expe error")

    def sum_long_term(self):
        """calculates sum of long term liabilities

        Returns:
            _float_: _total longterm liabilities_
        """
        try:
            database_connection = sqlite3.connect(
                "test.db")
            cusr = database_connection.cursor()
            coa_account = "Longtermliabilities"
            var_x = cusr.execute("SELECT SUM(KSH) FROM transactions WHERE coa_id=? AND tx_type=?", (coa_account, "credit")).fetchone()
            var_x = (''.join(map(str, var_x)))
            if var_x == str(None):
                var_x = 0.00
            else:
                var_x = round(float(''.join(map(str, var_x))), 2)
            return var_x
        except Exception:
            print("sum long term  error")

    def sum_short_term(self):
        """calculates sum shortterm liabilitiy

        Returns:
            _float_: _total shortterm liabilitiy_
        """
        try:
            database_connection = sqlite3.connect(
                "test.db")
            cusr = database_connection.cursor()
            coa_account = "currentliabilities"
            var_x = cusr.execute(
                "SELECT SUM(KSH) FROM transactions WHERE coa_id=? AND tx_type=?", (coa_account, "credit")).fetchone()
            var_x = (''.join(map(str, var_x)))
            if var_x == str(None):
                var_x = 0.00
            else:
                var_x = round(float(''.join(map(str, var_x))), 2)
            return var_x
        except Exception:
            print("sum short lib error")

    def sumCurrent_asset(self):
        """calculates sum current asset

        Returns:
            _float_: _total current asset_
        """
        try:
            database_connection = sqlite3.connect(
                "test.db")
            cusr = database_connection.cursor()
            coa_account = "currentassets"
            var_x = cusr.execute("SELECT SUM(KSH) FROM transactions WHERE coa_id=? AND tx_type=?", (coa_account, "debit")).fetchone()
            var_x = (''.join(map(str, var_x)))
            if var_x == str(None):
                var_x = 0.00
            else:
                var_x = round(float(''.join(map(str, var_x))), 2)
            return var_x
        except Exception:
            print("sum current asset error")

    def sumfixed_asset(self):
        """calculates sum fixed asset

        Returns:
            _float_: _total fixed asset_
        """
        try:
            database_connection = sqlite3.connect("test.db")
            cusr = database_connection.cursor()
            coa_account = "fixedassets"
            var_x = cusr.execute("SELECT SUM(KSH) FROM transactions WHERE coa_id=? AND tx_type=?", (coa_account, "debit")).fetchone()
            var_x = (''.join(map(str, var_x)))
            if var_x == str(None):
                var_x = 0.00
            else:
                var_x = round(float(''.join(map(str, var_x))), 2)
            return var_x
        except Exception:
            print("sum fixed asset")

    def Margin(self):
        try:
            d_r = (self.gross_profit() / self.total_sales()) * 100
        except Exception:
            print('Error', 'gross profit or total sales is empty.')
    # MARGIN FUNCTION

    def debt_percentage(self):
        try:
            d_r = (self.total_liability() / self.total_asset()) * 100
            
        except Exception:
            print("debt percentage error")

    def Netprofit_Margin(self):
        try:
            d_r = (self.net_profit() / self.total_sales()) * 100
            d_r = round(d_r, 2)
        except Exception:
            print('Error', 'Could not add expense to the database.')

    def working_capital(self):
        try:
            w_r = round(self.sumCurrent_asset() - self.sum_short_term(), 2)
            return w_r
        except Exception:
            print("working capital error")

    def capital_employed(self):
        try:
            c_e = round(self.sumfixed_asset() + self.working_capital(), 2)
            return c_e
        except Exception:
            print("capital employed error")

    def debt_ratio(self):
        try:
            d_r = round(self.total_liability() / self.total_asset(), 1)
            return d_r
        except Exception:
            print('Error', 'liability table or assets is empty.')

    def current_ratio(self):
        try:
            c_r = round(self.sumCurrent_asset() / self.sum_short_term(), 1)
            return c_r
        except Exception:
            print("error, sumCurrent_asset and sum_short_term")


if __name__ == '__main__':
    Finacial = Finacial()