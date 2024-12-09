from manim import *


class FixedPointIntroduction(Scene):
    def construct(self):
        big_title = Tex(
            r"TEOREMAS DE PONTO FIXO E SUAS APLICAÇÕES \\ EM EQUAÇÕES DIFERENCIAIS PARCIAIS ELÍPTICAS",
            font_size=52,
        )
        autor = Tex("Ruan Pablo Pfeffer Gallio", font_size=34)
        orientador = Tex("Orientador: Sandro Marcos Guzzo", font_size=34)

        autores = VGroup(autor, orientador).arrange(DOWN, aligned_edge=RIGHT)

        # set autores under the title and flushed to the right margin
        autores.next_to(big_title, DOWN).align_to(big_title, RIGHT)

        self.play(Write(big_title))
        self.wait()
        self.play(Write(autores))
        self.wait(3)

        self.play(FadeOut(VGroup(big_title, autores)))

        # Title
        title = Text("Teoria de Pontos Fixos", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))

        # Definition
        definition = Tex(
            r"{{Um ponto fixo de uma função}} {{$f: X \to X$}} é \\ um ponto {{$\bar{x} \in X$}} tal que: {{$$f(\bar{x}) = \bar{x}$$ }}"
        )
        definition.next_to(title, DOWN, buff=1)
        self.play(Write(definition))
        self.wait(2)

        exemplo = Tex(r"Exemplo de pontos fixos em funções", font_size=48)

        # Simple example with a graph
        axes = Axes(
            x_range=[-1.5, 1.5, 0.5],
            y_range=[-0.5, 2.5, 0.5],
            x_length=6,  # Set equal lengths
            y_length=6,  # Set equal lengths
            axis_config={"include_numbers": True},
            tips=False,
        )

        axes.shift(0.5 * DOWN)

        # Plot y = x
        identity = axes.plot(lambda x: x, color=BLUE)
        # Plot y = x²
        func = axes.plot(lambda x: x**2, color=RED)

        # Labels
        func_label = MathTex(r"f(x) = x^2", color=RED).scale(0.7)
        func_label.move_to(axes.c2p(1.75, 1.75))
        id_label = MathTex(r"y = x", color=BLUE).scale(0.7)
        id_label.move_to(axes.c2p(1.5, 1))

        exemplo.move_to(title)
        self.play(FadeOut(definition), ReplacementTransform(title, exemplo))
        self.wait()
        self.play(Create(axes))
        self.wait()
        self.play(Create(func), Create(identity))
        self.play(Write(func_label), Write(id_label))

        # Mark fixed points
        fp1 = Dot(axes.c2p(0, 0), color=GREEN)
        fp2 = Dot(axes.c2p(1, 1), color=GREEN)
        fp_label = Text("Pontos Fixos", color=GREEN).scale(0.6)
        fp_label.move_to(axes.c2p(1.5, 0.4))

        self.play(Create(fp1), Create(fp2), Write(fp_label))
        self.wait(2)

        # Clear screen for summary
        self.play(
            FadeOut(
                VGroup(axes, identity, func, func_label, id_label, fp1, fp2, fp_label)
            ),
        )

        # Continuation of the class FixedPointIntroduction
        # Transition to application
        application_title = Text("Aplicação: Problemas de Valor Inicial", font_size=36)
        application_title.to_edge(UP)

        # Explanation of the ODE problem
        ode_problem = MathTex(
            r"\begin{cases}"
            r"u'(t) = f(t, u (t)), & t \in [0,L], \\"
            r"u(0) = u_0."
            r"\end{cases}"
        ).scale(0.8)
        ode_problem.next_to(application_title, DOWN, buff=1)

        tfc = Tex(r"Ou seja,")
        tfc.move_to(ode_problem.get_center())

        integrating = MathTex(
            r"\int_{0}^{t} {{u}}'{{(s)}} \, ds = \int_{0}^{t} {{f({{s}}, {{u(s)}})}} \, ds."
        ).scale(0.8)
        integrating.next_to(tfc, DOWN)

        # Adding integral transformation
        integral_transformation = MathTex(
            r"{{u}}{{(t)}} = u(0) + \int_{0}^{t} {{f(s, u(s))}} \, ds."
        ).scale(0.8)
        integral_transformation.move_to(integrating.get_center())

        text2 = Tex(r"Defina então o operador $T:C([0,L]) \to C([0,L])$ como:")
        text2.next_to(integral_transformation, DOWN)

        # Introduction of operator T
        operator_definition = MathTex(
            r"(Tu)(t) = u(0) + \int_{0}^{t} f(s, u(s)) \, ds."
        ).scale(0.8)
        operator_definition.next_to(text2, DOWN)

        # Linking operator T to fixed-point
        fixed_point_equation = MathTex(r"Tu = u").scale(0.8)
        fixed_point_equation.next_to(operator_definition, DOWN)

        # Animations
        self.play(ReplacementTransform(exemplo, application_title))
        self.wait()
        self.play(Write(ode_problem))
        self.wait()
        self.play(Write(tfc), ReplacementTransform(ode_problem, integrating))
        self.wait()
        self.play(TransformMatchingTex(integrating, integral_transformation))
        self.wait()
        self.play(Write(text2))
        self.wait()
        self.play(Write(operator_definition))
        self.wait(3)

        # Closing with a reflection
        reflection = Tex(
            r"Assim, resolver o problema de valor inicial equivale\\ a encontrar um ponto de $T$ em que $Tu = u$."
        ).next_to(application_title, DOWN, buff=1)
        self.play(
            ReplacementTransform(operator_definition, reflection),
            FadeOut(VGroup(tfc, text2, integral_transformation)),
        )
        self.wait(3)

        # Clear screen for the next part
        self.play(
            FadeOut(
                VGroup(
                    application_title,
                    reflection,
                )
            )
        )

        # Summary
        summary = VGroup(
            Text("Neste trabalho, apresentaremos:", font_size=36),
            Tex(r"1. Teorema de Ponto Fixo de Banach"),
            Tex(r"2. Teorema de Ponto Fixo de Brouwer"),
            Tex(r"3. Teorema de Ponto Fixo de Schauder"),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        summary.next_to(title, DOWN, buff=1)

        for item in summary:
            self.play(Write(item))
            self.wait(0.5)
        self.wait(3)

        sub_summary = VGroup(
            Text("E comentaremos sobre:", font_size=36),
            Tex(r"1. Teorema de Ponto Fixo de Schaffer"),
            Tex(r"2. Teorema de Ponto Fixo de Krasnoselskii"),
            Tex(r"3. Teorema da Função Implícita e Inversa"),
            Tex(r"4. Teorema de Picard-Lindelöf"),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)

        # replace the summary with the sub_summary
        self.play(ReplacementTransform(summary, sub_summary))

        self.wait(4)

        objetivos = VGroup(
            Tex(r"Objetivos:", font_size=36),
            Tex(r"1. Estudar análise funcional e teoria de pontos fixos"),
            Tex(r"2. Estudar EDPs elípticas"),
            Tex(
                r"3. Compilar os principais resultados de pontos \\ fixos e suas aplicações em um texto em língua portuguesa"
            ),
        )
        self.play(ReplacementTransform(sub_summary, objetivos))

        self.play(FadeOut(*self.mobjects))
