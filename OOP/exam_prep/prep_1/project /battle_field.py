# from OOP.exam_prep.prep_1.project.player.beginner import Beginner


from .player.beginner import Beginner


class BattleField:

    @staticmethod
    def check_for_dead(pl):
        if pl.is_dead:
            raise ValueError("Player is dead!")

    @staticmethod
    def check_for_beginner(pl):
        if type(pl) is Beginner:
            pl.health += 40
            for card in pl.card_repository.Cards:
                card.damage_points += 30

    @staticmethod
    def get_bonus_hp(pl):
        bonus = 0
        for card in pl.card_repository.Cards:
            bonus += card.health_points

    def prepare_for_fight(self, attacker, enemy):
        self.check_for_dead(attacker)
        self.check_for_dead(enemy)
        self.check_for_beginner(attacker)
        self.check_for_beginner(enemy)
        self.get_bonus_hp(attacker)
        self.get_bonus_hp(enemy)

    def attack(self, pl1, pl2):
        for card in pl1.card_repository.Cards:
            pl2.health -= card.damage_points
            # Might have to deal all cards before check for dead
            self.check_for_dead(pl2)  # raises ValueError, may not have to raise error

    def fight(self, attacker, enemy):
        self.prepare_for_fight(attacker, enemy)
        self.attack(pl1=attacker, pl2=enemy)
        self.attack(pl1=enemy, pl2=attacker)
