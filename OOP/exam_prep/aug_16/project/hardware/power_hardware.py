from project.hardware.hardware import Hardware


class PowerHardware(Hardware):
    def __init__(self, name: str, capacity: int, memory: int):
        super().__init__(
            name=name,
            type='Power',
            capacity=capacity,
            memory=memory
        )
        self.capacity = int(0.25 * capacity)
        self.memory = int(1.75 * memory)
