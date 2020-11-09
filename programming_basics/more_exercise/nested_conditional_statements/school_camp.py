season = input()
type_of_group = input()
students_count = int(input())
nights_count = int(input())

prices = {"Winter": {"boys": 9.6, "girls": 9.6, "mixed": 10},
          "Spring": {"boys": 7.2, "girls": 7.2, "mixed": 9.5},
          "Summer": {"boys": 15, "girls": 15, "mixed": 20}}

total_price = prices[season][type_of_group] * students_count * nights_count

discounts = {students_count >= 50: 0.5 * total_price,
             20 <= students_count < 50: 0.15 * total_price,
             10 <= students_count < 20: 0.05 * total_price,
             students_count < 10: 0}
total_price -= discounts[True]

sports = {"Winter": {"boys": "Judo", "girls": "Gymnastics", "mixed": "Ski"},
          "Spring": {"boys": "Tennis", "girls": "Athletics", "mixed": "Cycling"},
          "Summer": {"boys": "Football", "girls": "Volleyball", "mixed": "Swimming"}}

sport = sports[season][type_of_group]

print(f"{sport} {total_price:.2f} lv.")
