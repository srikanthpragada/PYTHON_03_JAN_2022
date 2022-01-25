# Display all factors of the given number on command line

import sys

if len(sys.argv) < 2:
    print("Number is missing. Please run as follows:")
    print("python factors.py  <number>")
    exit()

num = int(sys.argv[1])

for n in range(2, num//2 + 1):
    if num % n == 0:
        print(n)