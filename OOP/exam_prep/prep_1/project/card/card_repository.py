from OOP.exam_prep.prep_1.project.card.card import Card


class CardRepository:
    def __init__(self):
        self.Count = 0
        self.Cards = []

    def add(self, card: Card):
        for c in self.Cards:
            if c.name == card.name:
                raise ValueError(f"Card {c.name} already exists!")
        self.Cards.append(card)
        self.Count += 1

    def remove(self, card: str):
        if not card:
            raise ValueError("Player cannot be an empty string!")
        for i, c in enumerate(self.Cards):
            if c.name == card:
                self.Count -= 1
                self.Cards.pop(i)
                return

    def find(self, name: str):
        for c in self.Cards:
            if c.name == name:
                return c
