hrizantemi_count = int(input())
roses_count = int(input())
tulips_count = int(input())
season = input()
if_holiday = input()

if season in ('Spring', 'Summer'):
    hrizantemi_price = 2
    roses_price = 4.1
    tulips_price = 2.5
else:
    hrizantemi_price = 3.75
    roses_price = 4.5
    tulips_price = 4.15

total_count = hrizantemi_count + roses_count + tulips_count
total_price = hrizantemi_count * hrizantemi_price + \
              roses_count * roses_price + \
              tulips_count * tulips_price

if if_holiday == 'Y':
    total_price *= 1.15

if season == 'Spring' and tulips_count > 7:
    total_price *= 0.95
if season == 'Winter' and roses_count >= 10:
    total_price *= 0.9
if total_count > 20:
    total_price *= 0.8

total_price += 2

print(f'{total_price:.2f}')
