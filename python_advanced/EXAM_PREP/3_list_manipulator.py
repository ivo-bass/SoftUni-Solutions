def list_manipulator(nums, *args):
    action, location, *values = args
    if action == 'add':
        if location == 'beginning':
            nums = values + nums
        else:
            nums = nums + values
    else:
        if location == 'beginning':
            if values:
                for _ in range(values[0]):
                    nums.pop(0)
            else:
                nums.pop(0)
        else:
            if values:
                for _ in range(values[0]):
                    nums.pop()
            else:
                nums.pop()
    return nums


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
