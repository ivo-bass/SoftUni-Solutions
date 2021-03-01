class CardRepository:
    def __init__(self):
        self.count = 0
        self.cards = list()

    def add(self, card):
        if any(c.name == card.name for c in self.cards):
            raise ValueError(f"Card {c.name} already exists!")
        self.cards.append(card)
        self.count += 1

    def remove(self, card: str):
        if not card:
            raise ValueError("Player cannot be an empty string!")
        card_found = list(filter(lambda x: x.name == card, self.cards))[0]
        self.cards.remove(card_found)
        self.count -= 1

    def find(self, name: str):
        return list(filter(lambda x: x.name == name, self.cards))[0]
