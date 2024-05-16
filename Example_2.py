# Representing Object as Strings:

# User-Friendly String Representations With .__str__():
class Person:
    def __init__(self, name, age, phone):
        self.name = name
        self.age = age
        self.phone = phone

    def __str__(self):
        return f"Person: {self.name}, Age: {self.age}, Phone: {self.phone}"


person_1 = Person("John", 50, 9122222222)
print("__str__ Method: ", person_1)

# Developer-Friendly String Representations With .__repr__():
class Color:
    def __init__(self, suffix, title):
        self.suffix = suffix
        self.title = title

    def __repr__(self):
        return f"Color({repr(self.suffix)}, {repr(self.title)})"


c1 = Color("Bright", "Red")
c2 = eval(repr(c1))
print(f"Color", c1.title, c1.suffix)
print(f"Color", c2.title, c2.suffix)
