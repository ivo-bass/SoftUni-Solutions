from typing import Union

from project.decoration.ornament import Ornament
from project.decoration.plant import Plant


class DecorationRepository:
    def __init__(self):
        self.decorations = []

    def add(self, decoration: Union[Ornament, Plant]):
        self.decorations.append(decoration)

    def remove(self, decoration: Union[Ornament, Plant]):
        if decoration not in self.decorations:
            return False
        self.decorations.remove(decoration)
        return True

    def find_by_type(self, decoration_type: str):
        for decoration in self.decorations:
            if decoration.__class__.__name__ == decoration_type:
                return decoration
        return 'None'
