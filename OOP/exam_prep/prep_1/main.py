from project.controller import Controller

c = Controller()
print(c.add_card('Magic', 'Spell'))
print(c.add_player('Beginner', 'Ivo'))
print(c.add_player('Beginner', 'Vesi'))
c.add_player_card('Ivo', 'Spell')
c.add_player_card('Vesi', 'Spell')
print(c.fight('Ivo', 'Vesi'))
print(c.report())
a = 5