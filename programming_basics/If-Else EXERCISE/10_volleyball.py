year_type = input()
holidays = int(input())
hometown_weekends = int(input())

plays_volley = (3/4 * (48 - hometown_weekends)) + (2/3 * holidays) + hometown_weekends

if year_type == 'leap':
    plays_volley *= 1.15

print(int(plays_volley))
