class Circle:
    def draw(self):
        print("Circle.draw")


class Square:
    def draw(self):
        print("Square.draw")


class ShapeFactory:
    @staticmethod
    def getShape(type):
        if type == "circle":
            return Circle()
        if type == "square":
            return Square()
        assert 0, "Could not find shape"+type


# f = ShapeFactory()
s = ShapeFactory.getShape("square")
print("===", s, "===")
s.draw()
print("======")
t = ShapeFactory.getShape("triangle")
