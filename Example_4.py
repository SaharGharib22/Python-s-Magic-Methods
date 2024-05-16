# Supporting Operator Overloading in Custom Class:

# Right-Hand Arithmetic Operators:

class RHArithmetic:
    def __init__(self, value):
        self.value = value

    def __radd__(self, other):
        return self.value + other

    def __rsub__(self, other):
        return self.value - other

    def __rmul__(self, other):
        return self.value * other

    def __rtruediv__(self, other):
        return self.value / other

    def __rfloordiv__(self, other):
        return self.value // other

    def __rmod__(self, other):
        return self.value % other

    def __rpow__(self, other):
        return self.value ** other


number = RHArithmetic(10)

# Perform Right-Hand Arithmetic Operators:
add_result = 2 + number
sub_result = 3 - number
mul_result = 4 * number
div_result = 5 / number
floor_result = 6 // number
mod_result = 7 % number
pow_result = 8 ** number

# Print Result:
print(f"Initial Value: {number.value}")
print(f"Addition: {add_result}")
print(f"Subtraction: {sub_result}")
print(f"Multiplication: {mul_result}")
print(f"Division: {div_result}")
print(f"Floor Division: {floor_result}")
print(f"Modulo: {mod_result}")
print(f"Exponentiation: {pow_result}")
