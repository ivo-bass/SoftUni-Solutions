total_count = int(input())

colored_eggs = {'red': 0, 'orange': 0, 'blue': 0, "green": 0}
for _ in range(total_count):
    color = input()
    colored_eggs[color] += 1

max_color = 0
max_count = 0
for color, count in colored_eggs.items():
    if count == max(colored_eggs.values()):
        max_count = count
        max_color = color

print(f"Red eggs: {colored_eggs['red']}\n"
      f"Orange eggs: {colored_eggs['orange']}\n"
      f"Blue eggs: {colored_eggs['blue']}\n"
      f"Green eggs: {colored_eggs['green']}\n"
      f"Max eggs: {max_count} -> {max_color}")
