def iseven(n):
    return n % 2 == 0


nums = [99, 56, 44, 55, 343]

for n in filter(iseven, nums):
    print(n)

for n in filter(lambda v: v % 2 == 0, nums):
    print(n)

for n in filter(lambda v: v > 0, [9, -4, 99, -8, 34]):
    print(n)

for n in filter(lambda v: len(v) == 3, ['abc', 'xyz', 'bc', 'a', 'err']):
    print(n)
