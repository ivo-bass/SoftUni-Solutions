control_minutes = int(input())
control_seconds = int(input())
length = float(input())
seconds_per_100m = int(input())

control_seconds += (control_minutes * 60)

time_seconds = length * (seconds_per_100m / 100)
time_seconds -= (2.5 * (length / 120))

if time_seconds <= control_seconds:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {time_seconds:.3f}.")
else:
    print(f"No, Marin failed! He was {(time_seconds - control_seconds):.3f} second slower.")
