data = input().strip().split(", ")
WINNING = ('@', '#', '$', '^')


def check_side(side):
	count = 0
	winning_symbol = ""
	for symbol in WINNING:
		if symbol * 6 in side:
			count = side.count(symbol)
			winning_symbol = symbol
	return count, winning_symbol


def check_for_match(t):
	match = False
	length = 0
	left, right = t[:10], t[10:]
	left_length, left_symbol = check_side(left)
	right_length, right_symbol = check_side(right)
	if left_symbol == right_symbol and left_symbol in WINNING:
		match = True
		length = min(left_length, right_length)
	return match, length, left_symbol


for ticket in data:
	ticket = ticket.strip()
	if not len(ticket) == 20:
		print("invalid ticket")
		continue
	is_match, match_length, match_symbol = check_for_match(ticket)
	if not is_match:
		print(f'ticket "{ticket}" - no match')
	elif 6 <= match_length <= 9:
		print(f'ticket "{ticket}" - {match_length}{match_symbol}')
	elif match_length == 10:
		print(f'ticket "{ticket}" - {match_length}{match_symbol} Jackpot!')
