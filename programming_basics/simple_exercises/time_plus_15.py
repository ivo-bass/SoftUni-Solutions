hour_input = int(input())
minutes_input = int(input())

input_time_in_minutes = hour_input * 60 + minutes_input
output_time_in_minutes = input_time_in_minutes + 15

hour_output = output_time_in_minutes // 60
minutes_output = output_time_in_minutes % 60

if hour_output == 24:
    hour_output = 0

print(f"{hour_output}:{minutes_output:02d}")
