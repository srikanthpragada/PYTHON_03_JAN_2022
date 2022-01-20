def wish(*names, message='Hi') -> None:
    for n in names:
        print(message, n)


wish("Anders", "Mark", message="Hello")
wish("Tom", "Martin", "David")
