# Supporting Operator Overloading in Custom Class:

# Bitwise Operators:

class Bitwise:
    def __init__(self, value):
        self.value = value

    def __and__(self, other):
        return self.value & other.value

    def __or__(self, other):
        return self.value | other.value

    def __xor__(self, other):
        return self.value ^ other.value

    def __lshift__(self, other):
        return self.value << other.value

    def __rshift__(self, other):
        return self.value >> other.value

    def __invert__(self):
        return ~ self.value


a = Bitwise(4)
b = Bitwise(9)

# Print Result:
print("Bitwise AND:", a & b)
print("Bitwise OR:", a | b)
print("Bitwise XOR:", a ^ b)
print("Bitwise NOT", ~a)
print("Left Shift:", a << b)
print("Right Shift", a >> b)
