from unittest import TestCase, main

from .custom_list import List


class ListTest(TestCase):
    def setUp(self) -> None:
        self.ll = List(1, 2, 3)

    def test_init(self):
        self.assertEqual([1, 2, 3], self.ll)

    def test_repr(self):
        self.assertEqual('[1, 2, 3]', str(self.ll))

    def test_len(self):
        self.assertEqual(3, len(self.ll))

    def test_getitem(self):
        self.assertEqual(3, self.ll[2])

    def test_add_instances(self):
        l2 = List(42)
        l3 = self.ll + l2
        self.assertEqual([1, 2, 3, 42], l3)

    def test_append__should_add_the_value_and_return_the_list(self):
        result = self.ll.append(42)
        self.assertEqual([1, 2, 3, 42], result)

    def test_remove__with_valid_index__should_remove_and_return_the_value(self):
        result = self.ll.remove(2)
        self.assertEqual([1, 2], self.ll)
        self.assertEqual(3, result)

    def test_remove__with_invalid_index__should_raise_index_error(self):
        with self.assertRaises(IndexError):
            self.ll.remove(10)

    def test_remove__with_index_not_int__should_raise_type_error(self):
        with self.assertRaises(TypeError):
            self.ll.remove('10')

    def test_get__should_return_the_value(self):
        result = self.ll.get(2)
        self.assertEqual(3, result)

    def test_get__with_invalid_index__should_raise_index_error(self):
        with self.assertRaises(IndexError):
            self.ll.get(10)

    def test_get__with_index_not_int__should_raise_type_error(self):
        with self.assertRaises(TypeError):
            self.ll.get('10')

    def test_extend__should_add_iterable_and_return_the_list(self):
        result = self.ll.extend('asd')
        self.assertEqual([1, 2, 3, 'a', 's', 'd'], result)

    def test_extend__with_invalid_iterable__should_raise_type_error(self):
        with self.assertRaises(TypeError):
            self.ll.extend(101)

    def test_insert_add_the_value_returns_the_list(self):
        result = self.ll.insert(0, 42)
        self.assertEqual([42, 1, 2, 3], result)

    def test_insert__with_invalid_index__should_raise_index_error(self):
        with self.assertRaises(IndexError):
            self.ll.insert(10, 10)

    def test_insert__with_index_not_int__should_raise_type_error(self):
        with self.assertRaises(TypeError):
            self.ll.insert('10', '10')

    def test_pop__should_remove_and_return_the_last_value(self):
        result = self.ll.pop()
        self.assertEqual(3, result)
        self.assertEqual([1, 2], self.ll)

    def test_clear__should_return_empty_list(self):
        self.ll.clear()
        self.assertEqual([], self.ll)

    def test_index__should_return_value_of_index(self):
        result = self.ll.index(3)
        self.assertEqual(2, result)

    def test_index__with_invalid_value__should_raise_value_error(self):
        with self.assertRaises(ValueError):
            self.ll.index(101)

    def test_count__should_return_count_of_value_in_list(self):
        self.ll.append(1)
        result = self.ll.count(1)
        self.assertEqual(2, result)

    def test_count_with_invalid_value__should_raise_value_error(self):
        with self.assertRaises(ValueError):
            self.ll.count(101)

    def test_reverse__should_return_the_reversed_list(self):
        result = self.ll.reverse()
        self.assertEqual([3, 2, 1], result)

    def test_copy__should_retunr_new_instance_of_the_list_with_same_elements(self):
        l2 = self.ll.copy()
        self.assertNotEqual(id(l2), id(self.ll))
        self.assertEqual(l2, self.ll)

    def test_size__should_return_the_length(self):
        result = self.ll.size()
        self.assertEqual(3, result)

    def test_add_first__should_append_left_the_value(self):
        result = self.ll.add_first(42)
        self.assertEqual([42, 1, 2, 3], result)

    def test_dictionize__should_return_the_list_as_dict(self):
        result = self.ll.dictionize()
        self.assertDictEqual({1: 2, 3: ' '}, result)

    def test_move__should_move_the_first_n_elements_to_the_end(self):
        result = self.ll.move(2)
        self.assertEqual([3, 1, 2], result)

    def test_move__with_invalid_amount__should_raise_index_error(self):
        with self.assertRaises(IndexError):
            self.ll.move(10)

    def test_move__with_amount_not_int__should_raise_type_error(self):
        with self.assertRaises(TypeError):
            self.ll.move('10')

    def test_sum__with_ints__should_sum_the_values(self):
        result = self.ll.sum()
        self.assertEqual(6, result)

    def test_sum__with_strings__should_sum_the_lengths(self):
        ll = List('asd', 'asd', 3)
        result = ll.sum()
        self.assertEqual(9, result)

    def test_sum__with_None__should_skip_None(self):
        ll = List('asd', 'asd', None, 3, '')
        result = ll.sum()
        self.assertEqual(9, result)

    def test_overbound__should_return_the_index_of_the_max_value_of_ints(self):
        result = self.ll.overbound()
        self.assertEqual(2, result)

    def test_overbound__should_return_the_index_of_the_max_len_of_strings(self):
        ll = List('asd', 'asdasd', 3)
        result = ll.overbound()
        self.assertEqual(1, result)

    def test_overbound__shoud_skip_None(self):
        ll = List('asd', 'asdasd', None, 3, '')
        result = ll.overbound()
        self.assertEqual(1, result)

    def test_underbound__should_return_the_index_of_the_max_value_of_ints(self):
        result = self.ll.underbound()
        self.assertEqual(0, result)

    def test_underbound__should_return_the_index_of_the_max_len_of_strings(self):
        ll = List('asd', 'asdasd', 42)
        result = ll.underbound()
        self.assertEqual(0, result)

    def test_underbound__should_skip_None(self):
        ll = List('asd', 'asdasd', None, 42, '')
        result = ll.underbound()
        self.assertEqual(0, result)


if __name__ == '__main__':
    main()
