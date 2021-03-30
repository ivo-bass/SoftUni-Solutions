from project.hardware.hardware import Hardware


class HeavyHardware(Hardware):
    def __init__(self, name: str, capacity: int, memory: int):
        super().__init__(
            name=name,
            type='Heavy',
            capacity=capacity,
            memory=memory
        )
        self.capacity = int(2 * capacity)
        self.memory = int(0.75 * memory)
