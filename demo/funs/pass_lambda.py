def mathop(a, b, operation):
    print(type(operation), id(operation))
    print(operation(a, b))


mathop(10, 20, lambda a, b: a + b)
mathop(10, 20, lambda a, b: a * b)
