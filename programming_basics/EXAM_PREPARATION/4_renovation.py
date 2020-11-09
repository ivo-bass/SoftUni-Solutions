from math import ceil

hight = int(input())
width = int(input())
percent = int(input()) / 100

room_area = hight * width * 4
to_be_painted = ceil(room_area - room_area * percent)

while True:
    paint_litres = input()
    if paint_litres == "Tired!":
        print(f"{to_be_painted} quadratic m left.")
        break
    paint_litres = int(paint_litres)
    to_be_painted -= paint_litres
    if to_be_painted < 0:
        print(f"All walls are painted and you have {abs(to_be_painted)} l paint left!")
        break
    elif to_be_painted == 0:
        print("All walls are painted! Great job, Pesho!")
        break
