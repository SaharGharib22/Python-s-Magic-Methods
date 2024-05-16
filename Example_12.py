# Controlling Attribute Access:

class Controlling:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __getattribute__(self, name):
        print(f"Accessing Attribute: {name}")
        return super().__getattribute__(name)

    def __getattr__(self, name):
        return f"Attribute '{name}' doesn't exist"

    def __setattr__(self, name, value):
        print(f"Setting Attribute: {name} = {value}")
        super().__setattr__(name, value)

    def __delattr__(self, name):
        if name in self.__dict__:
            del self.__dict__[name]
            print(f"Deleted Attribute: {name}")
        else:
            print(f"Attribute {name} doesn't exist")


p = Controlling("Ali", 30)

print(p.name)
print(p.age)
print(p.address)
p.address = "Tehran"
p.age = 31
del p.name
del p.phone
print(p.name)
