name_actor = input()
points = float(input())
count = int(input())

for _ in range(count):
    name_jury = input()
    points_jury = float(input())
    points += len(name_jury) * points_jury/2
    if points > 1250.5:
        print(f"Congratulations, {name_actor} got a nominee for leading role with {points:.1f}!")
        break

if points <= 1250.5:
    print(f"Sorry, {name_actor} you need {(1250.5 - points):.1f} more!")
