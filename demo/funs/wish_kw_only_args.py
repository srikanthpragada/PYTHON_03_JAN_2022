# keyword-only arguments
def wish(*, message, name):
    print(message, name)


# wish("Anders", "Hi")  # Positional Args
wish(message="Hello", name="Mark")  # Keyword Args
