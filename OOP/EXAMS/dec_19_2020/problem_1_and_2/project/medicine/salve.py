from project.medicine.medicine import Medicine


class Salve(Medicine):
    def __init__(self):
        super().__init__(health_increase=50)
