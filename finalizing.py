from manim import *


class FinalScene(Scene):
    def construct(self):
        # Thank you titlet= Text("Conclusão", font_size=60)tto_edge(UP)
        title = Text("Conclusão", font_size=60).to_edge(UP)

        # Create boxes for each theorem
        theorems = VGroup(
            VGroup(
                Text("Banach", font_size=36),
                Tex(r"$\bullet$ Serve para Espaços métricos completos"),
                Tex(r"$\bullet$ Baseado em contrações"),
                Tex(r"$\bullet$ Garante unicidade"),
                Tex(r"$\bullet$ Demonstração construtiva"),
            ).arrange(DOWN, aligned_edge=LEFT),
            VGroup(
                Text("Brouwer", font_size=36),
                Tex(r"$\bullet$ Dimensão finita"),
                Tex(r"$\bullet$ Hipóteses sobre os conjuntos: convexo e compacto"),
                Tex(r"$\bullet$ Garante apenas existência"),
                Tex(r"$\bullet$ Equivalente a diversos outros teoremas"),
                Tex(r"$\bullet$ Importância histórica"),
            ).arrange(DOWN, aligned_edge=LEFT),
            VGroup(
                Text("Schauder", font_size=36),
                Tex(r"$\bullet$ Dimensão infinita"),
                Tex(r"$\bullet$ Hipóteses sobre os conjuntos: convexo e compacto"),
                Tex(r"$\bullet$ Generalização de Brouwer"),
                Tex(r"$\bullet$ Com diversas reformulações"),
                Tex(r"$\bullet$ Possui mais aplicações em outras áreas"),
            ).arrange(DOWN, aligned_edge=LEFT),
        )

        # Scale everything down slightly
        theorems.scale(0.7)
        theorems.next_to(title, DOWN, buff=1)

        # Create boxes around each theorem
        boxes = VGroup(
            *[
                SurroundingRectangle(theorem, buff=0.3, corner_radius=0.2)
                for theorem in theorems
            ]
        )

        # Animate everything
        self.play(Write(title))
        self.wait(0.2)

        for theorem, box in zip(theorems, boxes):
            self.play(Write(theorem), Create(box))
            self.wait(2)
            self.play(FadeOut(theorem), FadeOut(box))
            self.wait(0.5)

        self.wait(1)
        self.play(FadeOut(title))

        thanks = Text("Obrigado!", font_size=72)
        self.play(Write(thanks))

        # Final fade out
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=2)
