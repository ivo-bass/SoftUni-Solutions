from project.card.card import Card


class TrapCard(Card):
    def __init__(self, name: str):
        super().__init__(name, 120, 5)
