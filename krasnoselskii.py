from manim import *


class KrasnoselskiFixedPoint(Scene):
    def construct(self):
        # Title
        title = Text("Teorema do Ponto Fixo de Krasnoselski", font_size=40)
        title.to_edge(UP)
        self.play(Write(title))

        # Theorem statement
        theorem = VGroup(
            Tex(
                r"Dado um espaço de Banach $X$ e $U \subset X$ não vazio, \\ fechado e convexo. Sejam $f,g:U \to X$ tais que"
            ).scale(0.8),
            Tex(r"1. $f(x) + g(y) \in U$ para todos $x,y \in U$;").scale(0.8),
            Tex(r"2. $f$ é contínuo e $f(U)$ é relativamente compacto;").scale(0.8),
            Tex(r"3. $g$ é uma contração de $U$ em $X$.").scale(0.8),
            Tex(
                r"Então existe $\bar{x} \in U$ tal que $f(\bar{x})+g(\bar{x})=\bar{x}$."
            ).scale(0.8),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)

        for item in theorem:
            self.play(Write(item))
            self.wait(0.6)
        self.wait(3)

        self.wait(3)
        self.play(FadeOut(theorem), FadeOut(title))
