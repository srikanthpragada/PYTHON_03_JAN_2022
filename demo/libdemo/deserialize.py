import pickle

class Contact:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return f"{self.name} - {self.email}"

f = open("contact.pickle", "rb")
c = pickle.load(f);
f.close()
print(c)

