goal = 10_000
current_steps = 0

while current_steps < goal:
    steps = input()
    if steps == 'Going home':
        steps = int(input())
        current_steps += steps
        if current_steps >= goal:
            print('Goal reached! Good job!')
        else:
            difference = goal - current_steps
            print(f"{difference} more steps to reach goal.")
        break
    else:
        steps = int(steps)
        current_steps += steps
else:
    print('Goal reached! Good job!')