import unittest

from project.card.magic_card import MagicCard
from project.card.card_repository import CardRepository


class TestCardRepository(unittest.TestCase):
    def test_init(self):
        pr = CardRepository()
        res = pr.cards, pr.count
        exp = [], 0
        self.assertEqual(res, exp)

    def test_count_add_valid_card(self):
        pr = CardRepository()
        a = MagicCard('asd')
        pr.add(a)
        res = pr.count
        exp = 1
        self.assertEqual(res, exp)

    def test_add_invalid_card(self):
        pr = CardRepository()
        a = MagicCard('asd')
        pr.add(a)
        try:
            pr.add(a)
        except ValueError:
            self.assertRaises(ValueError)

    def test_find(self):
        pr = CardRepository()
        a = MagicCard('asd')
        pr.add(a)
        res = pr.find('asd')
        exp = a
        self.assertEqual(res, exp)

    def test_remove_card(self):
        pr = CardRepository()
        a = MagicCard('asd')
        pr.add(a)
        pr.remove('asd')
        res = pr.count
        exp = 0
        self.assertEqual(res, exp)

    def test_remove_invalid_card(self):
        pr = CardRepository()
        try:
            pr.remove('')
        except ValueError:
            self.assertRaises(ValueError)


if __name__ == '__main__':
    unittest.main()
