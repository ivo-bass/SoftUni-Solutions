class PlayerRepository:
    def __init__(self):
        self.players = []

    @property
    def count(self):
        return len(self.players)

    def add(self, player):
        if self.find(player.username) is not None:
            raise ValueError(f"Player {player.username} already exists!")
        self.players.append(player)

    def remove(self, player: str):  # ??? does this mean the username ???
        if not player:
            raise ValueError("Player cannot be an empty string!")
        pl = self.find(player)
        self.players.remove(pl)

    def find(self, username: str):
        for player in self.players:
            if player.username == username:
                return player
