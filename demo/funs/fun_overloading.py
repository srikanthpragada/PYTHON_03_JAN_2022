# Overloading

def add(a, b):
    return a + b


print(id(add))
add2 = add


def add(a, b, c):
    return a + b + c


print(id(add))

print(add2(10, 20))
print(add(1, 2, 3))
