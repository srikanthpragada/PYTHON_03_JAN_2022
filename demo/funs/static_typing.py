# use mypy to type check

def add(a: int, b: int) -> int:
    return a + b


print(add(10, 20))
print(add("Abc", "Xyz"))
