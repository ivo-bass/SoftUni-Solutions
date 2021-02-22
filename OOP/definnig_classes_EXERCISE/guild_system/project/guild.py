class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players = []

    def assign_player(self, p):
        if p.guild == 'Unaffiliated':
            p.guild = self.name
            self.players.append(p)
            return f"Welcome player {p.name} to the guild {self.name}"
        if p.guild == self.name:
            return f"Player {p.name} is already in the guild."
        return f"Player {p.name} is in another guild."

    def kick_player(self, player_name):
        for p in self.players:
            if p.name == player_name:
                p.guild = 'Unaffiliated'
                self.players.remove(p)
                return f"Player {player_name} has been removed from the guild."
        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        g_info = f"Guild: {self.name}\n"
        pl_info = ''
        for pl in self.players:
            pl_info += f'{pl.player_info()}'
        return g_info + pl_info

# george = Player("George", 50, 100)
# ivo = Player("Ivo", 150, 200)
# print(george.add_skill("Shield Break", 20))
# print(ivo.add_skill('sth', 100))
# print(george.player_info())
# print(ivo.player_info())
# guild = Guild("UGT")
# guild2 = Guild("G2")
# print(guild.assign_player(george))
# print(guild2.assign_player(ivo))
# print(guild.kick_player(george.name))
# print(guild2.assign_player(george))
# print(guild2.kick_player(ivo.name))
# print(ivo.player_info())
# print(guild.guild_info())
# print(guild2.guild_info())
