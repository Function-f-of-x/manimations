from manim import *

from Render import render


class ParabolaToParaboloid(ThreeDScene):
    def construct(self):
        plane = NumberPlane(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            background_line_style={
                "stroke_color": GREY,
                "stroke_width": 1,
                "stroke_opacity": 0.5
            },
            axis_config={
                "include_numbers": True,
                "include_tip": True
            }
        )
        plane.rotate(PI / 2, axis=RIGHT)
        plane.move_to(ORIGIN)

        plane_wg = NumberPlane(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            background_line_style={
                "stroke_color": GREY,
                "stroke_width": 0,
                "stroke_opacity": 0
            },
            axis_config={
                "include_numbers": True,
                "include_tip": True
            }
        )
        plane_wg.rotate(PI / 2, axis=RIGHT)
        plane_wg.move_to(ORIGIN)

        grid_xy = NumberPlane(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            background_line_style={
                "stroke_color": GREY,
                "stroke_width": 1,
                "stroke_opacity": 0.5
            },
            axis_config={
                "include_numbers": False,
                "include_tip": False
            }
        )
        grid_xy.move_to(plane.c2p(0, 0))

        parabola = plane.plot_parametric_curve(
            lambda t: np.array([t, t ** 2, 0]),
            t_range=[-2, 2],
            color=YELLOW
        )

        y_line = NumberLine(
            x_range=[-4, 4, 1],
            length=8,
            color=WHITE,
            include_numbers=True,
            include_tip=True,
            include_ticks=False,
            numbers_to_exclude=[0],
            font_size=25
        )
        y_line.rotate(PI / 2, axis=UP)
        y_line.rotate(PI / 2, axis=RIGHT)
        y_line.move_to(ORIGIN)

        dots = VGroup()
        circles = VGroup()
        for t in np.linspace(0, 2, 20):
            circle = Circle(radius=t, color=YELLOW).move_to(plane.c2p(0, 0)).shift(OUT * t ** 2)
            circles.add(circle)
            dot = Dot3D(plane.c2p(t, t ** 2), color=YELLOW)
            dots.add(dot)

        paraboloid = Surface(
            lambda u, v: np.array([
                u * np.cos(v),
                u * np.sin(v),
                u ** 2
            ]),
            u_range=[0, 2],
            v_range=[0, TAU],
            resolution=(20, 20),
            checkerboard_colors=[RED, RED.darker()],
            fill_opacity=2,
            stroke_color=RED
        )

        plane_label1 = MathTex("x").move_to(plane.c2p(4.5, 0)).rotate(PI / 2, axis=RIGHT)
        plane_label2 = MathTex("y").move_to(plane.c2p(0, 4.5)).rotate(PI / 2, axis=RIGHT)
        line_label = MathTex("y").move_to(y_line.n2p(4.5)).rotate(PI / 2, axis=OUT)
        parabola_label = MathTex(r"y=x^2", color=YELLOW).to_corner(UL).shift(3 * UP)
        paraboloid_label = MathTex(r"z=x^2+y^2", color=RED).to_corner(UL).shift(3 * UP)
        line_label.rotate(PI / 2, axis=UP)
        disclamer1 = Paragraph(
            "Я хз что с Manim",
            "но параболоид глюченный оказался",
            alignment="center",
            font_size=36
        )

        disclamer2 = Paragraph(
            "Я пытался это исправить,",
            "но он не исправлялся.",
            alignment="center",
            font_size=36
        )

        disclamer3 = Paragraph(
            "Так что я забил на это,",
            "и просто написал этот текст.",
            alignment="center",
            font_size=36
        )

        self.add_fixed_in_frame_mobjects(parabola_label, paraboloid_label)
        self.play(Write(disclamer1), run_time=2)
        self.wait(0.5)
        self.play(ShrinkToCenter(disclamer1))
        self.wait(0.5)
        self.play(Write(disclamer2), run_time=2)
        self.wait(0.5)
        self.play(ShrinkToCenter(disclamer2))
        self.wait(0.5)
        self.play(Write(disclamer3), run_time=2)
        self.wait(0.5)
        self.play(ShrinkToCenter(disclamer3))
        self.wait(2)
        self.set_camera_orientation(phi=PI / 2, zoom=0.8)
        self.play(Create(plane), run_time=2)
        self.play(Write(plane_label1), Write(plane_label2))
        self.play(Create(parabola), run_time=2)
        self.play(parabola_label.animate.shift(3 * DOWN), run_time=2)
        self.move_camera(phi=75 * DEGREES, theta=-45 * DEGREES, zoom=0.8, run_time=2)
        self.add(plane_wg)
        self.play(Create(y_line), Uncreate(plane), Create(grid_xy), run_time=3)
        self.play(Write(line_label),
                  Transform(plane_label2, MathTex("z").move_to(plane.c2p(0, 4.5)).rotate(PI / 2, axis=RIGHT)))
        self.wait(0.5)
        self.play(*[Create(dot) for dot in dots])
        self.play(Rotate(parabola, angle=2 * PI, axis=OUT), *[Create(obj) for obj in circles], run_time=3)
        self.play(Uncreate(parabola), *[Uncreate(dot) for dot in dots])
        self.play(circles.animate.set_color(RED))
        self.play(Create(paraboloid), run_time=3)
        self.remove(circles)
        self.play(parabola_label.animate.shift(3 * UP), paraboloid_label.animate.shift(3 * DOWN), run_time=2)
        self.move_camera(phi=75 * DEGREES, theta=180 * DEGREES, zoom=0.8, run_time=2)
        self.wait(0.5)
        self.move_camera(phi=15 * DEGREES, theta=180 * DEGREES, zoom=0.8, run_time=4)
        self.wait(0.5)
        self.move_camera(phi=165 * DEGREES, theta=-90 * DEGREES, zoom=0.8, run_time=2)
        self.wait(0.5)
        self.move_camera(phi=75 * DEGREES, theta=-45 * DEGREES, zoom=0.8, run_time=2)
        self.play(*[Uncreate(obj) for obj in
                    (paraboloid, grid_xy, plane_wg, y_line, paraboloid_label, plane_label1, plane_label2, line_label)],
                  run_time=3)
        self.wait()


if __name__ == '__main__':
    render("manim -qh ParabolaToParaboloid.py ParabolaToParaboloid")
