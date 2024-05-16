# Controlling the Object Creation Process

# Initializing Object With .__init__():
class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.area = 3.14 * radius * radius


circle_1 = Circle(5)
print("Area of circle is: ", circle_1.area)


# Creating Object with .__new__():
class Square:
    def __new__(cls, side_length):
        instance = super(Square, cls).__new__(cls)
        instance.side_length = side_length
        return instance

    def calculate_area(self):
        return self.side_length ** 2


side_length = 5
square = Square(side_length)
area = square.calculate_area()
print("Area of Square is: ", area)
