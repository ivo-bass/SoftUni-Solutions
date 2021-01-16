from collections import deque

END_COMMAND = 'END'
GREEN_CYCLE_COMMAND = 'green'

green_light_duration = int(input())
free_window_duration = int(input())

cars_queue = deque()
cars_passed = []

is_crash = False
while not is_crash:
    command = input()
    if command == END_COMMAND:
        break
    if command == GREEN_CYCLE_COMMAND:
        time = 0
        char = ''
        passing_car = None
        while time < green_light_duration:
            time += 1
            if cars_queue and not passing_car:
                car = cars_queue.popleft()
                passing_car = car.copy()
            if passing_car:
                char = passing_car.popleft()
                if not passing_car:
                    cars_passed.append(car)
                    char = ''
        time = 0
        if char:
            char = passing_car.popleft()
            while time < free_window_duration:
                time += 1
                if passing_car:
                    char = passing_car.popleft()
                else:
                    cars_passed.append(car)
                    char = ''
                    break

        if char:
            print(f'A crash happened!')
            print(f'{"".join(car)} was hit at {char}.')
            is_crash = True

    else:
        cars_chars = deque([ch for ch in command])
        cars_queue.append(cars_chars)

if not is_crash:
    print('Everyone is safe.')
    print(f'{len(cars_passed)} total cars passed the crossroads.')
