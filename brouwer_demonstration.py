from manim import *
import numpy as np


class BrouwerFixedPoint(Scene):
    def construct(self):
        # Title
        title = Text("Teorema do Ponto Fixo de Brouwer", font_size=40)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait()

        # Statement of the theorem
        theorem = Tex(
            r"Seja $f: B^n \to B^n$ uma aplicação contínua, onde $B^n$ é a bola unitária fechada.",
            r" Então, $f$ possui um ponto fixo.",
        ).scale(0.7)
        theorem.next_to(title, DOWN, buff=0.5)
        self.play(Write(theorem))
        self.wait(2)
        self.play(FadeOut(theorem))

        # Argument by contradiction

        contradiction = Tex(
            r"Por um momento, suponha que $f$ não possui ponto fixo. Defina a aplicação $r: B^n \to S^{n-1}$ estendendo",
            r" a semirreta com início em $f(x)$ e que passa por $x$. Definimos $r(x)$ como o ponto de interseção de $S^{n-1}$ com a semirreta.",
            tex_environment="flushleft",
        )

        contradiction1 = Tex(
            r" Tal aplicação está bem definida pois, por hipótese, $f(x) \neq x$ para todo $x \in B^n$ e sua continuidade é garantida pela continuidade de $f$. De fato,",
            r" podemos definir a semirreta como",
            r"$$\gamma(t, x) = (1-t)f(x) + tx, \quad t \geq 0$$",
            r"e $r(x) = \gamma(t_0, x)$ para dado $t_0$ que satisfaz $\|\gamma(t_0, x)\| = 1$. Como $\gamma$ é contínua, $r$ é contínua.",
            tex_environment="flushleft",
        )

        contradiction2 = Tex(
            r" Isso faz de $r$ uma retração de $B^n$ em $S^{n-1}$, o que é uma contradição com o Lema anterior.",
            r" Logo, $f$ possui um ponto fixo.",
            tex_environment="flushleft",
        )
        contradiction.scale(0.7)
        contradiction1.scale(0.7)
        contradiction2.scale(0.7)
        contradiction.next_to(title, DOWN, buff=0.5)
        contradiction1.next_to(contradiction, DOWN, buff=0.5)
        contradiction2.next_to(contradiction1, DOWN, buff=0.5)
        self.play(Write(contradiction))
        self.play(Write(contradiction1))
        self.play(Write(contradiction2))
        self.wait(2)

        self.play(
            FadeOut(contradiction), FadeOut(contradiction1), FadeOut(contradiction2)
        )

        example_intro = Tex(
            r"Vamos considerar o caso $n=2$, onde $B^2$ é o disco unitário no plano.",
            r" A função $r(x)$ será construída para ilustrar o argumento.",
            tex_environment="flushleft",
        )
        example_intro.scale(0.7)
        example_intro.next_to(title, DOWN, buff=0.5)
        self.play(Write(example_intro))
        self.wait(2)
        self.play(FadeOut(example_intro))

        # Circle to represent B^2
        circle = Circle(radius=2, color=BLUE)
        self.play(Create(circle))

        # Points: origin, x, f(x), and r(x)
        fx = Dot(point=[0.3, 0.3, 0], color=RED)
        x = Dot(point=[1, 1, 0], color=YELLOW)
        rx = Dot(point=[-np.sqrt(2), -np.sqrt(2), 0], color=GREEN)

        self.play(FadeIn(fx), FadeIn(x), FadeIn(rx))

        # Labels for the points
        fx_label = MathTex("f(x)").next_to(fx, 0.3 * RIGHT + 0.3 * DOWN).scale(0.7)
        x_label = MathTex("x").next_to(x, 0.1 * RIGHT + 0.2 * DOWN).scale(0.7)
        rx_label = MathTex("r(x)").next_to(rx, 0.3 * RIGHT).scale(0.7)
        self.play(Write(fx_label), Write(x_label), Write(rx_label))

        # Lines to represent the semirays
        line_fx_x = Line(fx.get_center(), x.get_center(), color=WHITE)
        line_x_rx = Line(x.get_center(), rx.get_center(), color=WHITE)
        self.play(Create(line_fx_x), Create(line_x_rx))

        # Arrow to extend semirray
        arrow_rx_extension = Arrow(
            start=rx.get_center(),
            end=rx.get_center() * 1.5,
            color=WHITE,
            buff=0,
        )
        self.play(Create(arrow_rx_extension))

        # Highlight the contradiction argument
        contradiction_text = Tex(
            r"A função $r(x)$ é uma retração de $B^2$ em $S^{1}$.",
            r" Isto contradiz a topologia de $B^2$!",
        ).scale(0.7)
        contradiction_text.next_to(circle, DOWN, buff=1)
        self.play(Write(contradiction_text))
        self.wait(2)

        # End scene
        self.wait(3)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
