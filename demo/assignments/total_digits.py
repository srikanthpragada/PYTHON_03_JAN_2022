# Take a number on command line and display single digit sum

import sys

num = int(sys.argv[1])

total = 0

while True:
    while num > 0:
        total += num % 10
        num //= 10  # num = num // 10

    if total < 10:
        break

    num = total
    total = 0

print(total)
