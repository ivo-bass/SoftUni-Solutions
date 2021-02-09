from collections import deque


def print_output(customers, time):
    if customers:
        print('Not all customers were driven to their destinations')
        print(f'Customers left: {", ".join(map(str, customers))}')
    else:
        print('All customers were driven to their destinations')
        print(f'Total time: {time} minutes')


def get_input():
    customers = deque([int(c) for c in input().split(', ')])
    taxis = [int(c) for c in input().split(', ')]
    return customers, taxis


customers_times, taxis_fuel = get_input()
total_time = 0
while customers_times and taxis_fuel:
    current_customer = customers_times.popleft()
    current_taxi = taxis_fuel.pop()
    if current_taxi < current_customer:
        customers_times.appendleft(current_customer)
        continue
    total_time += current_customer
print_output(customers_times, total_time)
