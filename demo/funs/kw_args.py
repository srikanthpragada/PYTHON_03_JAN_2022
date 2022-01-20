def print_details(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


def details(*args, **kwargs):
    print(args)
    print(kwargs)


print_details(name="Tom", email='tom@gmail.com')
print_details(name="Scott", age=20, gender='M')

details(10, 20, name='Mark')
