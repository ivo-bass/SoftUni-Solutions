from math import ceil

name = input()
episode_time = int(input())
break_time = int(input())

lunch_time = 1/8 * break_time
relax_time = 1/4 * break_time
free_time = break_time - lunch_time - relax_time

time_difference = free_time - episode_time

if time_difference >= 0:
    print(f"You have enough time to watch {name} and left with {ceil(time_difference)} minutes free time.")
else:
    print(f"You don't have enough time to watch {name}, you need {ceil(abs(time_difference))} more minutes.")
