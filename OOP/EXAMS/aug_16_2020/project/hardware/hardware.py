from project.software.software import Software


class Hardware:
    def __init__(self, name: str, type: str, capacity: int, memory: int):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []
        self.capacity_used = 0
        self.memory_used = 0

    def install(self, software: Software):
        if self.capacity < self.capacity_used + software.capacity_consumption \
                or self.memory < self.memory_used + software.memory_consumption:
            raise Exception("Software cannot be installed")
        self.software_components.append(software)
        self.capacity_used += software.capacity_consumption
        self.memory_used += software.memory_consumption

    def uninstall(self, software: Software):
        self.software_components.remove(software)
        self.capacity_used -= software.capacity_consumption
        self.memory_used -= software.memory_consumption
