import unittest

from OOP.exam_prep.prep_1.project.card.card_repository import CardRepository
from OOP.exam_prep.prep_1.project.card.magic_card import MagicCard


class CardRepositoryTest(unittest.TestCase):
    def test_init_count_is_0(self):
        repo = CardRepository()
        act = repo.Count
        exp = 0
        self.assertEqual(act, exp)

    def test_init_cards_is_empty_list(self):
        repo = CardRepository()
        act = repo.Cards
        exp = []
        self.assertEqual(act, exp)

    def test_count_when_added_card(self):
        repo = CardRepository()
        repo.add(MagicCard('a'))
        act = repo.Count
        exp = 1
        self.assertEqual(act, exp)

    def test_cards_when_added_card(self):
        repo = CardRepository()
        repo.add(MagicCard('a'))
        act = repo.Cards[0].name
        exp = 'a'
        self.assertEqual(act, exp)

    def test_add_existing_card(self):
        repo = CardRepository()
        repo.add(MagicCard('a'))
        try:
            repo.add(MagicCard('a'))
        except:
            self.assertRaises(ValueError)
