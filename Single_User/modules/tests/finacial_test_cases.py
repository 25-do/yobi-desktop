import unittest

from financila_statement import Finacial

class TestingFinacilal(unittest.TestCase):
    fin = Finacial()
    def test_0_working_capital(self):
        working_capital = self.fin.working_capital()
        self.assertEqual(working_capital, 200000)
        print(f">>>>>>Working Capital Passed")
    
    def test_1_capital_employed(self):
        capital_employed = self.fin.capital_employed()
        self.assertEqual(capital_employed, 1200000.00)
        print(f">>>>>>Capital EMPLOYEDPassed")

    def test_2_current_ratio(self):
        current_ratio = self.fin.current_ratio()
        self.assertEqual(current_ratio, 3.5)
        print(f">>>>>> current_ratio Passed")

    def test_3_debt_ratio(self):
        debt_ratio = self.fin.debt_ratio()
        self.assertEqual(debt_ratio, 0.3)
        print(f">>>>>> current_ratio Passed")

    def test_4_gross_profit(self):
        gross_profit = self.fin.gross_profit()
        self.assertEqual(gross_profit, 50000.00)
        print(f">>>>>> gross_profit Passed")

    def test_5_net_profit(self):
        net_profit = self.fin.net_profit()
        self.assertEqual(net_profit, 42000.00)
        print(f">>>>>> net_profit Passed")
if __name__ == '__main__':
    unittest.main()