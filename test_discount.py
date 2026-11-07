import unittest
from discount import calculate_discount


class TestDiscount(unittest.TestCase):

    def test_discount_20_percent(self):
        self.assertEqual(calculate_discount(100, 20), 80)

    def test_discount_zero_percent(self):
        self.assertEqual(calculate_discount(100, 0), 100)

    def test_discount_100_percent(self):
        self.assertEqual(calculate_discount(100, 100), 0)

    def test_invalid_discount(self):
        with self.assertRaises(ValueError):
            calculate_discount(100, 150)


if __name__ == "__main__":
    unittest.main()