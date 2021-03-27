"""
In this workshop, we are going to create a custom data structure,
which has similar functionalities as the Python List
and create unit tests for its functionalities.
It will have the same functionalities as the original List
and we will also add our own custom functionalities.

Do not inherit List!
Feel free to implement your own functionality (and unit tests)
or to write the methods by yourself.
"""

import sys


class List:
    """a custom data structure, which has similar functionalities as the Python List"""

    def __init__(self, *args):
        self.__list = [*args]

    def __repr__(self):
        return str(self.__list)

    def __add__(self, other):
        return self.__list + other.__list

    def __eq__(self, other):
        return len(self.__list) == len(other.__list)

    def __ge__(self, other):
        return len(self.__list) >= len(other.__list)

    def __le__(self, other):
        return len(self.__list) <= len(other.__list)

    def __len__(self):
        return len(self.__list)

    def __getitem__(self, item):
        return self.__list[item]

    @staticmethod
    def __validate_iterable(iterable):
        if not type(iterable) is list and not type(iterable) is List:
            raise TypeError(f'\'{iterable}\' is not na iterable')

    def __validate_index(self, index):
        if not type(index) is int:
            raise TypeError(f'Index cannot be \'{index.__class__.__name__}\'')
        if index not in range(len(self.__list)):
            raise IndexError(f'Index not in range ({len(self.__list)})')

    def __validate_value(self, value):
        if value not in self.__list:
            raise ValueError(f'\'{value}\' not in List')

    def append(self, value):
        """
        Adds a value to the end of the list. Returns the list.
        """
        self.__list += [value]
        return self.__list

    def remove(self, index):
        """
        Removes the value on the index. Returns the value removed.
        """
        self.__validate_index(index)
        self.__list = self.__list[:index] + self.__list[index + 1:]
        return self.__list

    def get(self, index):
        """
        Returns the value on the index.
        """
        self.__validate_index(index)
        return self.__list[index]

    def extend(self, iterable):
        """
        Appends the iterable to the list. Returns the new list.
        """
        self.__validate_iterable(iterable)
        self.__list += iterable
        return self.__list

    def insert(self, index, value):
        """
        Adds the value on the specific index. Returns the list.
        """
        self.__validate_index(index)
        self.__list = self.__list[:index] + [value] + self.__list[index:]
        return self.__list

    def pop(self):
        """
        Removes the last value and returns it.
        """
        popped = self.__list[-1]
        self.__list = self.__list[:-1]
        return popped

    def clear(self):
        """
        Removes all values, contained in the list.
        """
        self.__list = []

    def index(self, value):
        """
        Returns the index of the given value.
        """
        self.__validate_value(value)
        for index, v in enumerate(self.__list):
            if v == value:
                return index

    def count(self, value):
        """
        Returns the number of times the value is contained in the list.
        """
        self.__validate_value(value)
        counter = 0
        for v in self.__list:
            if v == value:
                counter += 1
        return counter

    def reverse(self):
        """
        Returns the values of the list in reverse order.
        """
        new_list = []
        for _ in range(len(self.__list)):
            new_list.append(self.__list.pop())
        self.__list = new_list
        return self.__list

    def copy(self):
        """
        Returns a copy (new instance) of the list.
        """
        return List(*self.__list)

    def size(self):
        """
        Returns the length of the list.
        """
        return len(self.__list)

    def add_first(self, value):
        """
        Adds the value at the beginning of the list
        """
        self.__list = [value] + self.__list
        return self.__list

    def dictionize(self):
        """
        Returns the list as a dictionary.
        The keys will be each value on an even position
        and their values will be each value on an odd position.
        If the last value on an even position, it’s value will be " " (space)
        """
        dd = {}
        for index in range(0, len(self.__list), 2):
            key = self.__list[index]
            if index == len(self.__list) - 1:
                value = ' '
            else:
                value = self.__list[index + 1]
            dd[key] = value
        return dd

    def move(self, amount):
        """
        Moves the first "amount" of values to the end of the list. Returns the list.
        """
        self.__validate_index(amount)
        for i in range(amount):
            self.__list = self.__list[1:] + [self.__list[0]]
        return self.__list

    def sum(self):
        """
        Returns the sum of the list. If the value is not a number,
        add the length of the value to the overall number.
        """
        total = 0
        for el in self.__list:
            if type(el) is int or type(el) is float:
                total += el
            elif not el:
                continue
            else:
                total += len(el)
        return total

    def overbound(self):
        """Returns the index of the biggest value. If the value is not a number, check it’s length."""
        biggest_el = -sys.maxsize
        biggest_index = 0
        for index, el in enumerate(self.__list):
            if type(el) is int or type(el) is float:
                if el > biggest_el:
                    biggest_el = el
                    biggest_index = index
            elif not el:
                continue
            else:
                if len(el) > biggest_el:
                    biggest_el = len(el)
                    biggest_index = index
        return biggest_index

    def underbound(self):
        """Returns the index of the smallest value. If the value is not a number, check it’s length."""
        smallest_el = sys.maxsize
        smallest_index = 0
        for index, el in enumerate(self.__list):
            if type(el) is int or type(el) is float:
                if el < smallest_el:
                    smallest_el = el
                    smallest_index = index
            elif not el:
                continue
            else:
                if len(el) < smallest_el:
                    smallest_el = len(el)
                    smallest_index = index
        return smallest_index

# ll = List('a', 1, 1, 1, None)
# print(ll)
# ll.append(10)
# print(ll.append(42))
# print(ll.remove(0))
# l2 = List('a')
# l3 = l2 + ll
# print(l3)
# for i in enumerate(ll):
#     print(i)
# print(l2.insert(0, 42))
# print(ll.pop())
# print(l2.index(42))
# print(ll.count(1))
# print(ll)
# print(ll.reverse())
#
# llll = ll.copy()
# print(id(ll) == id(llll))
# print(ll.underbound())
# print(ll.sum())
# print(ll.move(2))
# dd = ll.dictionize()
# print(dd)
