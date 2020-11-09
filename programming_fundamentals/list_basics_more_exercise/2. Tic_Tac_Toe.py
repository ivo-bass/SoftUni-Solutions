"""You will receive a field of a tic-tac-toe game in three lines
containing numbers separated by a single space.
Legend:
 0 - empty space
 1 - first player move
 2 - second player move"""

row_1 = input().split()
row_2 = input().split()
row_3 = input().split()

is_winner = False
winner = ""

# check rows for winner
if row_1[0] == row_1[1] == row_1[2] != "0":
	is_winner = True
	winner = row_1[0]
elif row_2[0] == row_2[1] == row_2[2] != "0":
	is_winner = True
	winner = row_2[0]
elif row_3[0] == row_3[1] == row_3[2] != "0":
	is_winner = True
	winner = row_3[0]

# check columns for winner
if row_1[0] == row_2[0] == row_3[0] != "0":
	is_winner = True
	winner = row_1[0]
elif row_1[1] == row_2[1] == row_3[1] != "0":
	is_winner = True
	winner = row_1[1]
elif row_1[2] == row_2[2] == row_3[2] != "0":
	is_winner = True
	winner = row_1[2]

# check diagonals for winner
if row_1[0] == row_2[1] == row_3[2] != "0":
	is_winner = True
	winner = row_1[0]
elif row_1[2] == row_2[1] == row_3[0] != "0":
	is_winner = True
	winner = row_1[2]

if not is_winner:
	print("Draw!")
else:
	if winner == "1":
		print("First player won")
	elif winner == "2":
		print("Second player won")