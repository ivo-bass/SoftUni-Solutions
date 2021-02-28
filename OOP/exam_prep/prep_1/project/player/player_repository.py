class PlayerRepository:
    def __init__(self):
        self.count = 0
        self.players = []

    def add(self, player):
        for pl in self.players:
            if pl.username == player.username:
                raise ValueError(f"Player {pl.username} already exists!")
        self.players.append(player)
        self.count += 1

    def remove(self, player: str):
        if not player:
            raise ValueError("Player cannot be an empty string!")
        for i, pl in enumerate(self.players):
            if pl.username == player:
                self.count -= 1
                self.players.pop(i)
                return

    def find(self, username: str):
        for pl in self.players:
            if pl.username == username:
                return pl
