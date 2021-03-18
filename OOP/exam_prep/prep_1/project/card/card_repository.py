from project.card.card import Card


class CardRepository:
    def __init__(self):
        self.count = 0
        self.cards = []

    def add(self, card: Card):
        if self.find(card.name) is not None:
            raise ValueError(f"Card {card.name} already exists!")
        self.cards.append(card)
        self.count += 1

    def remove(self, card: str):  # ????? name or what
        if card == '':
            raise ValueError("Card cannot be an empty string!")
        c = self.find(card)
        self.cards.remove(c)
        self.count -= 1

    def find(self, name: str) -> Card:
        for c in self.cards:
            if c.name == name:
                return c
