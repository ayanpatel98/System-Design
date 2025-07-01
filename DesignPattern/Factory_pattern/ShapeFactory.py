from Shape import Shape
from CircleShape import CircleShape
from RectangleShape import RectangleShape
from SquareShape import SquareShape

class ShapeFactory:

    def getShape(self, shape)-> Shape:
        match shape:
            case "circle":
                return CircleShape()
            case "square":
                return SquareShape()
            case "rectangle":
                return RectangleShape()
            case _:
                raise ValueError("Enter valid shape")
        
