from project.card.card import Card


class TrapCard(Card):
    def __init__(self, name: str):
        super().__init__(name, damage_points=120, health_points=5)
