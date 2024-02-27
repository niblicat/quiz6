from abc import ABC, abstractmethod
import math
# Liskov Substitution Principle

class Shape(ABC):
    # get_area() does not violate LSP because of its implementation in each sublcass
    @abstractmethod
    def get_area(self) -> float:
        """returns the area of a shape"""
        raise NotImplementedError

class BaseHaver:
    def __init__(self, base) -> None:
        self.base = base
    def set_base(self, base) -> None:
        self.base = base
    def get_base(self) -> float:
        return self.base
    
class HeightHaver:
    def __init__(self, height) -> None:
        self.height = height
    def set_height(self, height) -> None:
        self.height = height
    def get_height(self) -> float:
        return self.height

class WidthHaver:
    def __init__(self, width) -> None:
        self.width = width
    def set_width(self, width) -> None:
        self.width = width
    def get_width(self) -> float:
        return self.width

class LengthHaver:
    def __init__(self, length) -> None:
        self.length = length
    def set_length(self, length) -> None:
        self.length = length
    def get_length(self) -> float:
        return self.length

class Circle(Shape, WidthHaver):
    def __init__(self, radius):
        super().__init__(width=(radius / 2))

    def get_area(self) -> float:
        return math.pi * (self.width / 2) ** 2
    

class Rectangle(Shape, LengthHaver, WidthHaver):
    def __init__(self, length, width) -> None:
        LengthHaver.__init__(self, length=length)
        WidthHaver.__init__(self, width=width)

    def get_area(self) -> float:
        return self.length * self.width

class Triangle(Shape, BaseHaver, HeightHaver):
    # for the sake of implicity, this is a right triangle
    def __init__(self, base, height) -> None:
        BaseHaver.__init__(self, base=base)
        HeightHaver.__init__(self, height=height)

    def get_area(self) -> float:
        return 0.5 * self.base * self.height

class Square(Shape, LengthHaver):
    """perfectionist rectangle"""
    def __init__(self, side) -> None:
        self.length = side

    def get_area(self) -> float:
        return self.length ** 2
    
class SideHaver:
    def __init__(self, side) -> None:
        self.side = side
    def set_side(self, side) -> None:
        self.side = side
    def get_side(self) -> float:
        return self.side
    
class Polygon(Shape):
    def __init__(self, sides) -> None:
        self.sides = sides

    def get_area(self) -> float:
        return NotImplementedError # do some cool area calculation using self.sides


def main() -> None:
    myCircle = Circle(2)
    print(myCircle.get_area())

    myRectangle = Rectangle(2, 4)
    print(myRectangle.get_area())
    
    mySquare = Square(3)
    print(mySquare.get_area())

    mySquare.set_length(4)
    print(mySquare.get_area())

if __name__ == "__main__":
    main()