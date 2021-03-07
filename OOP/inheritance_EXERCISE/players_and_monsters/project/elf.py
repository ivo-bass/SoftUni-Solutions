from project.hero import Hero


class Elf(Hero):
    def __init__(self, username: str, level: int):
        super().__init__(username, level)
