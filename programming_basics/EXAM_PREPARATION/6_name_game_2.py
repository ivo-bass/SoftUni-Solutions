# Създаваме празни списъци,
# където ще се запазват имената на играчите и техните резултати
players = []
results = []

# Отваряме цикъл за всеки нов играч,
# като при команда "Stop" го прекъсваме
while True:
    name = input()
    if name == "Stop":
        break

    name_length = len(name)
    points = 0     # В началото точките са НУЛА

    # Отваряме нов цикъл за всяка буква от името
    # и проверяваме дали входният номер съвпада
    # с ascii стойността на символа
    for n in range(name_length):
        number = input()
        ascii_value = ord(name[n])
        if int(number) == ascii_value:
            points += 10
        else:
            points += 2

    # Добавяме името и резултата
    # на настоящия играч в съответния списък
    players.append(name)
    results.append(points)

# По презумция първият играч има най-висок резултат
best_result = results[0]
best_player = players[0]

# С цикъл проверяваме дали някой от следващите играчи в списъка
# има по-висок резултат, като според заданието
# и при равен рзултат се взима резултата на следващия играч
for r in range(len(results)):
    if results[r] >= results[r-1]:
        best_result = results[r]
        best_player = players[r]

# Принтираме изход от програмата както е по задание
print(f"The winner is {best_player} with {best_result} points!")
