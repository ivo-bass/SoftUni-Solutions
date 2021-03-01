from datetime import datetime, timedelta


class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.time_obj = datetime(100, 1, 1, hour=hours, minute=minutes, second=seconds)

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def next_second(self):
        self.time_obj = self.time_obj + timedelta(seconds=1)
        self.hours = self.time_obj.hour
        self.minutes = self.time_obj.minute
        self.seconds = self.time_obj.second
        return self.get_time()

# time = Time(10, 29, 59)
# print(time.next_second())
