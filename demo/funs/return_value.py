def add(a, b):
    return a + b

def count_digits(s):
    count = 0
    for c in s:
        if c.isdigit():
            count += 1

    return count


def isprime(n):
    for i in range(2, n//2 + 1):
        if n % i == 0:
            return False # not prime

    return True    # prime


total = add(134330, 212340)
print(total)
print(add("abc", "xyz"))

print( count_digits("Abc123"))

if isprime(123):
    print("Prime")
else:
    print("Not prime")

