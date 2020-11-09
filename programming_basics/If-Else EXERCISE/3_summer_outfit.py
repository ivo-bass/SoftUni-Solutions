degrees = int(input())
time_of_the_day = input()

shit = {
    "outfit": {"Morning": {10 <= degrees <= 18: 'Sweatshirt',
                           18 < degrees <= 24: 'Shirt',
                           degrees >= 25: 'T-Shirt'},
               "Afternoon": {10 <= degrees <= 18: 'Shirt',
                             18 < degrees <= 24: 'T-Shirt',
                             degrees >= 25: 'Swim Suit'},
               "Evening": {10 <= degrees <= 18: 'Shirt',
                           18 < degrees <= 24: 'Shirt',
                           degrees >= 25: 'Shirt'}},

    "shoes": {"Morning": {10 <= degrees <= 18: 'Sneakers',
                          18 < degrees <= 24: 'Moccasins',
                          degrees >= 25: 'Sandals'},
              "Afternoon": {10 <= degrees <= 18: 'Moccasins',
                            18 < degrees <= 24: 'Sandals',
                            degrees >= 25: 'Barefoot'},
              "Evening": {10 <= degrees <= 18: 'Moccasins',
                          18 < degrees <= 24: 'Moccasins',
                          degrees >= 25: 'Moccasins'}}
}
outfit = shit['outfit'][time_of_the_day][True]
shoes = shit['shoes'][time_of_the_day][True]
print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")

# degrees = int(input())
# time_of_day = input()
# outfit = ""
# shoes = ""
# if time_of_day == "Morning":
#     if 10 <= degrees <= 18:
#         outfit = "Sweatshirt"
#         shoes = "Sneakers"
#     elif 18 < degrees <= 24:
#         outfit = "Shirt"
#         shoes = "Moccasins"
#     elif degrees >= 25:
#         outfit = "T-Shirt"
#         shoes = "Sandals"
# elif time_of_day == "Afternoon":
#     if 10 <= degrees <= 18:
#         outfit = "Shirt"
#         shoes = "Moccasins"
#     elif 18 < degrees <= 24:
#         outfit = "T-Shirt"
#         shoes = "Sandals"
#     elif degrees >= 25:
#         outfit = "Swim Suit"
#         shoes = "Barefoot"
# else:
#     outfit = "Shirt"
#     shoes = "Moccasins"
#
# print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
