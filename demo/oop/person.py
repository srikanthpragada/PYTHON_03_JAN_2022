class Person:
    def __init__(self, name, age):
        # Private attributes
        self.__name = name
        self.__age = age


p = Person("Jack", 20)
print(p.__dict__)
# p._Person__name = "Mark"
# print(p._Person__name)
