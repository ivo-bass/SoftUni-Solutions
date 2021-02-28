from OOP.exam_prep.prep_1.project.card.card import Card


class TrapCard(Card):
    def __init__(self, name: str, damage_points: int = 120, health_points: int = 5):
        super().__init__(name, damage_points, health_points)
