book_name = input()
library_capacity = int(input())

check = 0

while check < library_capacity:
    current_book = input()
    if current_book == book_name:
        print(f"You checked {check} books and found it.")
        break
    check += 1
else:
    print("The book you search is not here!")
    print(f"You checked {check} books.")
