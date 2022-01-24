def zero(n):
    print(id(n))
    n = 0
    print(id(n))


def prepend(lst, value):
    lst.insert(0, value)


# immutable
a = 100
print(id(a))
zero(a)
print(a)

# mutable
l = [1, 2, 3]
prepend(l, 5)
print(l)
