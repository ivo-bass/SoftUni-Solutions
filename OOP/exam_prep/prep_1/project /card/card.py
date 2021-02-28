from abc import ABC


class Card(ABC):
    def __init__(self, name: str, damage_points: int, health_points: int):
        if not name:
            raise ValueError("Card's name cannot be an empty string.")
        if damage_points < 0:
            raise ValueError("Card's damage points cannot be less than zero.")
        if health_points < 0:
            raise ValueError("Card's HP cannot be less than zero.")
        self.name = name
        self.damage_points = damage_points
        self.health_points = health_points
