def make_readable(time):
    hours = time // 3600
    time %= 3600
    minutes = time // 60
    seconds = time % 60
    return f'{hours:02d}:{minutes:02d}:{seconds:02d}'


print(make_readable(0))
print(make_readable(5))
print(make_readable(60))
print(make_readable(86399))
print(make_readable(359999))
