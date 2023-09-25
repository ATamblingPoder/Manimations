from manim import *

class Mobjects(Scene):
    def construct(self):
        circle = Circle()
        self.add(circle)
        self.wait(2)
        self.remove(circle)
        self.wait(1)

class Shapes(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        triangle = Triangle()

        circle.shift(LEFT)
        square.shift(UP)
        triangle.shift(RIGHT)

        self.add(circle, square, triangle)
        self.wait(2)
