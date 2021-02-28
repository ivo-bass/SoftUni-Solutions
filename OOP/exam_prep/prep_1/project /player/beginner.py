# from OOP.exam_prep.prep_1.project.player.player import Player


from .player import Player


class Beginner(Player):
    def __init__(self, username: str, health: int = 50):
        super().__init__(username, health)
