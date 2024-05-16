# Handling Setup and Teardown with Context Manager:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __enter__(self):
        print(f"Entering context: {self.name}, {self.age}")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Exiting context: {self.name}, {self.age}")


with Person("Harry", 40) as person:
    print(f"Inside context: {person.name}, {person.age}")

print("Outside context")
