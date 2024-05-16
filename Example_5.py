# Supporting Operator Overloading in Custom Class:

# Unary Operators:
class Unary:
    def __init__(self, value):
        self.value = value

    def __neg__(self):
        return -self.value

    def __pos__(self):
        return +self.value

    def __abs__(self):
        return abs(self.value)

    def __invert__(self):
        return ~self.value

    def __round__(self, n=None):
        return round(self.value, n)


number = Unary(7)

# Perform Unary Operators:
neg_result = - number
pos_result = + number
abs_result = abs(number)
invert_result = ~ number
round_result = round(number)


# Print Result:
print(f"Initial Value: {number.value}")
print(f"Negative: {neg_result}")
print(f"Positive: {pos_result}")
print(f"Absolute Value: {abs_result}")
print(f"Bitwise Inversion: {invert_result}")
print(f"Round: {round_result}")
