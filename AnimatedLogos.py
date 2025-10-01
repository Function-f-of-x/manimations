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
        text = Text("Парабола", color=YELLOW).rotate(PI / 7).move_to(plane.c2p(2, -1.3)).scale(0.8)

        border = Circle(color=YELLOW, stroke_width=5000, radius=29.48)

        self.camera.frame.set(height=9)
        self.play(Create(plane), run_time=3)

        def rate_function(speed_function, t):
            ts = np.linspace(0,1,200)
            s = np.cumsum(speed_function(ts))
            s = (s - s[0]) / (s[-1]-s[0])
            return np.interp(t, ts, s)
        
        self.play(Create(parabola), rate_func=lambda t: rate_function(lambda x: (x-0.5)**2 + 0.1, t))
        self.play(Create(label))
        self.play(Create(text))
        self.play(Create(border))
        self.wait()


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
            lambda t: np.array([t, np.e ** t, 0]),
            t_range=[-8, 2],
            color=BLUE
        )

        label = MathTex(r"e^x", color=BLUE).move_to(plane.c2p(-1.5, -1.5)).scale(3)
        text = Text("Экспонента", color=BLUE).rotate(PI / 7).move_to(plane.c2p(2, -1.3)).scale(0.8)

        border = Circle(color=BLUE, stroke_width=5000, radius=29.48)

        self.camera.frame.set(height=9)
        self.play(Create(plane), run_time=3)

        def rate_function(speed_function, t):
            ts = np.linspace(0,1,200)
            s = np.cumsum(speed_function(ts))
            s = (s - s[0]) / (s[-1]-s[0])
            return np.interp(t, ts, s)
        
        self.play(Create(exponent), run_time=11/6, rate_func=lambda t: rate_function(lambda x: np.exp(5*x), t))
        self.play(Create(label))
        self.play(Create(text))
        self.play(Create(border))
        self.wait()


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
            t_range=[-8, 8],
            color=RED
        )

        label = MathTex(r"\sin(x)", color=RED).move_to(plane.c2p(0, -2)).scale(2.5)
        text = Text("Синусоида", color=RED).move_to(plane.c2p(0, 2)).scale(1)

        border = Circle(color=RED, stroke_width=5000, radius=29.48)

        self.camera.frame.set(height=9)
        self.play(Create(plane), run_time=3)

        def rate_function(speed_function, t):
            ts = np.linspace(0,1,200)
            s = np.cumsum(speed_function(ts))
            s = (s - s[0]) / (s[-1]-s[0])
            return np.interp(t, ts, s)
        
        self.play(Create(sinewave), run_time=8/3, rate_func=lambda t: rate_function(lambda x: np.sin(-8 + 16*x) + 1.7, t))
        self.play(Create(label))
        self.play(Create(text))
        self.play(Create(border))
        self.wait()


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
            t_range=[-8, 8],
            color=WHITE
        )

        label = MathTex(r"f(x)", color=WHITE).move_to(plane.c2p(0, -2.5)).scale(2.5)
        text = Text("Функция", color=WHITE).move_to(plane.c2p(0, 2.5)).scale(1)

        border = Circle(color=WHITE, stroke_width=5000, radius=29.48)

        self.camera.frame.set(height=9)
        self.play(Create(plane), run_time=3)

        def rate_function(speed_function, t):
            ts = np.linspace(0,1,200)
            s = np.cumsum(speed_function(ts))
            s = (s - s[0]) / (s[-1]-s[0])
            return np.interp(t, ts, s)
        
        self.play(Create(function), run_time=8/3, rate_func=lambda t: rate_function(lambda x: np.sin(-8 + 16*x) + 1.7, t))
        self.play(Create(label))
        self.play(Create(text))
        self.play(Create(border))
        self.wait()

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
            x_range=(-10,10,1),
            y_range=(-10,10,1),
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
        ).move_to(plane.c2p(0,0))

        imaginary_exponent = axes.plot_parametric_curve(
            lambda t: np.array([t, np.cos(t), np.sin(t)]),
            t_range = [-5, 5],
            color = BLUE
        )
        
        label = MathTex(r"e^{ix}", color=BLUE).move_to(flat.c2p(-3,-4)).scale(4)
        text = Paragraph("Мнимая", "экспонента", alignment="center", color=BLUE).move_to(flat.c2p(3,-4)).rotate(PI / 7)
        
        border = Circle(color=BLUE, stroke_width=5000, radius=29.48)

        self.camera.frame_height = 9
      
        self.add_fixed_in_frame_mobjects(border, label, text)
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES, zoom=0.8, distance=1000, focal_distance=1000)
        self.add(plane, labels, line, imaginary_exponent)
        self.wait()
        
        dot = Dot3D(color=BLUE).scale(1.5)
        dot.move_to(axes.c2p(0, 1, 0))

        t_tracker = ValueTracker(0)
      
        value_label = always_redraw(lambda: MathTex(
            f"e^{{i{t_tracker.get_value():.2f}}}="
            f"{np.cos(t_tracker.get_value()):.2f}"
            + ("+" if np.sin(t_tracker.get_value()) >= 0 else "")
            + f"{np.sin(t_tracker.get_value()):.2f}i",
            font_size=72,
            color=BLUE
        ).rotate(PI/2, RIGHT).next_to(dot, DOWN+OUT))

        
        def update_dot(mob):
            t = t_tracker.get_value()
            new_pos = axes.c2p(t, np.cos(t), np.sin(t))
            mob.move_to(new_pos)

        dot.add_updater(update_dot)

        self.add(dot, value_label)

        
        self.play(
            t_tracker.animate.set_value(PI),
            run_time=6,
            rate_func=lambda t: np.sqrt(t)
        )

        dot.clear_updaters()
        self.remove(value_label)

        
        dot.set_color(GOLD)
        euler_label = MathTex(r"e^{i\pi} + 1 = 0", color=GOLD, font_size=150).rotate(PI/2, RIGHT).next_to(dot, UP)
        self.add(euler_label)
        self.wait(2)
        euler_label_flat = MathTex(r"e^{i\pi} + 1 = 0", color=GOLD, font_size=150).move_to(flat.c2p(0, 4))
        
        self.remove(euler_label)
        self.add_fixed_in_frame_mobjects(euler_label_flat)
        self.move_camera(phi=90 * DEGREES, theta=0, run_time=2)
        self.wait()
        self.move_camera(phi=75 * DEGREES, theta=-45 * DEGREES, run_time=2)
        self.wait()


if __name__ == '__main__':
    render("manim -qh AnimatedLogos.py ImaginaryExponentLogo")
