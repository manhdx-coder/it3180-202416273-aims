import unittest

from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class TestCartSort(unittest.TestCase):

    def setUp(self):
        self.cart = Cart()

        self.dvd1 = DigitalVideoDisc("Titanic", cost=20.0)
        self.dvd2 = DigitalVideoDisc("Avatar", cost=30.0)
        self.dvd3 = DigitalVideoDisc("Batman", cost=10.0)

        self.cart.add_dvd(self.dvd1)
        self.cart.add_dvd(self.dvd2)
        self.cart.add_dvd(self.dvd3)

    def test_sort_by_title(self):
        self.cart.sort_by_title()

        titles = [dvd.title for dvd in self.cart.items]

        self.assertEqual(
            titles,
            ["Avatar", "Batman", "Titanic"]
        )

    def test_sort_by_cost(self):
        self.cart.sort_by_cost()

        costs = [dvd.cost for dvd in self.cart.items]

        self.assertEqual(
            costs,
            [10.0, 20.0, 30.0]
        )


if __name__ == "__main__":
    unittest.main()