from calendar import month_name


class DVD:
    def __init__(self, name: str, id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    def __repr__(self):
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) " \
               f"has age restriction {self.age_restriction}. " \
               f"Status: {self.check_rented(self.is_rented)}"

    @classmethod
    def from_date(cls, id: int, name: str, date: str, age_restriction: int):
        _, mm, yyyy = date.split('.')
        month = month_name[int(mm)]
        year = int(yyyy)
        return cls(name=name, id=id, creation_year=year, creation_month=month, age_restriction=age_restriction)

    @staticmethod
    def check_rented(rented):
        if rented:
            return 'rented'
        return 'not rented'
