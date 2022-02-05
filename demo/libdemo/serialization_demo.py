import pickle
import json

class Contact:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return f"{self.name} - {self.email}"


c = Contact("Abc", "abc@gmail.com")
f = open("contact.pickle", "wb")
pickle.dump(c,f);
f.close()

