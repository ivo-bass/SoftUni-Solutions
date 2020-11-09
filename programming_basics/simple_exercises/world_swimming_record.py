record = float(input())
distance = float(input())
time_per_m = float(input())

time = time_per_m * distance

if distance >= 15:
    times_slowed = int(distance // 15)
    for i in range(times_slowed):
        time += 12.5

if time < record:
    print(f" Yes, he succeeded! The new world record is {time:.2f} seconds.")
else:
    time_over = time - record
    print(f"No, he failed! He was {time_over:.2f} seconds slower.")
