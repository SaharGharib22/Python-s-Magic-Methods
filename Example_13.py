# Managing Attributes Through Descriptors:

class Name:
    def __init__(self):
        self._name = None

    def __get__(self, instance, owner):
        print(f"Getting attribute '{self.attr_name}'")
        return self._name

    def __set__(self, instance, value):
        print(f"Setting attribute '{self.attr_name}' to '{value}'")
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        self._name = value

    def __delete__(self, instance):
        print(f"Deleting attribute '{self.attr_name}'")
        self._name = None

    def __set_name__(self, owner, name):
        self.attr_name = name
        print(f"Descriptor assigned to {name} in class {owner.__name__}")

class Person:
    name = Name()

    def __init__(self, name):
        self.name = name


p = Person("John")
print(p.name)

p.name = "Harry"
print(p.name)

del p.name
print(p.name)
