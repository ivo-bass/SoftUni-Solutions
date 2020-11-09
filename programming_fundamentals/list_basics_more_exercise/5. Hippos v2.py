row_count = int(input())
board = []
letters = [chr(l) for l in range(65, 90)]
assigned = []

def check_neighbours_for_letter():
	pass

for row_index in range(row_count):
	row = input().split()
	board.append(row)

