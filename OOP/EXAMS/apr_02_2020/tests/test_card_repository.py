import unittest

from project.card.magic_card import MagicCard
from project.card.card_repository import CardRepository


class TestCardRepository(unittest.TestCase):
    def setUp(self) -> None:
        self.repo = CardRepository()
        self.card = MagicCard('name')

    def test_init(self):
        self.assertEqual(0, self.repo.count)
        self.assertListEqual([], self.repo.cards)

    def test_add__when_valid__should_add_to_cards(self):
        self.repo.add(self.card)
        self.assertIn(self.card, self.repo.cards)

    def test_add__when_valid__should_increase_count(self):
        self.repo.add(self.card)
        self.assertEqual(1, self.repo.count)

    def test_add__when_card_exists__should_raise(self):
        self.repo.add(self.card)
        new_card = MagicCard('name')
        with self.assertRaises(ValueError) as exc:
            self.repo.add(new_card)
        msg = f"Card {new_card.name} already exists!"
        self.assertEqual(msg, str(exc.exception))

    def test_remove__when_valid__should_remove(self):
        self.repo.add(self.card)
        self.repo.remove('name')
        self.assertNotIn(self.card, self.repo.cards)

    def test_remove__when_valid__should_decrease_count(self):
        self.repo.add(self.card)
        self.repo.remove('name')
        self.assertEqual(0, self.repo.count)

    def test_remove__when_empty_name__should_raise(self):
        self.repo.add(self.card)
        with self.assertRaises(ValueError) as exc:
            self.repo.remove('')
        msg = "Card cannot be an empty string!"
        self.assertEqual(msg, str(exc.exception))

    def test_find__should_return_card(self):
        self.repo.add(self.card)
        res = self.repo.find('name')
        self.assertEqual(self.card, res)


if __name__ == '__main__':
    unittest.main()
