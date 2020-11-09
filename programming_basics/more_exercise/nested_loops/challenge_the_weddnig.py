men_count = int(input())
women_count = int(input())
tables_count = int(input())

while tables_count > 0:
    for man in range(1, men_count + 1):
        for woman in range(1, women_count + 1):
            if tables_count <= 0:
                break
            tables_count -= 1
            print(f"({man} <-> {woman})", end=" ")
    else:
        break
