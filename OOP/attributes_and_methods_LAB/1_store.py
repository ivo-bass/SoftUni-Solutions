class Store:
    def __init__(self, name: str, type: str, capacity: int):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items = {}  # {name: quantity}

    @classmethod
    def from_size(cls, name: str, type: str, size: int):
        return Store(name, type, size // 2)

    def add_item(self, item_name: str):
        # TODO: If the addition is not possible, the following message
        #  should be returned "Not enough capacity in the store"
        if item_name not in self.items:
            self.items[item_name] = 0
        self.items[item_name] += 1
        return f"{item_name} added to the store"

    def remove_item(self, item_name: str, amount: int):
        if item_name not in self.items or self.items[item_name] < amount:
            return f"Cannot remove {amount} {item_name}"
        self.items[item_name] -= amount
        return f"{amount} {item_name} removed from the store"

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"


import unittest


class StoreTests(unittest.TestCase):
    def setUp(self):
        self.store = Store("First Store", "Best Type", 5)

    def test_from_size_should_create_class(self):
        store = Store.from_size("Test", "Test Type", 20)
        self.assertEqual(store.name, "Test")
        self.assertEqual(store.type, "Test Type")
        self.assertEqual(store.capacity, 10)
        self.assertEqual(store.items, {})

    def test_add_item_success(self):
        result = self.store.add_item("tomato")
        self.assertEqual(self.store.items["tomato"], 1)
        self.assertEqual(result, "tomato added to the store")

    def test_remove_item_success(self):
        self.store.add_item("tomato")
        result = self.store.remove_item("tomato", 1)
        self.assertEqual(result, "1 tomato removed from the store")

    def test_remove_item_success(self):
        self.store.add_item("tomato")
        result = self.store.remove_item("tomato", 1)
        self.assertEqual(result, "1 tomato removed from the store")

    def test_remove_item_unsuccessful(self):
        self.store.add_item("tomato")
        result = self.store.remove_item("tomato", 2)
        self.assertEqual(result, "Cannot remove 2 tomato")

    def test_repr(self):
        self.assertEqual(repr(self.store), "First Store of type Best Type with capacity 5")


if __name__ == "__main__":
    unittest.main()
