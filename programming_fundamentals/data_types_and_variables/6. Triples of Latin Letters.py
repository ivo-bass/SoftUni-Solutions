n = int(input())

for ch1 in range(n):
    for ch2 in range(n):
        for ch3 in range(n):
            print(f"{chr(97+ch1)}"
                  f"{chr(97+ch2)}"
                  f"{chr(97+ch3)}")
