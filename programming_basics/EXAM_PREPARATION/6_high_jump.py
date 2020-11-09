goal_height = int(input())
current_height = goal_height - 30
total_attempts = 0
success = False
while not success:
    for _ in range(3):
        attempt_height = int(input())
        total_attempts += 1
        if goal_height <= current_height < attempt_height:
            success = True
            break
        if attempt_height > current_height:
            current_height += 5
            break
    else:
        break

if success:
    print(f"Tihomir succeeded, he jumped over {current_height}cm after {total_attempts} jumps.")
else:
    print(f"Tihomir failed at {current_height}cm after {total_attempts} jumps.")
