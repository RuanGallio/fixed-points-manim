from manim import *


class BanachFixedPoint(Scene):
    def construct(self):
        # Title
        title = Text("Ponto fixo de Banach", font_size=40)
        title.to_edge(UP)
        self.play(Write(title))

        # Theorem statement
        theorem = Tex(
            r"Seja $f: X \to X$ uma contração. Então $f$ possui um único ponto fixo $\bar{x} \in X$."
        ).scale(0.8)

        theorem.next_to(title, DOWN, buff=0.5)

        self.play(Write(theorem))
        self.wait(2)
        self.play(FadeOut(theorem))
        self.wait()

        # Part 1: Uniqueness
        uniqueness_title = Text("Unicidade", font_size=36)
        uniqueness_title.next_to(title, DOWN, buff=1)

        u1 = Tex("Sejam $x,y$ são pontos fixos, isso implica que").scale(0.8)
        u2 = MathTex(r"{{d(x,y)}} = d(f(x),f(y))").scale(0.8)
        u3 = MathTex(r"{{d(x,y)}} \leq \lambda d(x,y)").scale(0.8)
        u4 = Tex(
            r"Mas, como $\lambda >0$, isso implica que $d(x,y) = 0 \implies x = y$"
        ).scale(0.8)
        u1.next_to(uniqueness_title, DOWN)
        u2.next_to(u1, DOWN)
        u3.move_to(u2.get_center())
        u4.next_to(u3, DOWN)

        self.play(Write(uniqueness_title))
        self.play(Write(u1))
        self.play(Write(u2))
        self.wait()
        self.play(TransformMatchingTex(u2, u3))
        self.wait()
        self.play(Write(u4))
        self.wait(3)

        # Part 2: Existence - Sequence Construction
        existence_title = Text("Existência", font_size=36)
        existence_title.next_to(title, DOWN, buff=1)

        self.play(ReplacementTransform(uniqueness_title, existence_title))
        e1 = Tex(
            r"Tome $x_0 \in X$ e defina a sequência $(x_n)$ tal que $x_{n+1} = f(x_n)$. \\ Note que",
        ).scale(0.8)

        e1.next_to(existence_title, DOWN)

        self.play(
            ReplacementTransform(u1, e1),
            FadeOut(u3),
            FadeOut(u4),
        )
        self.wait(1)

        # First set of transformations
        e3 = MathTex(r"{{d(x_{n+1},x_{n})}} = {{d(f(x_{n}), f(x_{n-1}))}}").scale(0.8)
        e4 = MathTex(
            r"{{d(x_{n+1},x_{n})}} \leq {{\lambda}} {{d(x_{n}, x_{n-1})}}"
        ).scale(0.8)

        e3.next_to(e1, DOWN)
        e4.move_to(e3)
        self.play(Write(e3))
        self.play(TransformMatchingTex(e3, e4))
        self.wait(1)

        # Show recursive steps with fading previous steps
        steps = [
            r"{{d(x_{n+1},x_{n})}} \leq {{\lambda}} {{d(x_{n}, x_{n-1})}}",
            r"{{d(x_{n+1},x_{n})}} \leq {{\lambda}} {{d(f(x_{n}), f(x_{n-1}))}}",
            r"{{d(x_{n+1},x_{n})}} \leq {{\lambda}}^2 {{d(x_{n-1}, x_{n-2})}}",
            r"{{d(x_{n+1},x_{n})}} \leq {{\lambda}}^2 {{d(f(x_{n-1}), f(x_{n-2}))}}",
            r"{{d(x_{n+1},x_{n})}} \leq {{\lambda}}^3 {{d(x_{n-2}, x_{n-3})}}",
            r"{{d(x_{n+1},x_{n})}} \leq {{\lambda}}^3 {{d(f(x_{n-2}), f(x_{n-3}))}}",
            r"{{d(x_{n+1},x_{n})}} \leq {{\lambda^4}} {{d(x_{n-3}, x_{n-4})}}",
        ]

        current_eq = e4
        for _, step in enumerate(steps[1:], 1):
            next_eq = MathTex(step).scale(0.8)
            next_eq.move_to(current_eq)
            next_eq.move_to(current_eq)

            self.play(TransformMatchingTex(current_eq, next_eq))
            current_eq = next_eq
            self.wait(1)

        # Show dots to indicate continuation
        dots_eq = MathTex(
            r"{{d(x_{n+1},x_{n})}} \leq {{\lambda}}^4 {{d(x_{n-3}, x_{n-4})}} \leq \cdots"
        ).scale(0.8)
        dots_eq.move_to(current_eq)
        self.play(TransformMatchingTex(current_eq, dots_eq))
        self.wait()

        # Final form
        final_eq1 = MathTex(
            r"{{d(x_{n+1},x_{n})}} \leq {{\lambda^n}} {{d(x_1, x_0)}}"
        ).scale(0.8)
        final_eq2 = MathTex(
            r"{{d(x_{n+1},x_{n})}} \leq {{\lambda^n}} {{d(f(x_0), x_0)}}"
        ).scale(0.8)
        final_eq1.move_to(dots_eq)
        final_eq2.move_to(dots_eq)

        # Add a small arrow or indicator
        arrow = Arrow(
            dots_eq.get_right() + RIGHT * 0.5, dots_eq.get_right() + RIGHT * 1.5
        )
        text = Text("n passos", font_size=24).next_to(arrow, UP, buff=0.1)

        self.play(Create(arrow), Write(text))
        self.wait()

        self.play(
            TransformMatchingTex(dots_eq, final_eq1), FadeOut(arrow), FadeOut(text)
        )
        self.wait()
        self.play(TransformMatchingTex(final_eq1, final_eq2))
        self.wait(3)

        dt = Tex(
            "Assim, sejam $n,m \in \mathbb{N}$ tais que $n < m$. Da desigualdade triangular"
        ).scale(0.8)
        dt.move_to(e1.get_center())

        eq0 = MathTex(
            r"d(x_{n},x_{m}) \leq d(x_{n}, x_{n+1})+d(x_{n+1},x_{n+2})+\dots+d(x_{m-1},x_{m}),"
        ).scale(0.8)
        eq0.next_to(dt, DOWN)

        self.play(ReplacementTransform(e1, dt))
        self.play(ReplacementTransform(final_eq2, eq0))

        self.wait(3)

        eq1 = MathTex(
            r"d(x_{n},x_{m}) \leq \lambda^{n}d(f(x_{0}),x_{0}) + \lambda^{n+1}d(f(x_{0}),x_{0}) + \cdots + \lambda^{m-1}d(f(x_{0}),x_{0})",
            substrings_to_isolate=[r"\lambda", r"d(f(x_{0}),x_{0})"],
        ).scale(0.7)

        eq1.move_to(eq0.get_center())

        # Second equation (factored d(f(x_0),x_0))
        eq2 = MathTex(
            r"=(\lambda^{n}+\lambda^{n+1}+\cdots+\lambda^{m-1})d(f(x_{0}),x_{0})",
            substrings_to_isolate=[r"\lambda", r"d(f(x_{0}),x_{0})"],
        ).scale(0.7)
        eq2.next_to(eq1, DOWN)

        # Final equation (factored λⁿ)
        eq3 = MathTex(
            r"= \lambda^{n}",
            r" (1+\lambda+\cdots+\lambda^{m-n-1})",
            r" d(f(x_{0}),x_{0})",
        ).scale(0.7)
        eq3.next_to(eq2, DOWN, buff=0.5)

        # Display initial equation
        self.play(Transform(eq0, eq1))
        self.play(eq1.animate.set_color_by_tex("d(f(x_{0}),x_{0})", YELLOW))

        self.play(Write(eq2))
        self.play(eq2.animate.set_color_by_tex(r"d(f(x_{0}),x_{0})", YELLOW))
        self.play(eq2.animate.set_color_by_tex(r"\lambda", BLUE))

        self.play(Write(eq3))

        # Highlight final structure
        self.play(
            eq3[0].animate.set_color(BLUE),
            eq3[1].animate.set_color(GREEN),
            eq3[2].animate.set_color(YELLOW),
            run_time=1,
        )

        # Create power series and explanation
        series = MathTex(r"\left(\sum_{i=0}^{\infty}\lambda^{i}\right)")

        eq4 = MathTex(
            r"< \lambda^{n}",
            series.get_tex_string(),
            eq3[2].get_tex_string(),
        ).scale(0.7)

        eq4[0].set_color(BLUE)
        eq4[1].set_color(GREEN)
        eq4[2].set_color(YELLOW)

        eq5 = MathTex(
            eq4[0].get_tex_string(),
            r"\frac{1}{1-\lambda}",
            eq4[2].get_tex_string(),
        ).scale(0.7)

        eq5[0].set_color(BLUE)
        eq5[1].set_color(GREEN)
        eq5[2].set_color(YELLOW)

        eq6 = MathTex(
            r"=",
            r"\frac{\lambda^{n}}{1-\lambda}",
            r"d(f(x_{0}),x_{0})",
        ).scale(0.7)

        explanation = MathTex(
            r"\text{Como }0<\lambda<1\text{, note que}",
            r"(1+\lambda+\dots+\lambda^{m-n-1})",
            r"<",
            r"\sum_{i=0}^{\infty}\lambda^{i}",
            r"=",
            r"\frac{1}{1-\lambda}",
        )
        explanation.scale(0.8)  # Make it slightly smaller

        # Position the series where eq3[1] is
        eq4.move_to(eq3)
        eq5.move_to(eq3)
        eq6.move_to(eq3)

        # Position explanation
        explanation.next_to(eq3, DOWN, buff=1)

        # Animate transformation and explanation
        self.play(Transform(eq3, eq4), Write(explanation), run_time=2)
        self.wait()
        self.play(Transform(eq3, eq5), run_time=2)
        self.wait()

        self.play(Transform(eq3, eq6), run_time=2)

        self.wait()

        # Fade out previous equations and the box
        self.play(
            FadeOut(dt), FadeOut(eq0), FadeOut(eq1), FadeOut(eq2), FadeOut(explanation)
        )

        # Shift eq6 up by 2 and transform it to eq7
        eq7 = Tex(
            r"$d(x_n, x_m) < \dfrac{\lambda^{n}}{1-\lambda}d(f(x_0), x_0) \to 0$ quando $n \to \infty$"
        ).scale(0.8)
        eq7.move_to(eq3.get_center() + UP * 2)

        self.play(ReplacementTransform(eq3, eq7), run_time=2)
        self.wait()

        # Add explanatory text about the sequence being Cauchy
        final_argument = VGroup(
            Tex("Portanto, a sequência $(x_n)$ é de Cauchy.").scale(0.8),
            Tex(
                r"Como $X$ é completo, a sequência converge para um ponto fixo $\bar{x}$."
            ).scale(0.8),
            Tex("Como $f$ é contínua, temos que").scale(0.8),
        ).arrange(DOWN)
        eq8 = MathTex(
            r"f(\bar{x}) = f(\lim_{n \to \infty} x_n) = \lim_{n \to \infty} f(x_n) = \lim_{n \to \infty} x_{n+1} = \bar{x}"
        ).scale(0.8)
        eq8.next_to(existence_title, DOWN, buff=0.5)

        final_eq = MathTex(r"f(\bar{x}) = \bar{x}").scale(0.8)
        final_eq.move_to(eq8)

        final_argument.next_to(eq8, DOWN, buff=0.5)
        self.play(Write(final_argument))

        self.play(
            ReplacementTransform(eq7, eq8),
            FadeOut(final_argument),
        )
        # transform eq8 to final_eq and then create a box around it
        self.wait(1.3)
        self.play(Transform(eq8, final_eq))
        box = SurroundingRectangle(eq8, buff=0.1, color=WHITE)
        self.play(Create(box))

        self.wait(2)

        # Fade out everything
        self.play(*[FadeOut(mob) for mob in self.mobjects])
