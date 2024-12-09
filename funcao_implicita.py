from manim import *


class ImplicitFunctionTheorem(Scene):
    def construct(self):
        # Title
        title = Text("Teorema da Função Implícita", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Initial setup - spaces definition
        spaces_def = Tex(
            r"Sejam $X,Y,Z$ espaços de Banach e",
            r"$u_0=(x_0,y_0) \in U \subset X \times Y$, com $U$ aberto \\",
            r"e $F: X\times Y \to Z$ onde as seguintes propriedades valem:",
            tex_environment="flushleft",
        ).scale(0.8)
        spaces_def.next_to(title, DOWN, buff=1)

        self.play(Write(spaces_def))
        self.wait(1)

        # Properties
        properties = (
            VGroup(
                Tex(r"1. $F$ é contínua em $u_0$ com $F(u_0)=0$;"),
                Tex(r"2. $D_yF(u)$ existe para todo $u \in U$;"),
                Tex(r"3. $D_yF$ é contínua em $u_0$ e $D_yF(u_0)$ é invertível;"),
            )
            .scale(0.8)
            .arrange(DOWN, aligned_edge=LEFT)
        )

        properties.next_to(spaces_def, DOWN)

        for prop in properties:
            self.play(Write(prop))
            self.wait(0.4)

        # Fade out previous content
        self.play(FadeOut(spaces_def), FadeOut(properties))

        # Conclusion
        conclusion_1 = (
            Tex(
                r"Então existem constantes $\alpha, \beta >0$ para as quais",
                r" $\overline{B_X}(x_0,\alpha)\times \overline{B_Y}(y_0, \beta) \subset U$",
                tex_environment="flushleft",
            )
            .scale(0.8)
            .to_edge(LEFT)
        )
        conclusion_1.next_to(title, DOWN, buff=0.5)

        conclusion_2 = Tex(
            r"e uma única aplicação",
            r"$$f: \overline{B_X}(x_0,\alpha) \to \overline{B_Y}(y_0, \beta)$$",
            tex_environment="flushleft",
        ).scale(0.8)
        conclusion_2.next_to(conclusion_1, DOWN).align_to(conclusion_1, LEFT)

        final_relation = Tex(
            r"tal que a relação",
            r"$$F(x,y)=0 \iff f(x)=y$$",
            r"é válida para todo par $(x,y) \in \overline{B_X}(x_0,\alpha) \times \overline{B_Y}(y_0, \beta)$",
            tex_environment="flushleft",
        ).scale(0.8)
        final_relation.next_to(conclusion_2, DOWN, buff=0.5).align_to(
            conclusion_2, LEFT
        )

        self.play(Write(conclusion_1))
        self.wait(0.2)
        self.play(Write(conclusion_2))
        self.wait(0.2)
        self.play(Write(final_relation))
        self.wait(3)

        # Optional: fade everything out at the end
        self.play(FadeOut(Group(title, conclusion_1, conclusion_2, final_relation)))
        self.wait(1)
