class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return (f'{self.name} has saved {self.money} money.')


import unittest


class WorkerTest(unittest.TestCase):
    def setUp(self) -> None:
        self.w = Worker('a', 100, 100)

    def test_worker_init(self):
        self.assertEqual(self.w.name, 'a')
        self.assertEqual(self.w.salary, 100)
        self.assertEqual(self.w.energy, 100)

    def test_if_rest_increments_energy(self):
        old_energy = self.w.energy
        self.w.rest()
        self.assertEqual(self.w.energy - old_energy, 1)

    def test_work_with_zero_energy(self):
        self.w.energy = 0
        with self.assertRaises(Exception):
            self.w.work()

    def test_work_with_negative_energy(self):
        self.w.energy = -1
        with self.assertRaises(Exception):
            self.w.work()

    def test_if_money_is_increased_after_work(self):
        old_money = self.w.money
        self.w.work()
        self.assertEqual(self.w.money - old_money, self.w.salary)

    def test_if_energy_is_decreased_after_work(self):
        old_energy = self.w.energy
        self.w.work()
        self.assertEqual(old_energy - self.w.energy, 1)

    def test_get_info(self):
        exp = "a has saved 0 money."
        res = self.w.get_info()
        self.assertEqual(res, exp)


if __name__ == '__main__':
    unittest.main()
