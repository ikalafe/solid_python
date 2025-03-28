# shape_ocp.py

from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    def __init__(self, shape_type):
        self.shape_type = shape_type
        
    @abstractmethod
    def calculate_area(self):
        pass
    
class Circle(Shape):
    def __init__(self, redius):
        super().__init__("circle")
        self.redius = redius
        
    def calculate_area(self):
        return pi * self.redius**2
    
class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("rectangle")
        self.width = width
        self.height = height
        
    def calculate_area(self):
        return self.width * self.height
    
class Square(Shape):
    def __init__(self, side):
        super().__init__("square")
        self.side = side
        
    def calculate_area(self):
        return self.side**2