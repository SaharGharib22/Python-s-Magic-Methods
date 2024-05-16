# Supporting Operator Overloading in Custom Class:

# Membership Operators:

class Membership:
    def __init__(self, elements):
        self.elements = elements

    def __contains__(self, item):
        return item in self.elements


container = Membership([1, 2, 3, 4, 5, 6])
print(3 in container)
print(15 in container)
