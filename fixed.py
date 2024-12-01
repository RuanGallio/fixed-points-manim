from manim import *
import numpy as np


class BanachSenVisualization(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-0.5, 5, 0.5],
            y_range=[-0.5, 4, 0.5],
            axis_config={"include_numbers": True},
            tips=False,
        )

        title = Text("Teorema de ponto fixo de Banach:")
        title.to_edge(UP)
        title.scale(0.8)

        identity_line = axes.plot(lambda x: x, x_range=[-0.3, 4], color=BLUE_C)
        identity_label = Text("y = x", color=BLUE_C).scale(0.5)
        identity_label.next_to(axes.c2p(3.6, 3.6), RIGHT)

        sen_function = axes.plot(
            lambda x: np.sin(x + PI / 4) / 2 + 2, x_range=[-0.5, 4], color=RED
        )
        function_label = MathTex(
            "y = \\frac{\sin(x + \\frac{\\pi}{4})}{2} +2 ", color=RED
        ).scale(0.5)
        function_label.next_to(axes.c2p(3.9, 1.3), RIGHT)

        self.play(Create(axes), Write(title))
        self.play(Create(identity_line), Write(identity_label))
        self.play(Create(sen_function), Write(function_label))

        start_x = 1.5
        point = Dot(axes.c2p(start_x, 0), color=YELLOW)
        value_text = Text("x = 1.500").scale(0.6)
        value_text.to_edge(DOWN)
        self.play(Create(point), Write(value_text))

        current_x = start_x
        for _ in range(6):
            new_y = np.sin(current_x + PI / 4) / 2 + 2

            vertical_line = DashedLine(
                axes.c2p(current_x, current_x),
                axes.c2p(current_x, new_y),
                color=GREEN,
                stroke_width=2,
            )

            horizontal_line = DashedLine(
                axes.c2p(current_x, new_y),
                axes.c2p(new_y, new_y),
                color=GREEN,
                stroke_width=2,
            )

            self.play(Create(vertical_line))
            self.play(point.animate.move_to(axes.c2p(current_x, new_y)))
            self.play(Create(horizontal_line))
            self.play(
                point.animate.move_to(axes.c2p(new_y, new_y)),
                Transform(
                    value_text, Text(f"x = {new_y:.3f}").scale(0.6).to_edge(DOWN)
                ),
            )

            current_x = new_y
            self.play(FadeOut(vertical_line), FadeOut(horizontal_line))

        fixed_point = Dot(axes.c2p(current_x, current_x), color=GREEN)
        fixed_point_label = Text(
            f"Ponto Fixo ({current_x:.3f}, {current_x:.3f})", color=GREEN
        ).scale(0.5)
        fixed_point_label.next_to(fixed_point, 2 * UP)

        self.play(Create(fixed_point), Write(fixed_point_label))
        self.wait(2)


# To render:
# manim -pql scene_file.py BanachSenVisualization
