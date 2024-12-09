from manim import *


class SchauderFixedPoint(Scene):
    def construct(self):
        # Title
        title = Text("Teorema do Ponto Fixo de Schauder", font_size=40)
        title.to_edge(UP)
        self.play(Write(title))

        # Theorem statement
        theorem = VGroup(
            Tex(r"Seja $K \subset X$ um conjunto compacto e convexo e"),
            Tex(r"$T: K \to K$ é contínuo."),
            Tex(r"Então $T$ possui um ponto fixo em $K$."),
        ).arrange(DOWN)
        theorem.next_to(title, DOWN, buff=0.5)
        self.play(Write(theorem))
        self.wait(2)
        self.play(FadeOut(theorem))

        # Step 1: Finite Cover
        step1_title = Text("Passo 1: Cobertura Finita", font_size=36)
        step1_title.next_to(title, DOWN, buff=1)

        cover_explanation = VGroup(
            Tex(r"Como $K$ é compacto, existe uma cobertura finita:"),
            MathTex(r"K \subset \bigcup_{i=1}^{n}B(u_{i},\varepsilon)"),
            Tex(r"para pontos $u_1, u_2, ..., u_n$ e $\varepsilon > 0$"),
        ).arrange(DOWN)
        cover_explanation.next_to(step1_title, DOWN)

        self.play(Write(step1_title))
        self.play(Write(cover_explanation))
        self.wait(2)

        # Step 2: Convex Hull
        step2_title = Text("Passo 2: Envoltório Convexo", font_size=36)
        step2_title.next_to(title, DOWN, buff=1)

        convex_hull = VGroup(
            Tex(
                r"Definimos $K_{\varepsilon}$ como envoltório convexo de $\{u_1,...,u_n\}$:"
            ),
            MathTex(
                r"K_{\varepsilon} = \left\{ \sum_{i=1}^{n}\lambda_{i}u_{i}; \sum_{i=1}^{n}\lambda_{i}=1, 0 \leq \lambda_{i} \leq 1 \right\}."
            ),
            Tex(r"Note que $K_{\varepsilon} \subset K$, pois $K$ é convexo."),
        ).arrange(DOWN)
        convex_hull.next_to(step2_title, DOWN)

        self.play(
            ReplacementTransform(step1_title, step2_title),
            ReplacementTransform(cover_explanation, convex_hull),
        )
        self.wait(3)

        # Step 3: Definition of φᵢ
        step3_title = Text("Passo 3: Funções Auxiliares", font_size=36)
        step3_title.next_to(title, DOWN, buff=1)
        phi_definition = VGroup(
            Tex(r"Definimos $\phi_{i}: K \to \mathbb{R}$:"),
            MathTex(
                r"\phi_{i}(u) = \begin{cases} \varepsilon - d(u, u_{i}), & u \in B(u_{i}, \varepsilon) \\ 0, & u \notin B(u_{i}, \varepsilon), \end{cases}"
            ),
        ).arrange(DOWN)

        self.play(
            ReplacementTransform(step2_title, step3_title),
            ReplacementTransform(convex_hull, phi_definition),
        )
        self.wait(2)
        # Step 4: Projection Operator
        step4_title = Text("Passo 4: Operador de Projeção", font_size=36)
        step4_title.next_to(title, DOWN, buff=1)

        # First create and show projection_def in center
        proj = MathTex(
            r"{{P_{\varepsilon}(u)}}",
            "=",
            r"{{ \sum_{i=1}^{n}}} {{\frac{\phi_{i}(u)}{\phi(u)} }} {{u_{i} }}",
        )

        projection_def = VGroup(
            Tex(r"Definimos $P_{\varepsilon}: K \to K_{\varepsilon}$:"),
            proj,
            Tex(r"onde $\phi(u) = \sum_{i=1}^{n}\phi_{i}(u)$"),
        ).arrange(DOWN)

        projection_def
        projection_def.move_to(ORIGIN)  # Start in center

        self.play(
            ReplacementTransform(step3_title, step4_title),
            ReplacementTransform(phi_definition, projection_def),
        )
        self.wait(2)

        self.play(
            projection_def.animate.scale(0.8),
            projection_def.animate.to_edge(LEFT, buff=1),
        )
        self.wait(1)

        # Create and show properties on right
        projection_properties = Tex(
            r"""\begin{enumerate}
                    \item Perceba que $\phi_{i}$ é a distância de um ponto \\ $u \in K$ ao conjunto $K - B(u_{i}, \varepsilon);$ \\
                    \item $\phi(u) > 0$ para todo $u \in K$; \\
                    \item Portanto, $P_{\varepsilon}(u) \in K_{\varepsilon}$ para todo $u \in K$, \\ com $P_{\varepsilon}$ contínua.  
                \end{enumerate}""",
        )
        projection_properties.scale(0.7)
        projection_properties.next_to(step4_title, DOWN).to_edge(RIGHT, buff=0.5)

        self.play(Write(projection_properties))
        self.wait(3)

        self.play(
            FadeOut(projection_def[0]),
            FadeOut(projection_def[2]),
            FadeOut(projection_properties),
            FadeOut(step4_title),
        )

        eq1 = MathTex(
            r"{{P_{\varepsilon}(u)}} - {{u}}",
            "=",
            r"{{\sum_{i=1}^{n} }} {{\frac{\phi_{i}(u) }{\phi(u)} }} {{u_{i} }}",
            "-",
            "u",
        )

        # Move proj to the center again
        self.play(proj.animate.move_to(ORIGIN))

        # Transform proj into eq1
        self.play(TransformMatchingTex(proj, eq1))
        self.wait(2)

        # First, create equations with isolated parts for better matching

        # First, create equations with isolated parts for better matching
        eq2 = MathTex(
            r"\|{{P_{\varepsilon}(u)}} - {{u}}\|",
            "=",
            r"{{\biggm\lvert\biggm\lvert}}",
            r"{{\sum_{i=1}^{n} }} {{\frac{\phi_{i}(u) }{\phi(u)} }} {{u_{i} }}",
            "-",
            "{{u}}",
            r"{{\biggm\lvert\biggm\lvert}}",
        )

        eq3 = MathTex(
            r"\|{{P_{\varepsilon}(u)}} - {{u}}\|",
            "=",
            r"{{\biggm\lvert\biggm\lvert}}",
            r"{{\sum_{i=1}^{n}}} {{\frac{\phi_{i}(u) }{\phi(u)} }} {{u_{i} }}",
            "-",
            r"{{\frac{\phi(u)}{\phi(u)} }}",
            "{{u}}",
            r"{{\biggm\lvert\biggm\lvert}}",
        )

        eq4 = MathTex(
            r"\|{{P_{\varepsilon}(u)}} - {{u}}\|",
            "=",
            r"{{\biggm\lvert\biggm\lvert}}",
            r"{{\sum_{i=1}^{n}}} {{\frac{\phi_{i}(u) }{\phi(u)} }} {{u_{i} }}",
            "-",
            r"{{\sum_{i=1}^{n}}} {{\frac{\phi_{i}(u) }{\phi(u)} }}",
            "{u}",
            r"{{\biggm\lvert\biggm\lvert}}",
        )

        eq5 = MathTex(
            r"\|{{P_{\varepsilon}(u)}} - {{u}}\|",
            "=",
            r"{{\biggm\lvert\biggm\lvert}}",
            r"{{\sum_{i=1}^{n}}} {{\frac{\phi_{i}(u) }{\phi(u)} }} ({{u_{i} }} - {{u}})",
            r"{{\biggm\lvert\biggm\lvert}}",
        )

        eq6 = MathTex(
            r"\|{{P_{\varepsilon}(u)}} - {{u}}\|",
            r"\leq",
            r"{{\sum_{i=1}^{n}}} {{\frac{\phi_{i}(u) }{\phi(u)} }} ",
            r"{{\| {{u_{i} }} - {{u}} \|}}",
        )

        eq7 = MathTex(
            r"\|{{P_{\varepsilon}(u)}} - {{u}}\|",
            r"\leq",
            r"{{\sum_{i=1}^{n}}} {{\frac{\phi_{i}(u) }{\phi(u)} }}",
            r"\varepsilon < {{\varepsilon}}",
        )

        eq8 = MathTex(
            r"\|{{P_{\varepsilon}(u)}} - {{u}}\|",
            "<",
            r"{{\varepsilon}}",
        )

        # Animate transformations
        self.play(TransformMatchingTex(eq1, eq2))
        self.wait(1)
        self.play(TransformMatchingTex(eq2, eq3))
        self.wait(1)
        self.play(TransformMatchingTex(eq3, eq4))
        self.wait(1)
        self.play(TransformMatchingTex(eq4, eq5))
        self.wait(1)
        self.play(TransformMatchingTex(eq5, eq6))
        self.wait(1)
        self.play(TransformMatchingTex(eq6, eq7))
        self.wait(1)
        self.play(TransformMatchingTex(eq7, eq8))
        self.wait(1)

        box1 = SurroundingRectangle(eq8, buff=0.1, color=WHITE)
        self.play(Create(box1))
        explanation_text = Tex(
            r"A desigualdade é clara se $u \in B(u_{i}, \varepsilon)$ e, caso contrário, $\frac{\sum_{i=1}^{n}\phi_{i}(u)}{\phi(u)}=0$"
        )
        explanation_text.scale(0.7)
        explanation_text.next_to(proj, DOWN, buff=0.5)
        self.play(Write(explanation_text))
        self.wait(3)

        # Create new title for final part
        final_title = Text("Conclusão da Demonstração", font_size=36)
        final_title.next_to(title, DOWN, buff=1)

        # Operator definition
        operator_def = Tex(
            r"Considere o operador $T_{\epsilon}: K_{\epsilon} \to K_{\epsilon}$ definido por",
            r"$$T_{\epsilon}(u):= P_{\epsilon}(T(u))$$",
        ).scale(0.8)

        # Dimension explanation
        dim_explanation = Tex(
            r"Como $K_{\epsilon}$ possui dimensão finita $m \leq n$,"
            r" o Teorema do Ponto Fixo de Brouwer, $T_{\epsilon}$ possui um ponto fixo $u_{\epsilon}$.",
        ).scale(0.8)

        # Convergence explanation
        conv_explanation = Tex(
            r"A compacidade de $K$ nos garante que existe uma subsequência ",
            r"$\epsilon_j \to 0$ na qual $u_{\epsilon_j} \to u$, para algum $u \in K$.",
            r"Seja $u_{\epsilon_j} = u_j$ para simplificar a notação.",
        ).scale(0.8)

        de_fato = Text("De fato, temos que").scale(0.7)
        de_fato.next_to(final_title, DOWN, buff=0.5).to_edge(LEFT)

        # Final equations
        eq_final1 = MathTex(
            r"\|{{u_j }}- {{T(u_j)}}\| = \|{{T_j(u_j)}}-{{T(u_j)}}\|",
        )

        eq_final2 = MathTex(
            r"\|{{u_j }}- {{T(u_j) }}\| =  \| {{P_{j}(T(u_{j}))}}  - {{T(u_j) }} \|",
        )

        eq_final3 = MathTex(
            r"\|{{u_j }} - {{T(u_j) }}\| < \epsilon_j",
        )

        explanation = Tex(
            r"Onde a última desigualdade vem do fato que $\|P_{\epsilon}(u) -u \| < \epsilon$.",
            tex_environment="flushleft",
        )

        fin = Tex(
            " Assim, podemos tomar o limite de modo que",
            tex_environment="flushleft",
        )

        eq_final4 = MathTex(
            r"\lim \|{{u_j }}- {{T(u_j)}}\| < \lim \epsilon_j {{\to 0}}"
        ).scale(1.2)
        eq_final5 = MathTex(r"\|\lim {{u_j }}- \lim {{T(u_j)}}\| {{{\to 0}}}").scale(
            1.2
        )
        eq_final6 = MathTex(r"\|u - T(u)\| {{\to 0}}").scale(1.2)
        eq_final7 = MathTex(r"T(u) = u").scale(1.2)

        # Position all elements
        group1 = (
            VGroup(operator_def, dim_explanation, conv_explanation)
            .arrange(DOWN)
            .next_to(final_title, DOWN)
        )

        # Animations
        self.play(Write(final_title))
        self.wait(1)

        self.play(
            ReplacementTransform(eq8, group1), FadeOut(box1), FadeOut(explanation_text)
        )
        self.wait(4)

        self.play(ReplacementTransform(group1, de_fato))

        self.wait(1)
        eq_final1.move_to(ORIGIN)
        eq_final2.move_to(eq_final1)
        eq_final3.move_to(eq_final1)

        explanation.next_to(eq_final3, DOWN, buff=0.5).to_edge(LEFT)

        self.play(Write(eq_final1))
        self.play(TransformMatchingTex(eq_final1, eq_final2))
        self.wait(1.3)
        self.play(TransformMatchingTex(eq_final2, eq_final3))
        self.wait(1.3)
        self.play(Write(explanation))
        self.wait(1.3)

        fin.next_to(final_title, DOWN)

        self.play(
            ReplacementTransform(de_fato, fin),
            ReplacementTransform(eq_final3, fin),
            ReplacementTransform(explanation, fin),
        )

        eq_final4.next_to(fin, DOWN, buff=0.5)
        eq_final5.move_to(eq_final4.get_center())
        eq_final6.move_to(eq_final4.get_center())
        eq_final7.move_to(eq_final4.get_center())
        self.play(Write(eq_final4))
        self.wait(1.3)
        self.play(TransformMatchingTex(eq_final4, eq_final5))
        self.wait(1.3)
        self.play(ReplacementTransform(eq_final5, eq_final6))
        self.wait(1.3)
        self.play(ReplacementTransform(eq_final6, eq_final7))

        box2 = SurroundingRectangle(eq_final7, buff=0.1, color=WHITE)
        self.play(Create(box2))

        self.wait(4)

        # Final fade out
        self.play(*[FadeOut(mob) for mob in self.mobjects])
