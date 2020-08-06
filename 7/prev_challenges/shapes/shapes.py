class Shape:
    def __init__(self, shape_type):
        self.shape_type = shape_type

    def area():
        raise NotImplementedError

class Square(Shape):
    def __init__(self, side):
        Shape.__init__(self, "Square")
        self.side = side

    def area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__(self, width, height):
        Shape.__init__(self, "Triangle")
        self.width = width
        self.height = height

    def area(self):
        return (self.width * self.height) / 2


