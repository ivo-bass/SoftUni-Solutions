"""You will receive on the first line the rows of the matrix (n) and
on the next n lines you will get each row of the matrix as a string
(zeros and ones separated by a single space). You have to calculate
how many blocks of food you have (connected ones horizontally or vertically)"""

row_count = int(input())
board = []
clusters = 0


def check_neighbours(row, col, board, visited):
	visited[row][col] = True
	if row > 0 and board[row - 1][col] == "1" and visited[row - 1][col] == False:
		check_neighbours(row - 1, col, board, visited)
	if col > 0 and board[row][col - 1] == "1" and visited[row][col - 1] == False:
		check_neighbours(row, col - 1, board, visited)
	if row < len(board) - 1 and board[row + 1][col] == "1" and visited[row + 1][col] == False:
		check_neighbours(row + 1, col, board, visited)
	if col < len(board[0]) - 1 and board[row][col + 1] == "1" and visited[row][col + 1] == False:
		check_neighbours(row, col + 1, board, visited)


for row_index in range(row_count):
	row = input().split()
	board.append(row)

visited = [[False for i in range(len(board[0]))] for j in range(len(board))]

for index_row, row in enumerate(board):
	for index_column, value in enumerate(row):
		if value == "1" and visited[index_row][index_column] == False:
			check_neighbours(index_row, index_column, board, visited)
			clusters += 1

print(clusters)
