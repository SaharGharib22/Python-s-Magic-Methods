# Supporting Operator Overloading in Custom Class:

# Augmented Assignment Operators:

class Augmented:
    def __init__(self, value):
        self.value = value

    def __iadd__(self, other):
        self.value += other
        return self

    def __isub__(self, other):
        self.value -= other
        return self

    def __imul__(self, other):
        self.value *= other
        return self

    def __itruediv__(self, other):
        self.value /= other
        return self

    def __ifloordiv__(self, other):
        self.value //= other
        return self

    def __imod__(self, other):
        self.value %= other
        return self

    def __ipow__(self, other):
        self.value **= other
        return self


number_1 = Augmented(10)
number_2 = 5

# Result:
number_1 += number_2
print("After +=", number_1.value)
number_1 -= number_2
print("After -=", number_1.value)
number_1 *= number_2
print("After *=", number_1.value)
number_1 /= number_2
print("After /=", number_1.value)
number_1 //= number_2
print("After //=", number_1.value)
number_1 %= number_2
print("After %=", number_1.value)
number_1 **= number_2
print("After **=", number_1.value)
