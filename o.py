from abc import ABC, abstractmethod
from dataclasses import dataclass
import math
# Open-Closed Principle

class Shape(ABC):
    @abstractmethod
    def get_area(self) -> float:
        """returns the area of a shape"""
        raise NotImplementedError
    @abstractmethod
    def get_perimeter(self) -> float:
        """returns the perimeter of a shape"""
        raise NotImplementedError

@dataclass
class Circle(Shape):
    radius: float

    def get_area(self) -> float:
        return math.pi * self.radius * self.radius
    def get_perimeter(self) -> float:
        return 2 * math.pi * self.radius

@dataclass
class Rectangle(Shape):
    length: float
    width: float

    def get_area(self) -> float:
        return self.length * self.width
    def get_perimeter(self) -> float:
        return 2 * self.length + 2 * self.width

@dataclass
class Triangle(Shape):
    # for the sake of implicity, this is a right triangle
    base: float
    height: float

    def get_area(self) -> float:
        return 0.5 * self.base * self.height
    def get_perimeter(self) -> float:
        altSide = (self.base ** 2 + self.height ** 2) ** (0.5)
        return self.base + 2 * altSide

class Square:
    """perfectionist rectangle"""
    def __init__(self, side):
        self.rectangle = Rectangle(side, side)
    
    @property
    def side(self) -> float:
        return self.rectangle.length
    
    @side.setter
    def side(self, newSide) -> None:
        self.rectangle.length = newSide
        self.rectangle.width = newSide
    
    def get_area(self) -> float:
        return self.rectangle.get_area()


def main() -> None:
    myCircle = Circle(2)
    print(myCircle.get_area())

    myRectangle = Rectangle(2, 4)
    print(myRectangle.get_area())
    
    mySquare = Square(3)
    print(mySquare.get_area())

    mySquare.side = 4
    print(mySquare.get_area())

if __name__ == "__main__":
    main()