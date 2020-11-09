total_clients = int(input())

activities = {
    "work out": {"Back": 0, "Chest": 0, "Legs": 0, "Abs": 0},
    "protein": {"Protein shake": 0, "Protein bar": 0}
}
for _ in range(total_clients):
    activity = input()
    if activity in activities["work out"]:
        activities["work out"][activity] += 1
    elif activity in activities["protein"]:
        activities["protein"][activity] += 1

work_out_percentage = sum(list(activities["work out"].values())) / total_clients * 100
protein_out_percentage = sum(list(activities["protein"].values())) / total_clients * 100

print(f'{activities["work out"]["Back"]} - back')
print(f'{activities["work out"]["Chest"]} - chest')
print(f'{activities["work out"]["Legs"]} - legs')
print(f'{activities["work out"]["Abs"]} - abs')
print(f'{activities["protein"]["Protein shake"]} - protein shake')
print(f'{activities["protein"]["Protein bar"]} - protein bar')
print(f'{work_out_percentage:.2f}% - work out')
print(f'{protein_out_percentage:.2f}% - protein')
