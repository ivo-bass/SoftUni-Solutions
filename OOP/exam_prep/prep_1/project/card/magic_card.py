from project.card.card import Card


class MagicCard(Card):
    def __init__(self, name: str):
        super().__init__(name, 5, 80)
