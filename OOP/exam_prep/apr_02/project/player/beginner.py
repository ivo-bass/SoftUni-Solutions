from project.player.player import Player


class Beginner(Player):
    def __init__(self, username: str):
        super().__init__(username, health=50)
