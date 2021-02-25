class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def next_second(self):
        new_h = self.hours
        new_m = self.minutes
        if not self.seconds + 1 > Time.max_seconds:
            new_s = self.seconds + 1
        else:
            new_s = 0
            if not self.minutes + 1 > Time.max_minutes:
                new_m = self.minutes + 1
            else:
                new_m = 0
                if not self.hours + 1 > Time.max_hours:
                    new_h = self.hours + 1
                else:
                    new_h = 0
        self.set_time(new_h, new_m, new_s)
        return self.get_time()

# time = Time(23, 59, 59)
# print(time.next_second())
