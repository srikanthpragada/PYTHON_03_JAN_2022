class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other) -> bool:
        return self.name == other.name and self.price == other.price

    def __str__(self) -> str:
        return f"{self.name} - {self.price}"

    def __gt__(self, other) -> bool:
        return self.price > other.price


p1 = Product("A", 1000)
p2 = Product("A", 1000)
p3 = Product("B", 500)

products = [p1, p2, p3]

print(p1 == p2)  # p1.__eq__(p2)
print(p1)  # str(p1) ->   p1.__str__()
#print(p3 > p1)  # p3.__gt__(p1)

for p in sorted(products):
    print(p)
