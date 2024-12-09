from manim import *


class ContractionDefinition(Scene):
    def construct(self):
        # Title
        title = Text("Contração", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Definition of Lipschitz continuity
        lipschitz_def = Tex(
            r"\textbf{Definição} Uma função $f: X \to X$ é Lipschitz contínua se\\",
            r"existe $\lambda > 0$  tal que $d(f(x),f(y)) \leq \lambda d(x,y)$.",
        )
        lipschitz_def.next_to(title, DOWN, buff=1)

        self.play(Write(lipschitz_def))
        self.wait(2)

        # Contraction definition
        contraction_def = Tex(r"Se $0 < \lambda < 1$ , então $f$ é uma contração.")
        contraction_def.next_to(lipschitz_def, DOWN, buff=1)

        self.play(Write(contraction_def))
        self.wait(2)

        self.wait(3)
