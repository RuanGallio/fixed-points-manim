from manim import *


class ImplicitInterpretation(Scene):
    def construct(self):
        # Title
        title = Text("Interpretação Geométrica", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Key idea text
        interpretation = Tex(
            r"\raggedright A ideia principal é: se tivermos uma equação $F(x,y)=0$ e\\",
            r"a derivada parcial em relação a $y$ não se anula em um ponto\\",
            r"de solução $(x_0,y_0)$, então podemos resolver a equação\\",
            r"para $y$ próximo a este ponto.",
        ).align_to(LEFT + UP)
        interpretation.shift(2.5 * LEFT)
        interpretation.next_to(title, DOWN, buff=1)

        # Example
        example = Tex(
            r"\raggedright \textbf{Exemplo:} Considere a equação de um círculo\\",
            r"$x^2 + y^2 = 1$",
        ).align_to(LEFT + UP)
        example.shift(2.5 * LEFT)
        example.next_to(interpretation, DOWN, buff=1)

        # Local description
        local_desc = Tex(
            r"\raggedright Próximo ao ponto $(0,1)$, podemos expressar $y$\\",
            r"explicitamente como $y = \sqrt{1-x^2}$",
        ).align_to(LEFT + UP)
        local_desc.shift(2.5 * LEFT)
        local_desc.next_to(example, DOWN, buff=1)

        # Create axes for the circle visualization
        axes = Axes(
            x_range=[-1.5, 1.5],
            y_range=[-1.5, 1.5],
            axis_config={"include_tip": True},
        )

        # Create the circle
        circle = Circle(radius=1)
        circle.set_color(BLUE)

        # Create a dot at (0,1)
        point = Dot(axes.coords_to_point(0, 1), color=RED)
        point_label = Tex("$(0,1)$").next_to(point, UR, buff=0.1)

        # Create a neighborhood around (0,1)
        neighborhood = Arc(
            radius=0.5,
            angle=PI / 2,
            start_angle=PI / 4,
            color=YELLOW,
            arc_center=axes.coords_to_point(0, 1),
        )

        # Group the geometric elements
        geometric_group = VGroup(axes, circle, point, point_label, neighborhood)
        geometric_group.scale(0.8)  # Make it smaller to fit
        geometric_group.next_to(local_desc, DOWN, buff=1)

        # Animations
        self.play(Write(interpretation))
        self.wait(2)
        self.play(Write(example))
        self.wait(1)
        self.play(Write(local_desc))
        self.wait(1)
        self.play(Create(axes))
        self.play(Create(circle))
        self.play(Create(point), Write(point_label))
        self.play(Create(neighborhood))
        self.wait(3)

        # Final fade out
        self.play(
            FadeOut(Group(title, interpretation, example, local_desc, geometric_group))
        )
        self.wait(1)
