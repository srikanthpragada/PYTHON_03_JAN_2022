# Print numbers with digits total 9

for n in range(100, 200):
    total = 0
    num = n
    while num > 0:
        total += num % 10
        num //= 10  # n = n // 10

    if total == 9:
        print(n)
