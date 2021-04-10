class CardRepository:
    def __init__(self):
        self.cards = []

    @property
    def count(self):
        return len(self.cards)

    def add(self, card):
        if self.find(card.name) is not None:
            raise ValueError(f"Card {card.name} already exists!")
        self.cards.append(card)

    def remove(self, card: str):  # ????? name or what
        if card == '':
            raise ValueError("Card cannot be an empty string!")
        c = self.find(card)
        self.cards.remove(c)

    def find(self, name: str):
        for card in self.cards:
            if card.name == name:
                return card
