# positional-only arguments
def wish(name, message="Hi", /):
    print(message, name)


wish("Anders", "Hello")  # Positional Args
wish("Martin")
# wish(message="Hello", name="Mark")  # Keyword Args
