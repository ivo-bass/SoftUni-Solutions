def cast_spell(dic, name, mp_needed, spell_name):
	if dic[name]["mp"] >= mp_needed:
		dic[name]["mp"] -= mp_needed
		print(
			f'{name} has successfully cast {spell_name} and now has {dic[name]["mp"]} MP!')
	else:
		print(f'{name} does not have enough MP to cast {spell_name}!')
	return dic


def take_damage(dic, name, damage, attacker):
	dic[name]["hp"] -= damage
	if dic[name]["hp"] > 0:
		print(f'{name} was hit for {damage} HP by {attacker} and now has {dic[name]["hp"]} HP left!')
	else:
		del dic[name]
		print(f'{name} has been killed by {attacker}!')
	return dic


def recharge(dic, name, amount):
	if amount + dic[name]["mp"] > 200:
		amount = 200 - dic[name]["mp"]
	dic[name]["mp"] += amount
	print(f'{name} recharged for {amount} MP!')
	return dic


def heal(dic, name, amount):
	if amount + dic[name]["hp"] > 100:
		amount = 100 - dic[name]["hp"]
	dic[name]["hp"] += amount
	print(f'{name} healed for {amount} HP!')
	return dic


def get_info(dic):
	dic = dict(sorted(dic.items(), key=lambda item: (-item[1]["hp"], item[0])))
	for name, values in dic.items():
		print(name)
		print(f'  HP: {values["hp"]}')
		print(f'  MP: {values["mp"]}')


def main():
	heroes = {}
	count = int(input())
	for _ in range(count):
		data = input().split()
		name, hp, mp = data[0], int(data[1]), int(data[2])
		if hp > 100:
			hp = 100
		if mp > 200:
			mp = 200
		heroes[name] = {"hp": hp, "mp": mp}

	while True:
		command = input()
		if command == "End":
			get_info(heroes)
			break
		action, name, *values = command.split(" - ")
		if action == "CastSpell":
			mp_needed, spell_name = int(values[0]), values[1]
			heroes = cast_spell(heroes, name, mp_needed, spell_name)
		elif action == "TakeDamage":
			damage, attacker = int(values[0]), values[1]
			heroes = take_damage(heroes, name, damage, attacker)
		elif action == "Recharge":
			amount = int(values[0])
			heroes = recharge(heroes, name, amount)
		elif action == "Heal":
			amount = int(values[0])
			heroes = heal(heroes, name, amount)


main()
