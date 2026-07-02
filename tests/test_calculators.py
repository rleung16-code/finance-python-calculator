import unittest
from calculators import (
    compound_interest,
    monthly_loan_payment,
    return_on_investment,
    monthly_savings_required,
)


class TestCalculators(unittest.TestCase):
    def test_compound_interest(self):
        result = compound_interest(1000, 0.05, 1, 12)
        self.assertAlmostEqual(result, 1051.16, places=2)

    def test_monthly_loan_payment(self):
        result = monthly_loan_payment(10000, 0.06, 3)
        self.assertAlmostEqual(result, 304.22, places=2)

    def test_return_on_investment(self):
        result = return_on_investment(1000, 1200)
        self.assertAlmostEqual(result, 0.20, places=2)

    def test_monthly_savings_required(self):
        result = monthly_savings_required(12000, 3000, 12)
        self.assertAlmostEqual(result, 750.00, places=2)


if __name__ == "__main__":
    unittest.main()
