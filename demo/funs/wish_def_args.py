def wish(name="Guest", message="Hi"):
    print(message, name)


wish()
wish(message="Hello")
wish("Anders")  # Positional Args
wish(message="Hello", name="Mark")  # Keyword Args
wish("Jason", "Good Morning")
