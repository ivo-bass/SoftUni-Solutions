exam_hour = int(input())
exam_minute = int(input())
student_hour = int(input())
student_minute = int(input())

exam_time = exam_hour * 60 + exam_minute
student_time = student_hour * 60 + student_minute
time_difference = exam_time - student_time
abs_time_difference = abs(time_difference)
abs_hour_difference = 0
abs_minutes_difference = 0

if abs_time_difference < 60:
    abs_minutes_difference = abs(time_difference)
else:
    abs_hour_difference = int(abs_time_difference / 60)
    abs_minutes_difference = abs_time_difference % 60

evaluation = 'On time'

if time_difference == 0:
    print(evaluation)
elif 0 < time_difference <= 30:
    print(evaluation)
    print(f'{abs_minutes_difference} minutes before the start')
elif 30 < time_difference < 60:
    evaluation = 'Early'
    print(evaluation)
    print(f'{abs_minutes_difference} minutes before the start')
elif time_difference >= 60:
    evaluation = 'Early'
    print(evaluation)
    print(f'{abs_hour_difference}:{abs_minutes_difference:02d} hours before the start')
elif -60 < time_difference < 0:
    evaluation = 'Late'
    print(evaluation)
    print(f'{abs_minutes_difference} minutes after the start')
elif time_difference <= -60:
    evaluation = 'Late'
    print(evaluation)
    print(f'{abs_hour_difference}:{abs_minutes_difference:02d} hours after the start')
