import unittest

from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard


class CardRepositoryTest(unittest.TestCase):
    def test_init_count_is_0(self):
        repo = CardRepository()
        act = repo.count
        exp = 0
        self.assertEqual(exp, act)

    def test_init_cards_is_empty_list(self):
        repo = CardRepository()
        act = repo.cards
        exp = []
        self.assertEqual(exp, act)

    def test_count_when_added_card(self):
        repo = CardRepository()
        repo.add(MagicCard('a'))
        act = repo.count
        exp = 1
        self.assertEqual(exp, act)

    def test_cards_when_added_card(self):
        repo = CardRepository()
        repo.add(MagicCard('a'))
        act = repo.cards[0].name
        exp = 'a'
        self.assertEqual(exp, act)

    def test_add_existing_card(self):
        repo = CardRepository()
        repo.add(MagicCard('a'))
        try:
            repo.add(MagicCard('a'))
        except:
            self.assertRaises(ValueError)
