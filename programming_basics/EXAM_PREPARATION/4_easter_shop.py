eggs_count = int(input())

eggs_sold = 0
while True:
    command = input()
    if command == 'Close':
        print("Store is closed!")
        print(f"{eggs_sold} eggs sold.")
        break

    elif command == 'Buy':
        current_count = int(input())
        if current_count > eggs_count:
            print("Not enough eggs in store!")
            print(f"You can buy only {eggs_count}.")
            break
        eggs_count -= current_count
        eggs_sold += current_count

    elif command == 'Fill':
        current_count = int(input())
        eggs_count += current_count
