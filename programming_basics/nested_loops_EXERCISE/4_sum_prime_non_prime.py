command = input()

prime_sum = 0
non_prime_sum = 0

while command != 'stop':
    number = int(command)
    is_prime = True
    if number > 0:
        for i in range(2, number//2+1):
            if number % i == 0:
                non_prime_sum += number
                is_prime = False
                break
        if is_prime:
            prime_sum += number
    elif number == 0:
        non_prime_sum += number
    else:
        print("Number is negative.")
    command = input()

print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non prime numbers is: {non_prime_sum}")
