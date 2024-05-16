# Supporting Operator Overloading in Custom Class:

# Comparison Operator Methods:

class Comparison:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value < other

    def __gt__(self, other):
        return self.value > other

    def __le__(self, other):
        return self.value <= other

    def __ge__(self, other):
        return self.value >= other

    def __eq__(self, other):
        return self.value == other

    def __ne__(self, other):
        return self.value != other


number_1 = Comparison(10)
number_2 = Comparison(15)

# Perform Comparison Operators:
lt_result = number_1 < number_2
gt_result = number_1 > number_2
le_result = number_1 <= number_2
ge_result = number_1 >= number_2
eq_result = number_1 == number_2
ne_result = number_1 != number_2


# Print Result:
print("Initial Values: 10 , 15")
print(f"Less Than : {lt_result}")
print(f"Greater Than: {gt_result}")
print(f"Less than or Equal to: {le_result}")
print(f"Greater Than or Equal to: {ge_result}")
print(f"Equal To: {eq_result}")
print(f"Not Equal To: {ne_result}")
