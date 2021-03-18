from project.player.player import Player


class PlayerRepository:
    def __init__(self):
        self.count = 0
        self.players = []

    def add(self, player: Player):
        if self.find(player.username) is not None:
            raise ValueError(f"Player {player.username} already exists!")
        self.players.append(player)
        self.count += 1

    def remove(self, player: str):  # ??? does this mean the username ???
        if player == '':
            raise ValueError("Player cannot be an empty string!")
        pl = self.find(player)
        self.players.remove(pl)
        self.count -= 1

    def find(self, username: str) -> Player:
        for pl in self.players:
            if pl.username == username:
                return pl
