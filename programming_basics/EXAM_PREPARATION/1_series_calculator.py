name = input()
seasons = int(input())
episodes_count = int(input())
episodes_time = float(input())

adds = episodes_time * 0.2
episodes_time += adds
last_episode_time = episodes_time + 10
episodes_time_per_season = episodes_time * (episodes_count - 1) + last_episode_time
total_time = seasons * episodes_time_per_season

print(f"Total time needed to watch the {name} series is {int(total_time)} minutes.")
