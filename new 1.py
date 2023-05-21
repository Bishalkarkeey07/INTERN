import abc
class Shape(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def calculate_area(self):
        pass

    @abc.abstractmethod
    def calculate_perimeter(self):
        pass
class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def calculate_area(self):
        return self.height * self.width 

    def calculate_perimeter(self):
        return 2 * (self.height + self.width) 

class Square(Shape):
    def __init__(self, width):
        self.width = width

    def calculate_area(self):
        return self.width ** 2

    def calculate_perimeter(self):
        return 4 * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius

    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius
    
width = float(input("Enter the width of the rectangle: "))
height = float(input("Enter the height of the rectangle: "))

rectangle = Rectangle(height, width)
area = rectangle.calculate_area()
perimeter = rectangle.calculate_perimeter()

print("Rectangle Area:", area)
print("Rectangle Perimeter:", perimeter)
