from math import floor

hall_length_sm = float(input()) * 100
hall_width_sm = float(input()) * 100
wardrobe_side_sm = float(input()) * 100

hall_size_sm2 = hall_length_sm * hall_width_sm
wardrobe_size_sm2 = wardrobe_side_sm * wardrobe_side_sm
bench_size_sm2 = hall_size_sm2 / 10
free_space_sm2 = hall_size_sm2 - wardrobe_size_sm2 - bench_size_sm2
space_per_dancer_sm2 = 7040
dancers_count_floored = floor(free_space_sm2 / space_per_dancer_sm2)

print(dancers_count_floored)