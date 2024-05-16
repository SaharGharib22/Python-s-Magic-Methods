# Supporting Operator Overloading in Custom Class:

# Arithmetic Operators:
class Arithmetic:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other

    def __sub__(self, other):
        return self.value - other

    def __mul__(self, other):
        return self.value * other

    def __truediv__(self, other):
        return self.value / other

    def __floordiv__(self, other):
        return self.value // other

    def __mod__(self, other):
        return self.value % other

    def __pow__(self, other):
        return self.value ** other


number = Arithmetic(9)

# Perform Arithmetic Operators:
add_result = number + 5
sub_result = number - 3
mul_result = number * 2
div_result = number / 4
floor_result = number // 6
mod_result = number % 7
pow_result = number ** 8

# Print Result:
print(f"Initial Value: {number.value}")
print(f"Addition: {add_result}")
print(f"Subtraction: {sub_result}")
print(f"Multiplication: {mul_result}")
print(f"Division: {div_result}")
print(f"Floor Division: {floor_result}")
print(f"Modulo: {mod_result}")
print(f"Exponentiation: {pow_result}")
