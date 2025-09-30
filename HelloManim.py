from manim import *
from Render import render


class HelloManim(Scene):
    def construct(self):
        circle = Circle(color=BLUE, fill_opacity=0.3).scale(2)
        square = Square(color=GREEN)
        text = Text("Привет, Manim!", font_size=30)
        self.play(Create(square))
        self.play(Rotate(square, angle=PI + PI / 4))
        self.play(square.animate.scale(2))
        self.play(Write(text))
        self.play(square.animate.shift(0.5 * UP), text.animate.shift(3 * DOWN))
        self.wait(0.3)
        self.play(Transform(square, circle), text.animate.shift(3 * UP))
        self.wait(0.3)
        self.play(ShrinkToCenter(square), ShrinkToCenter(text))
        self.wait()


if __name__ == '__main__':
    render("manim -r 1920,1080 --fps 24 HelloManim.py HelloManim")
