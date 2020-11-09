count_biscuits_per_worker_per_day = int(input())
count_of_workers = int(input())
rival_factory_per_month = int(input())

my_factory_per_day = count_biscuits_per_worker_per_day * count_of_workers
my_factory_per_month = int(20 * my_factory_per_day + 10 * 0.75 * my_factory_per_day)
difference = (my_factory_per_month - rival_factory_per_month)
percentage = difference/rival_factory_per_month * 100

print(f"You have produced {my_factory_per_month} biscuits for the past month.")
if difference > 0:
	print(f"You produce {percentage:.2f} percent more biscuits.")
else:
	print(f"You produce {abs(percentage):.2f} percent less biscuits.")
