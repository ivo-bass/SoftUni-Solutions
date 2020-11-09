destination = input()

while destination != 'End':
    budget = float(input())
    saved = 0
    while saved < budget:
        savings = float(input())
        saved += savings
    print(f"Going to {destination}!")
    destination = input()
