command = input()

count_adults = 0
count_kids = 0
sum_toys = 0
sum_sweaters = 0
while command != "Christmas":
    age = int(command)
    if age > 16:
        count_adults += 1
        sum_sweaters += 15
    else:
        count_kids += 1
        sum_toys += 5
    command = input()

print(f"Number of adults: {count_adults}")
print(f"Number of kids: {count_kids}")
print(f"Money for toys: {sum_toys}")
print(f"Money for sweaters: {sum_sweaters}")
#
# first_top = int(input())
# second_top = int(input())
# third_top = int(input())
#
# for f in range(2, first_top+1, 2):
#     for s in range(2, second_top+1):
#         for th in range(2, third_top+1, 2):
#             if s in (2, 3, 5, 7):
#                 print(f"{f} {s} {th}")
