class PlayerRepository:
    def __init__(self):
        self.count = 0
        self.players = list()

    def add(self, player):
        if any(pl.username == player.username for pl in self.players):
            raise ValueError(f"Player {pl.username} already exists!")
        self.players.append(player)
        self.count += 1

    def remove(self, player: str):
        if not player:
            raise ValueError("Player cannot be an empty string!")
        found_player = list(filter(lambda x: x.username == player, self.players))[0]
        self.players.remove(found_player)
        self.count -= 1

    def find(self, username: str):
        return list(filter(lambda x: x.username == username, self.players))[0]
