def recursive_power(num, power):
    if power == 1:
        return num
    num *= recursive_power(num, power-1)
    return num


print(recursive_power(2, 10))
