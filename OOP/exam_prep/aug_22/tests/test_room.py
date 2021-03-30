import unittest


from project.people.child import Child
from project.rooms.room import Room


class TestRoom(unittest.TestCase):
    def setUp(self) -> None:
        self.r = Room('a', 12.2, 2)
        self.child_one = Child(5, 1, 2, 1)
        self.child_two = Child(3, 2)

    def test_init(self):
        self.assertEqual(self.r.family_name, 'a')
        self.assertEqual(self.r.budget, 12.2)
        self.assertEqual(self.r.members_count, 2)
        self.assertEqual(self.r.children, [])
        self.assertEqual(self.r.expenses, 0)

    def test_invalid_expenses(self):
        try:
            self.r.expenses = -1
        except Exception:
            self.assertRaises(ValueError)

    def test_calculate_expenses(self):
        self.r.children.append(self.child_one)
        self.r.children.append(self.child_two)
        self.r.calculate_expenses(self.r.children)
        self.assertEqual(self.r.expenses, 420)


if __name__ == '__main__':
    unittest.main()
