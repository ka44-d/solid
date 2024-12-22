from abc import ABC, abstractmethod
import math

# 1. Single Responsibility Principle (SRP)

class Circle:
    def __init__(self, radius):
        self.radius = radius


class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width


# 2. Open/Closed Principle (OCP)

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class CircleShape(Shape):
    
    def __init__(self, circle: Circle):
        self.circle = circle

    def calculate_area(self):
        return math.pi * self.circle.radius ** 2


class RectangleShape(Shape):

    def __init__(self, rectangle: Rectangle):
        self.rectangle = rectangle

    def calculate_area(self):
        return self.rectangle.length * self.rectangle.width


# 3. Liskov Substitution Principle (LSP)
def print_area(shape: Shape):
    
    print(f"Area: {shape.calculate_area():.2f}")


# 4. Interface Segregation Principle (ISP)
class Perimeter(ABC):

    @abstractmethod
    def calculate_perimeter(self):
        pass


class CirclePerimeter(CircleShape, Perimeter):
  
    def calculate_perimeter(self):
        return 2 * math.pi * self.circle.radius


class RectanglePerimeter(RectangleShape, Perimeter):

    def calculate_perimeter(self):
        return 2 * (self.rectangle.length + self.rectangle.width)


# 5. Dependency Inversion Principle (DIP)
class ShapeService:
 
    def __init__(self, shape: Shape):
        self.shape = shape

    def display_area(self):
        print(f"Shape Area: {self.shape.calculate_area():.2f}")


# Demonstrating the SOLID principles with shapes
circle = Circle(radius=5)
rectangle = Rectangle(length=10, width=4)

# Area calculations
circle_shape = CircleShape(circle)
rectangle_shape = RectangleShape(rectangle)

print_area(circle_shape)  # Area of the circle
print_area(rectangle_shape)  # Area of the rectangle

# Perimeter calculations
circle_perimeter = CirclePerimeter(circle)
rectangle_perimeter = RectanglePerimeter(rectangle)

print(f"Circle Perimeter: {circle_perimeter.calculate_perimeter():.2f}")
print(f"Rectangle Perimeter: {rectangle_perimeter.calculate_perimeter():.2f}")

# Using ShapeService
shape_service = ShapeService(circle_shape)
shape_service.display_area()
