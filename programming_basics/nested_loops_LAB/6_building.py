floors = int(input())
rooms = int(input())

for f in range(floors, 0, -1):
    rooms_per_floor = []
    for r in range(rooms):
        if f == floors:
            room = f"L{f}{r}"
            rooms_per_floor.append(room)
        else:
            if f % 2 == 0:
                room = f"O{f}{r}"
                rooms_per_floor.append(room)
            else:
                room = f"A{f}{r}"
                rooms_per_floor.append(room)
    print(*rooms_per_floor)
