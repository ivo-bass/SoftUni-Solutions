from unittest import TestCase, main

from project.hardware.hardware import Hardware
from project.software.software import Software


class HardwareTest(TestCase):
    name = 'name'
    type = 'type'
    capacity = 100
    memory = 100

    def setUp(self) -> None:
        self.hw = Hardware(
            name=self.name,
            type=self.type,
            capacity=self.capacity,
            memory=self.memory
        )

    def test_init(self):
        self.assertEqual(self.name, self.hw.name)
        self.assertEqual(self.type, self.hw.type)
        self.assertEqual(self.capacity, self.hw.capacity)
        self.assertEqual(self.memory, self.hw.memory)
        self.assertEqual([], self.hw.software_components)

    def test_install__with_valid_software__should_add_to_list(self):
        software = Software('s_name', 's_type', capacity_consumption=10, memory_consumption=10)
        self.hw.install(software)
        self.assertIn(software, self.hw.software_components)

    def test_install__with_not_enough_capacity__should_raise_exception(self):
        software = Software('s_name', 's_type', capacity_consumption=200, memory_consumption=10)
        with self.assertRaises(Exception) as exc:
            self.hw.install(software)
        msg = "Software cannot be installed"
        self.assertEqual(msg, str(exc.exception))

    def test_install__with_not_enough_memory__should_raise_exception(self):
        software = Software('s_name', 's_type', capacity_consumption=10, memory_consumption=200)
        with self.assertRaises(Exception) as exc:
            self.hw.install(software)
        msg = "Software cannot be installed"
        self.assertEqual(msg, str(exc.exception))

    def test_uninstall(self):
        software = Software('s_name', 's_type', capacity_consumption=10, memory_consumption=10)
        self.hw.install(software)
        self.hw.uninstall(software)
        self.assertNotIn(software, self.hw.software_components)
        # also should remove software from System._software


if __name__ == '__main__':
    main()
