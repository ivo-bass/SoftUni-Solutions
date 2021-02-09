def numbers_searching(*args):
    numbers = list(sorted(args))
    min_number = numbers[0]
    max_number = numbers[-1]
    missing_num = None
    for num in range(min_number, max_number + 1):
        if num not in numbers:
            missing_num = num
    duplicates_dict = {num: args.count(num) for num in numbers if numbers.count(num) > 1}
    duplicates_sorted_list = list(duplicates_dict.keys())
    return [missing_num, duplicates_sorted_list]


print(numbers_searching(1, 2, 4, 2, 3, 5, 4, 7))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
