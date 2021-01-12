from collections import deque

q = deque()

pumps_count = int(input())
for _ in range(pumps_count):
    q.append(input())

index = 0
success = False
while True:
    fuel_in_tank = 0
    # copy of the que is needed to operate with
    q_copy = q.copy()
    for _ in range(pumps_count):  # The amount of steps in the circle == pumps_count
        amount, distance = q_copy.popleft().split(' ')
        amount, distance = int(amount), int(distance)
        fuel_in_tank += amount
        fuel_in_tank -= distance
        # If the fuel is negative, the tank cannot proceed
        if fuel_in_tank < 0:
            success = False
            break
        # Otherwise the circle is closed
        success = True
    if success:
        break
    # If the circle is not closed we try starting from next index
    q.append(q.popleft())
    index += 1
print(index)

# The complexity is O(n^2)
