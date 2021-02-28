from OOP.exam_prep.prep_1.project.card.card import Card


# from .card import Card


class MagicCard(Card):
    def __init__(self, name: str, damage_points: int = 5, health_points: int = 80):
        super().__init__(name, damage_points, health_points)
