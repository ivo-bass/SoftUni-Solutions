"""As a young baker_, you are baking the bread out of the bakery.
You have initial energy 100 and initial coins 100.
You will be given a string, representing the working day events.
Each event_ is separated with '|' (vertical bar): "event1|event2|event3…"
"""

events_string = input()

events_list = list(events_string.strip().split("|"))
baker = [100, 100]  # [0]= energy, [1]= coins


def rest(energy_, value_):
	"""If the event_ is "rest": you gain energy, the number in the second
	part. But your energy cannot exceed your initial energy (100)"""
	energy_ += value_
	if energy_ > 100:
		value_ -= energy_ - 100
		energy_ = 100
	print(f"You gained {value_} energy.")
	print(f"Current energy: {energy_}.")
	return energy_


def order(energy_, coins_, value_):
	"""If the event_ is "order": You've earned some coins, the number
	in the second part. Each time you get an order,
	your energy decreases with 30 points."""
	if energy_ >= 30:
		coins_ += value_
		energy_ -= 30
		print(f"You earned {value_} coins.")
	else:
		energy_ += 50
		print("You had to rest!")
	return [energy_, coins_]


def buy(item_, value_, coins_):
	"""In any other case you are having an ingredient, you have to buy.
	The second part of the event_, contains the coins you have to spent
	and remove from your coins. """
	if value_ < coins_:
		coins_ -= value_
		print(f"You bought {item_}.")
	else:
		print(f"Closed! Cannot afford {item_}.")
		quit(0)
	return coins_


def actions(baker_, event_, value_):
	if event_ == "rest":
		baker_[0] = rest(baker_[0], value_)
	elif event_ == "order":
		baker_ = order(baker_[0], baker_[1], value_)
	else:
		baker_[1] = buy(event_, value_, baker_[1])
	return baker_


for e in events_list:
	event_split = list(e.split("-"))
	event = event_split[0]
	value = int(event_split[1])
	baker = actions(baker, event, value)

print(f"Day completed!\nCoins: {baker[1]}\nEnergy: {baker[0]}")
