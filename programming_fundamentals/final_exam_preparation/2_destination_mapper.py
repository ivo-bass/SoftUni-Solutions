from re import findall
destinations = [match[1] for match in findall(r"([=|/])([A-Z][A-Za-z]{2,})(\1)", input())]
print(f"Destinations: {', '.join(destinations)}\nTravel Points: {sum([len(d) for d in destinations])}")
