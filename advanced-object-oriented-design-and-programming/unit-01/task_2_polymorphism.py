"""Unit 1, Task 2: Polymorphism using abstract shapes."""

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


if __name__ == "__main__":
    shapes = [Circle(3), Rectangle(4, 5)]
    for shape in shapes:
        print(f"{type(shape).__name__} area: {shape.area():.2f}")
