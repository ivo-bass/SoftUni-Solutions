class Stack(list):
    def __init__(self):
        super().__init__()
        self.data = list()

    def __str__(self):
        return f'[{", ".join([el for el in self.data])}]'

    def push(self, item: str):
        self.data = [item] + self.data

    def pop(self):
        return self.data.pop(0)

    def peek(self):
        return self.data[0]

    def is_empty(self) -> bool:
        return len(self.data) == 0


# test zero
import unittest


class StackTests(unittest.TestCase):
    def test_zero(self):
        stack = Stack()
        stack.push("apple")
        stack.push("carrot")
        self.assertEqual(str(stack), '[carrot, apple]')
        self.assertEqual(stack.pop(), 'carrot')
        self.assertEqual(stack.peek(), 'apple')
        stack.push("cucumber")
        self.assertEqual(str(stack), '[cucumber, apple]')
        self.assertEqual(stack.is_empty(), False)


if __name__ == '__main__':
    unittest.main()
