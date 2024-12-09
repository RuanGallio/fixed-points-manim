from manim import *


class SchafferFixedPoint(Scene):
    def construct(self):
        # Title
        title = Text("Teorema do Ponto Fixo de Schaffer", font_size=40)
        title.to_edge(UP)
        self.play(Write(title))

        # Definition text
        definition = Tex(
            r"\textbf{Definição:} Dados espaços de Banach $X,Y$, uma aplicação \\ $T: U \subset X \to Y$ é dita compacta se a imagem de conjuntos \\ limitados são conjuntos relativamente compactos.",
            tex_environment="flushleft",
        ).scale(0.8)
        self.play(Write(definition))
        self.wait(3)

        # Theorem statement
        theorem = VGroup(
            Tex(
                r"Seja $T: X \to X$ uma aplicação contínua e compacta. Assuma que o conjunto"
            ).scale(0.8),
            MathTex(
                r"\mathcal{F} = \{x \in X; \quad x = \lambda T(x), \text{ para algum } 0 \leq \lambda \leq 1\} \subset X"
            ).scale(0.8),
            Tex(r"é limitado. Então $T$ possui um ponto fixo.").scale(0.8),
        ).arrange(DOWN)
        self.play(FadeOut(definition))
        for item in theorem:
            self.play(Write(item))
            self.wait(0.3)

        self.wait(3)
        self.play(FadeOut(theorem), FadeOut(title))
