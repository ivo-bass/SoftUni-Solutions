from project.appliances.appliance import Appliance


class Stove(Appliance):
    def __init__(self):
        super().__init__(cost=0.7)
