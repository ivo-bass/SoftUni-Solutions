best_movie = ''
best_ascii_sum = 0
for i in range(7):
    title = input()
    if title == "STOP":
        break
    current_ascii_sum = 0
    for c in title:
        current_ascii_sum += ord(c)
        if c in "abcdefghijklmnopqrstuvwxyz":
            current_ascii_sum -= 2 * len(title)
        elif c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            current_ascii_sum -= len(title)
    if current_ascii_sum > best_ascii_sum:
        best_ascii_sum = current_ascii_sum
        best_movie = title
    if i == 6:
        print("The limit is reached.")

print(f"The best movie for you is {best_movie} with {best_ascii_sum} ASCII sum.")
