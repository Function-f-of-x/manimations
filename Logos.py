from manim import *
from Render import render


class ParabolaLogo(MovingCameraScene):
    def construct(self):
        plane = NumberPlane(
            x_range=[-8, 8, 1],
            y_range=[-8, 8, 1],
            background_line_style={
                "stroke_color": GREY,
                "stroke_width": 1,
                "stroke_opacity": 0.5
            },
            axis_config={
                "include_numbers": True
            }
        )

        parabola = plane.plot_parametric_curve(
            lambda t: np.array([t, t ** 2, 0]),
            t_range=[-3, 3],
            color=YELLOW
        )

        label = MathTex(r"x^2", color=YELLOW).move_to(plane.c2p(-1.5, -1.5)).scale(3)
        text = Text("Parabola", color=YELLOW).rotate(PI / 7).move_to(plane.c2p(2, -1.3)).scale(0.8)

        border = Circle(color=YELLOW, stroke_width=200, radius=5.45)
        self.camera.frame.set(width=9)
        self.add(plane)
        self.add(parabola)
        # self.add(border)
        self.add(label)
        self.add(text)


class ExponentLogo(MovingCameraScene):
    def construct(self):
        plane = NumberPlane(
            x_range=[-8, 8, 1],
            y_range=[-8, 8, 1],
            background_line_style={
                "stroke_color": GREY,
                "stroke_width": 1,
                "stroke_opacity": 0.5
            },
            axis_config={
                "include_numbers": True
            }
        )

        exponent = plane.plot_parametric_curve(
            lambda t: np.array([t, (np.e) ** t, 0]),
            t_range=[-5, 3],
            color=BLUE
        )

        label = MathTex(r"e^x", color=BLUE).move_to(plane.c2p(-1.5, -1.5)).scale(3)
        text = Text("Экспонента", color=BLUE).rotate(PI / 7).move_to(plane.c2p(2, -1.3)).scale(0.8)

        border = Circle(color=BLUE, stroke_width=200, radius=5.45)
        self.camera.frame.set(width=9)
        self.add(plane)
        self.add(exponent)
        self.add(border)
        self.add(label)
        self.add(text)


class SinewaveLogo(MovingCameraScene):
    def construct(self):
        plane = NumberPlane(
            x_range=[-8, 8, 1],
            y_range=[-8, 8, 1],
            background_line_style={
                "stroke_color": GREY,
                "stroke_width": 1,
                "stroke_opacity": 0.5
            },
            axis_config={
                "include_numbers": True
            }
        )

        sinewave = plane.plot_parametric_curve(
            lambda t: np.array([t, np.sin(t), 0]),
            t_range=[-5, 5],
            color=RED
        )

        label = MathTex(r"\sin(x)", color=RED).move_to(plane.c2p(0, -2)).scale(2.5)
        text = Text("Синусоида", color=RED).move_to(plane.c2p(0, 2)).scale(1)

        border = Circle(color=RED, stroke_width=200, radius=5.45)
        self.camera.frame.set(width=9)
        self.add(plane)
        self.add(sinewave)
        self.add(border)
        self.add(label)
        self.add(text)


class FunctionLogo(MovingCameraScene):
    def construct(self):
        plane = NumberPlane(
            x_range=[-8, 8, 1],
            y_range=[-8, 8, 1],
            background_line_style={
                "stroke_color": GREY,
                "stroke_width": 1,
                "stroke_opacity": 0.5
            },
            axis_config={
                "include_numbers": True
            }
        )

        function = plane.plot_parametric_curve(
            lambda t: np.array(
                [t, (np.sin(3*t+42) + np.sin(np.pi*(3*t+42)) + np.sin(np.e*(3*t+42)) + np.sin(np.sqrt(2)*(3*t+42)))/2, 0]),
            t_range=[-5, 5],
            color=WHITE
        )

        label = MathTex(r"f(x)", color=WHITE).move_to(plane.c2p(0, -2.5)).scale(2.5)
        text = Text("Function", color=WHITE).move_to(plane.c2p(0, 2.5)).scale(1)

        border = Circle(color=WHITE, stroke_width=200, radius=5.45)
        self.camera.frame.set(width=9)
        self.add(plane)
        self.add(function)
        self.add(border)
        self.add(label)
        self.add(text)

class ImaginaryExponentLogo(ThreeDScene):
    def construct(self):
        line = NumberLine(
            x_range=(-5, 5, 1),
            length=15,
            include_numbers=True,
            numbers_to_exclude=[0],
            font_size=48,
            include_tip=True,
            tip_length=0.1
        ).rotate(PI / 2, RIGHT)

        plane = NumberPlane(
            x_range=(-5, 5, 1),
            y_range=(-5, 5, 1),
            x_length=15,
            y_length=15,
            background_line_style={"stroke_opacity": 0.3, "stroke_color": GRAY},
            x_axis_config={
                "include_tip": True,
                "tip_length": 0.1,
                "include_numbers": True,
                "font_size": 48
            },
            y_axis_config={
                "include_tip": True,
                "tip_length": 0.1,
                "include_numbers": False
            }
        )

        plane.rotate(PI / 2, RIGHT).rotate(PI / 2, OUT).move_to(line.n2p(0))
        for num in plane.get_x_axis().numbers:
            num.shift(0.2 * RIGHT)
        labels = VGroup()
        for i in range(-5, 5):
            if i == 0:
                continue
            labels.add(
                MathTex(f"-i" if i == -1 else f"i" if i == 1 else f"{i}i", font_size=48).move_to(plane.c2p(0, i)).shift(
                    0.3 * UP if i == 1 else 0.45 * UP if i == -1 else 0.4 * UP if i > 0 else 0.6 * UP).rotate(
                    PI / 2, UP).rotate(PI / 2, RIGHT))

        flat = NumberPlane(
            x_range=(-10, 10, 1),
            y_range=(-10, 10, 1),
            x_length=20,
            y_length=20
        )

        axes = ThreeDAxes(
            x_range=(-5, 5, 1),
            y_range=(-5, 5, 1),
            z_range=(-5, 5, 1),
            x_length=15,
            y_length=15,
            z_length=15
        ).move_to(plane.c2p(0, 0))

        imaginary_exponent = axes.plot_parametric_curve(
            lambda t: np.array([t, np.cos(t), np.sin(t)]),
            t_range=[-5, 5],
            color=BLUE
        )

        label = MathTex(r"e^{ix}", color=BLUE).move_to(flat.c2p(-3, -4)).scale(4)
        text = Paragraph("Мнимая", "экспонента", alignment="center", color=BLUE).move_to(flat.c2p(3, -4)).rotate(PI / 7)

        border = Circle(color=BLUE, stroke_width=500, radius=9.53)

        self.add_fixed_in_frame_mobjects(border, label, text)
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES, zoom=0.8, distance=1000, focal_distance=1000)
        self.add(plane, labels, line, imaginary_exponent)


if __name__ == '__main__':
    render("manim -r 1080,1080 Logos.py -a")
