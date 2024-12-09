from manim import *


class RetractionDefinition(Scene):
    def construct(self):
        # Title
        title = Text("Definição de Retração", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))

        # Definition text
        definition = Tex(
            r"Seja $B^{n} \subset \mathbb{R}^{n}$, $B^{n} = \{ x \in \mathbb{R}^{n} \mid \|x\| \leq 1 \}$, ",
            r"a bola unitária centrada na origem.",
            r"Um conjunto $E \subset B^{n}$ é uma \textbf{retratação} de $B^{n}$ se existe uma aplicação contínua ",
            r"$r: B^{n} \to E$, também chamada de retratação, tal que $r(x) = x$ para todo $x \in E$.",
            tex_environment="flushleft",
        ).scale(0.7)
        definition.next_to(title, DOWN)
        self.play(Write(definition, run_time=10))

        # Lemma title
        lemma_title = Text("Lema", font_size=48)
        lemma_title.next_to(definition, DOWN, buff=1)
        self.play(Write(lemma_title))

        # Lemma statement
        lemma = Tex(
            r"A esfera unitária, $S^{n-1} = \{ x \in \mathbb{R}^{n} \mid \|x\| = 1 \}$, ",
            r"não é uma retratação de $B^{n}$.",
            tex_environment="flushleft",
        ).scale(0.7)
        lemma.next_to(lemma_title, DOWN)
        self.play(Write(lemma, run_time=5))

        self.wait(2)
