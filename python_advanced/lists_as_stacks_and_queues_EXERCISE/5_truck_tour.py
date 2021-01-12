from collections import deque

q_fuel = deque()
q_dist = deque()

pumps_count = int(input())

for _ in range(pumps_count):
    # Fill the queues
    info = input().split(' ')
    amount, distance = int(info[0]), int(info[1])
    q_fuel.append(amount)
    q_dist.append(distance)

index = 0
success = False
while True:
    fuel_in_tank = 0
    # copies of the dequeues are needed to operate
    q_f_copy = q_fuel.copy()
    q_d_copy = q_dist.copy()
    for _ in range(pumps_count):  # The amount of steps in the circle == pumps_count
        # First we take the properties of the current pump
        current_amount = q_f_copy.popleft()
        next_distance = q_d_copy.popleft()
        # Then we add the ammount to the tank
        fuel_in_tank += current_amount
        # Then we extract the distance from the tank
        fuel_in_tank -= next_distance
        # If the fuel is negative, the tank cannot proceed
        if fuel_in_tank < 0:
            success = False
            break
        # Otherwise the circle is closed
        success = True
    if success:
        break
    # If the circle is not closed we try starting from next index
    q_fuel.append(q_fuel.popleft())
    q_dist.append(q_dist.popleft())
    index += 1

print(index)

# The complexity is On
# TODO: optimize
