from manim import *
from Render import render


class CubicParabolaDerivatives(MovingCameraScene):
    def construct(self):
        grid = NumberPlane(x_range=[-16, 16, 1], y_range=[-8.5, 8.5, 1],
                           background_line_style={"stroke_color": GREY, "stroke_width": 1, "stroke_opacity": 0.5})
        grid.add_coordinates()

        plotter = NumberPlane(x_range=[-2.1, 2.1, 1], y_range=[-8.5, 8.5, 1])

        func = plotter.plot(lambda x: x ** 3, color=YELLOW)
        diff1 = plotter.plot(lambda x: 3 * x ** 2, color=ORANGE)
        diff2 = plotter.plot(lambda x: 6 * x, color=RED)
        diff3 = grid.plot(lambda x: 6, color=PINK)
        functions = VGroup(func, diff1, diff2, diff3)
        for function in functions:
            function.save_state()

        func_label = MathTex(r"f(x)=x^3", color=YELLOW).to_corner(UL)
        diff1_label = MathTex(r"\frac{d}{dx} f(x)=3x^2", color=ORANGE).to_corner(UL)
        diff2_label = MathTex(r"\frac{d}{dx} \frac{d}{dx} f(x)=6x", color=RED).to_corner(UL)
        diff3_label = MathTex(r"\frac{d}{dx} \frac{d}{dx} \frac{d}{dx} f(x)=6", color=PINK).move_to(grid.c2p(-8.5,6))
        labels = VGroup(func_label, diff1_label, diff2_label, diff3_label)
        for label in labels:
            label.save_state()

        self.play(Create(grid), run_time=3)
        self.play(Write(func_label), Create(func))
        self.wait()
        self.play(Transform(func, diff1), Transform(func_label, diff1_label))
        self.wait(0.5)
        self.play(Transform(func, diff2), Transform(func_label, diff2_label))
        self.wait(0.5)
        self.play(self.camera.frame.animate.set(height=14),
                  Transform(func_label, func_label.copy().scale(14 / 8).move_to(grid.c2p(-9,6))))
        self.play(Transform(func, diff3), Transform(func_label, diff3_label.scale(14/8)))
        self.wait(0.4)
        self.play(Uncreate(func))
        self.play(Uncreate(func_label))
        func.restore()
        func_label.restore().scale(14 / 8).move_to(grid.c2p(-10,6))
        diff1_label.scale(14 / 8).next_to(func_label, DOWN, aligned_edge=LEFT)
        diff2_label.scale(14 / 8).next_to(diff1_label, DOWN, aligned_edge=LEFT)
        diff3_label.restore().scale(14 / 8).next_to(diff2_label, DOWN, aligned_edge=LEFT)
        self.wait()
        self.play(Create(func))
        self.play(Create(diff1))
        self.play(Create(diff2))
        self.play(Create(diff3))
        self.play(*[Create(label) for label in labels])
        self.wait(0.5)
        self.play(*[function.animate.set_color(GRAY) for function in functions],
                  *[label.animate.set_color(GRAY) for label in labels])
        self.wait()
        self.play(func.animate.set_color(YELLOW), func_label.animate.set_color(YELLOW))
        self.wait(0.6)
        self.play(func.animate.set_color(GRAY), func_label.animate.set_color(GRAY), diff1.animate.set_color(ORANGE),
                  diff1_label.animate.set_color(ORANGE))
        self.wait(0.6)
        self.play(diff1.animate.set_color(GRAY), diff1_label.animate.set_color(GRAY), diff2.animate.set_color(RED),
                  diff2_label.animate.set_color(RED))
        self.wait(0.6)
        self.play(diff2.animate.set_color(GRAY), diff2_label.animate.set_color(GRAY), diff3.animate.set_color(PINK),
                  diff3_label.animate.set_color(PINK))
        self.wait(0.5)
        self.play(
            func.animate.set_color(YELLOW), func_label.animate.set_color(YELLOW),
            diff1.animate.set_color(ORANGE), diff1_label.animate.set_color(ORANGE),
            diff2.animate.set_color(RED), diff2_label.animate.set_color(RED),
            diff3.animate.set_color(PINK), diff3_label.animate.set_color(PINK)
        )
        self.play(*[Uncreate(function) for function in functions], run_time=3)
        self.play(*[Uncreate(label) for label in labels], Uncreate(grid))
        self.wait(2)


if __name__ == '__main__':
    render("manim -qh CubicParabolaDerivatives.py CubicParabolaDerivatives")
