import unittest

from aims.cart import Cart
from aims.dvd import DigitalVideoDisc
from aims.search import search_by_category, search_by_title


class TestSearch(unittest.TestCase):

    def setUp(self):
        self.cart = Cart()
        self.dvd1 = DigitalVideoDisc("The Lion King", "Animation", "Roger", 87, 19.95)
        self.dvd2 = DigitalVideoDisc("Star Wars", "Science Fiction", "George", 124, 24.95)
        self.dvd3 = DigitalVideoDisc("Finding Nemo", "Animation", "Andrew", 100, 18.99)

        self.cart.items = [self.dvd1, self.dvd2, self.dvd3]

    def test_search_by_category(self):
        result = search_by_category(self.cart, "Animation")
        self.assertEqual(result, [self.dvd1, self.dvd3])

    def test_search_by_category_case_insensitive(self):
        result = search_by_category(self.cart, "animation")
        self.assertEqual(result, [self.dvd1, self.dvd3])

    def test_search_by_title(self):
        result = search_by_title(self.cart, "star")
        self.assertEqual(result, [self.dvd2])


if __name__ == "__main__":
    unittest.main()