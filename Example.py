from manim import *
from Render import render


class RotatedComplexPlane3D(ThreeDScene):
    def construct(self):
        plane = ComplexPlane(
            x_range=[-3, 3, 1],  # по умолчанию Re - ось x
            y_range=[-3, 3, 1],  # Im - ось y
            background_line_style={"stroke_opacity": 0.3, "stroke_color": GRAY},
            axis_config={"include_tip": True, "tip_length": 0.1},
        ).add_coordinates()

        plane.rotate(PI/2, RIGHT).rotate(PI/2, OUT)

        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        self.add(plane)


class ComplexNumberLine(ThreeDScene):
    def construct(self):
        imag = NumberLine(
            x_range=(-5, 5, 1),
            length=15,
            include_tip=True,
            tip_length=0.1,
            numbers_to_include=[-5, -4, -3, -2, -1, 1, 2, 3, 4],
            label_direction=UP,
            label_constructor=lambda x: MathTex(f"-" if x == "-" else f"i" if x == "1" else f"{x}i")
        ).rotate(PI / 2, DOWN)
        for num in imag.numbers:
            num.rotate(PI/2, RIGHT).flip(axis=OUT)
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES, zoom=0.8)
        self.add(imag)

if __name__ == '__main__':
    render("manim -r 1080,1080 Example.py ComplexNumberLine")