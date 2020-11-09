total_time = int(input())
scenes_count = int(input())
scene_time = int(input())

preparation = total_time * 0.15
filming_time = scene_time * scenes_count + preparation

difference = total_time - filming_time

if difference >= 0:
    print(f"You managed to finish the movie on time! You have {round(difference)} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {round(abs(difference))} minutes.")
