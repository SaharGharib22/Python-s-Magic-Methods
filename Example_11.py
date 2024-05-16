# Introspecting Object:

# __dir__():
class Object:
    def __init__(self):
        self.value = 4

    @staticmethod
    def func():
        return "Hello World!"


obj = Object()
print("Result of __dir__:")
print(dir(obj))

# __hasattr__():
class Person:
    def __init__(self, name):
        self.name = name


p = Person("John")
print("\nResult of __hasattr__:")
print(hasattr(p, "name"))
print(hasattr(p, "age"))

# __isinstancecheck__():
class NumberMeta(type):
    def __instancecheck__(self, instance):
        return isinstance(instance, int) or isinstance(instance, Number)

class Number(metaclass=NumberMeta):
    def __init__(self, value):
        self.value = value


num = Number(10)
print("\nResult of __instancecheck__:")
print(isinstance(num, Number))
print(isinstance(num, int))

# __sunclasscheck__():
class First:
    pass

class Second(First):
    pass


print("\nResult of __sunclasscheck__:")
print(issubclass(Second, First))
print(issubclass(First, Second))
