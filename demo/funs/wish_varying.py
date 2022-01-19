def wish(*names) -> None:
    for n in names:
        print('Hello', n)


wish("Anders", "Mark")
wish("Tom", "Martin", "David")
