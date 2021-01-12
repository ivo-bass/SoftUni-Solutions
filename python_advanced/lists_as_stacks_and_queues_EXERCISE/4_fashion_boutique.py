box = input()
rack_capacity = int(input())

current_sum = 0
racks_count = 0

if box:
    stack = [int(s) for s in box.split(' ')]

    while stack:
        current_item = stack.pop()
        current_sum += current_item
        if current_sum < rack_capacity:
            if not racks_count:
                racks_count += 1
        elif current_sum == rack_capacity and stack:
            current_sum = 0
            racks_count += 1
        elif current_sum > rack_capacity:
            current_sum = 0
            current_sum += current_item
            racks_count += 1

print(racks_count)
