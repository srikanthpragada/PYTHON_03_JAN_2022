def numbers():
    for n in range(1, 11):
        yield n


g = numbers()
print(g)
print(next(g), next(g))  # 1 2
# Print from 3
for v in g:
    print(v)
