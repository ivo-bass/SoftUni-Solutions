sold_count = int(input())

hearthstone_count = 0
fornite_count = 0
overwatch_count = 0
others_count = 0

for s in range(sold_count):
    game_name = input()
    if game_name == "Hearthstone":
        hearthstone_count += 1
    elif game_name == "Fornite":
        fornite_count += 1
    elif game_name == "Overwatch":
        overwatch_count += 1
    else:
        others_count += 1

hearthstone_share = hearthstone_count / sold_count
fornite_share = fornite_count / sold_count
overwatch_share = overwatch_count / sold_count
others_share = others_count / sold_count

print(f"Hearthstone - {hearthstone_share:.2%}")
print(f"Fornite - {fornite_share:.2%}")
print(f"Overwatch - {overwatch_share:.2%}")
print(f"Others - {others_share:.2%}")
