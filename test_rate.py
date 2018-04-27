# -*- conding: utf-8 -*-

import unittest
from model.rate import Rate

rate = Rate()


class TestRate(unittest.TestCase):
    def test_percent(self):
        self.assertEqual(rate.percent(100), 70)

    def test_quantityType(self):
        self.assertEqual(rate.quantityType(1), 5)
        self.assertEqual(rate.quantityType(2), 20)
        self.assertEqual(rate.quantityType(3), 60)

    def test_calculateTotalPay(self):
        self.assertEqual(
            rate.calculateTotalPay(1, 1, 1),
            'Total to pay is 5$\n\nPress Enter to back the menu')
        self.assertEqual(
            rate.calculateTotalPay(2, 1, 1),
            'Total to pay is 20$\n\nPress Enter to back the menu')
        self.assertEqual(
            rate.calculateTotalPay(3, 1, 1),
            'Total to pay is 60$\n\nPress Enter to back the menu')
        self.assertEqual(
            rate.calculateTotalPay(1, 3, 1, True),
            'Total to pay is 10.5$\n\nPress Enter to back the menu')


if __name__ == '__main__':
    unittest.main()
