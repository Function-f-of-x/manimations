from manim import *
from Render import render

class SquareScene(Scene):
    def construct(self):
        square = Square()
        self.play(Create(square))

if __name__ == "__main__":
    render("manim -qh Example1.py SquareScene")
