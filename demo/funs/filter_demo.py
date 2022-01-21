def hasupper(s: str) -> bool:
    for c in s:
        if c.isupper():
            return True

    return False


names = ['java', 'JavaScript', 'c#', 'Sql']
uppernames = filter(hasupper, names)
for n in uppernames:
    print(n)
