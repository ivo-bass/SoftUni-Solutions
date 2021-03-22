def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def get_primes(ll):
    for num in ll:
        if is_prime(num):
            yield num


# print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))