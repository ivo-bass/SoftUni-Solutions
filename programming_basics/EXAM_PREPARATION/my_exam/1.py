from math import ceil

avrg_speed = float(input())
fuel_consumption = float(input())

distance = 384400 * 2
time_travel = ceil(distance / avrg_speed)
total_time = int(time_travel + 3)
total_fuel = int((fuel_consumption * distance) / 100)

print(f"{total_time}")
print(f"{total_fuel}")
