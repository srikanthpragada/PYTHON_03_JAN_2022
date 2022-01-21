def mathop(a, b, operation):
    print(operation(a, b))


def add(a, b):
    return a + b


def mul(a, b):
    return a * b


mathop(10, 20, add)
mathop(10, 20, len)
