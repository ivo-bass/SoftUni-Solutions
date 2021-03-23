import unittest


from project.people.child import Child
from project.rooms.room import Room


class TestRoom(unittest.TestCase):
    def test_init(self):
        r = Room('a', 12.2, 2)
        self.assertEqual(r.family_name, 'a')
        self.assertEqual(r.budget, 12.2)
        self.assertEqual(r.members_count, 2)
        self.assertEqual(r.children, [])
        self.assertEqual(r.expenses, 0)

    def test_invalid_expenses(self):
        r = Room('a', 12.2, 2)
        try:
            r.expenses = -1
        except ValueError:
            self.assertRaises(ValueError)

    def test_calculate_expenses(self):
        child_one = Child(5, 1, 2, 1)
        child_two = Child(3, 2)
        r = Room("Peterson", 600, 520)
        r.children.append(child_one)
        r.children.append(child_two)
        r.calculate_expenses(r.children)
        self.assertEqual(r.expenses, 420)


if __name__ == '__main__':
    unittest.main()
