# Supporting Operator Overloading in Custom Class:

# Augmented Bitwise Operators:

class Bitwise:
    def __init__(self, value):
        self.value = value

    def __iand__(self, other):
        self.value &= other
        return self

    def __ior__(self, other):
        self.value |= other
        return self

    def __ixor__(self, other):
        self.value ^= other
        return self

    def __ilshift__(self, other):
        self.value <<= other
        return self

    def __irshift__(self, other):
        self.value >>= other
        return self


number_1 = Bitwise(12)
number_2 = 8

# Result:
number_1 &= number_2
print("After &=", number_1.value)
number_1 |= number_2
print("After |=", number_1.value)
number_1 ^= number_2
print("After ^=", number_1.value)
number_1 <<= number_2
print("After <<=", number_1.value)
number_1 >>= number_2
print("After >>=", number_1.value)
