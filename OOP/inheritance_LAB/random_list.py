class RandomList(list):
    def append(self, el):
        return list.append(self, el)

    def get_random_element(self):
        return list.pop(self)


# test first zero
import unittest
from unittest import mock


class RandomListTests(unittest.TestCase):
    def test_zero_first(self):
        mocked_choice = lambda x: 5
        with mock.patch('random.choice', mocked_choice):
            li = RandomList()
            li.append(4)
            li.append(3)
            li.append(5)
            self.assertEqual(li.get_random_element(), 5)


if __name__ == '__main__':
    unittest.main()
