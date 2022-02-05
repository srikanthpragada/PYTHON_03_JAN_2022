import json

class Contact:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return f"{self.name} - {self.email}"


c = Contact("Abc", "abc@gmail.com")
json_str = json.dumps(c.__dict__)
print(json_str)

