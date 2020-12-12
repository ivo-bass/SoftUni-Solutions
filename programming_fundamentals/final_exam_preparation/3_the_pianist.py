def add_piece(pieces, piece, composer, key):
	if piece in pieces:
		print(f"{piece} is already in the collection!")
	else:
		pieces[piece] = {"composer": composer, "key": key}
		print(f"{piece} by {composer} in {key} added to the collection!")
	return pieces


def remove_piece(pieces, piece):
	if piece not in pieces:
		print(f"Invalid operation! {piece} does not exist in the collection.")
	else:
		del pieces[piece]
		print(f"Successfully removed {piece}!")
	return pieces


def change_key(pieces, piece, key):
	if piece not in pieces:
		print(f"Invalid operation! {piece} does not exist in the collection.")
	else:
		pieces[piece]["key"] = key
		print(f"Changed the key of {piece} to {key}!")
	return pieces


def get_pieces():
	pieces = {}
	n = int(input())
	for _ in range(n):
		piece, composer, key = input().split("|")
		pieces[piece] = {"composer": composer, "key": key}
	return pieces


def print_pieces(pieces):
	pieces = dict(sorted(pieces.items(), key=lambda x: (x[0], x[1]["composer"])))
	for name, values in pieces.items():
		print(f"{name} -> Composer: {values['composer']}, Key: {values['key']}")


def main():
	pieces = get_pieces()
	while True:
		command = input()
		if command == "Stop":
			break
		action, *token = command.split("|")
		if action == "Add":
			piece, composer, key = token
			pieces = add_piece(pieces, piece, composer, key)
		elif action == "Remove":
			piece = token[0]
			pieces = remove_piece(pieces, piece)
		elif action == "ChangeKey":
			piece, key = token
			pieces = change_key(pieces, piece, key)
	print_pieces(pieces)


main()
