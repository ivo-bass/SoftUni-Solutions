length = int(input())
width = int(input())
height = int(input())
occupied_space_percentage = float(input()) / 100

volume_in_sm = length * width * height
volume_in_litres = volume_in_sm / 1000
occupied_space = occupied_space_percentage * volume_in_litres
water = volume_in_litres - occupied_space

print(f'{water:.3f}')
