time1 = int(input())
time2 = int(input())
time3 = int(input())

total_time = time1 + time2 + time3

minutes = total_time // 60
seconds = total_time % 60


print(f'{minutes}:{seconds:02d}')
