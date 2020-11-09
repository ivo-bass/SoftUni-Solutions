string = input()
count_shuffles = int(input())

original_deck = list(string.split())
half_deck_length = len(original_deck) // 2


def faro_shuffle(deck, h_len):
	shuffled_deck = []
	first_half = deck[:h_len]
	second_half = deck[h_len:]
	for _ in range(h_len):
		shuffled_deck.append(first_half.pop(0))
		shuffled_deck.append(second_half.pop(0))
	return shuffled_deck


for _ in range(count_shuffles):
	original_deck = faro_shuffle(original_deck, half_deck_length)

print(original_deck)
