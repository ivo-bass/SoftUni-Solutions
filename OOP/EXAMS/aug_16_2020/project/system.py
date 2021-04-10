from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


def find(name, ll):
    inst = None
    for el in ll:
        if el.name == name:
            inst = el
    return inst


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        inst = PowerHardware(name=name, capacity=capacity, memory=memory)
        System._hardware.append(inst)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        inst = HeavyHardware(name=name, capacity=capacity, memory=memory)
        System._hardware.append(inst)

    @staticmethod
    def register_express_software(
            hardware_name: str,
            name: str,
            capacity_consumption: int,
            memory_consumption: int
    ):
        hardware = find(hardware_name, System._hardware)
        if not hardware:
            return "Hardware does not exist"
        software = ExpressSoftware(
            name=name,
            capacity_consumption=capacity_consumption,
            memory_consumption=memory_consumption
        )
        try:
            hardware.install(software)
            System._software.append(software)
        except Exception as exc:
            return exc.args[0]

    @staticmethod
    def register_light_software(
            hardware_name: str,
            name: str,
            capacity_consumption: int,
            memory_consumption: int
    ):
        hardware = find(hardware_name, System._hardware)
        if not hardware:
            return "Hardware does not exist"
        software = LightSoftware(
            name=name,
            capacity_consumption=capacity_consumption,
            memory_consumption=memory_consumption
        )
        try:
            hardware.install(software)
            System._software.append(software)
        except Exception as exc:
            return exc.args[0]

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        hardware = find(hardware_name, System._hardware)
        software = find(software_name, System._software)
        if not hardware or not software:
            return "Some of the components do not exist"
        hardware.uninstall(software)
        System._software.remove(software)

    @staticmethod
    def analyze():
        total_memory = sum(hardware.memory for hardware in System._hardware)
        total_memory_used = sum(hardware.memory_used for hardware in System._hardware)
        total_capacity = sum(hardware.capacity for hardware in System._hardware)
        total_capacity_used = sum(hardware.capacity_used for hardware in System._hardware)

        return f"""System Analysis
Hardware Components: {len(System._hardware)}
Software Components: {len(System._software)}
Total Operational Memory: {total_memory_used} / {total_memory}
Total Capacity Taken: {total_capacity_used} / {total_capacity}"""

    @staticmethod
    def system_split():
        info = ""
        for hardware in System._hardware:
            info += f"""Hardware Component - {hardware.name}
Express Software Components: {len([software for software in hardware.software_components if software.type == "Express"])}
Light Software Components: {len([software for software in hardware.software_components if software.type == "Light"])}
Memory Usage: {hardware.memory_used} / {hardware.memory}
Capacity Usage: {hardware.capacity_used} / {hardware.capacity}
Type: {hardware.type}
"""
            if not hardware.software_components:
                info += 'None'
            else:
                components_names = ", ".join([software.name for software in hardware.software_components])
                info += f"Software Components: {components_names}"
        return info
