class Bunker:
    def __init__(self):
        self.survivors = []
        self.supplies = []
        self.medicine = []

    @property
    def food(self):
        foods = [s for s in self.supplies if s.__class__.__name__ == 'FoodSupply']
        if not foods:
            raise IndexError("There are no food supplies left!")
        return foods

    @property
    def water(self):
        water = [s for s in self.supplies if s.__class__.__name__ == 'WaterSupply']
        if not water:
            raise IndexError("There are no water supplies left!")
        return water

    @property
    def painkillers(self):
        painkiller = [s for s in self.medicine if s.__class__.__name__ == 'Painkiller']
        if not painkiller:
            raise IndexError("There are no painkillers left!")
        return painkiller

    @property
    def salves(self):
        salve = [s for s in self.medicine if s.__class__.__name__ == 'Salve']
        if not salve:
            raise IndexError("There are no salves left!")
        return salve

    def add_survivor(self, survivor):
        for s in self.survivors:
            if s.name == survivor.name:
                raise ValueError(f"Survivor with name {s.name} already exists.")
        self.survivors.append(survivor)

    def add_supply(self, supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine):
        self.medicine.append(medicine)

    def heal(self, survivor, medicine_type: str):
        med = None
        if survivor.needs_healing:
            for index in range(len(self.medicine)-1, -1, -1):
                if self.medicine[index].__class__.__name__ == medicine_type:
                    med = self.medicine.pop(index)
                    break
            if med:
                med.apply(survivor)
                return f"{survivor.name} healed successfully with {medicine_type}"

    def sustain(self, survivor, sustenance_type: str):
        sustenance = None
        if survivor.needs_sustenance:
            for index in range(len(self.supplies)-1, -1, -1):
                if self.supplies[index].__class__.__name__ == sustenance_type:
                    sustenance = self.supplies.pop(index)
                    break
            if sustenance:
                sustenance.apply(survivor)
                return f"{survivor.name} sustained successfully with {sustenance_type}"

    def next_day(self):
        for survivor in self.survivors:
            result = survivor.age * 2
            survivor.needs -= result

            self.sustain(survivor, 'FoodSupply')
            self.sustain(survivor, 'WaterSupply')
