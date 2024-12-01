from manim import *

class BrouwerFixedPoint(Scene):
    def construct(self):
        # Title
        title = Text("Teorema de ponto fixo de Brouwer", font_size=48)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))
        
        # Draw the unit disk
        disk = Circle(radius=2, color=BLUE)
        disk.set_fill(color=BLUE, opacity=0.1)
        self.play(Create(disk))
        
        # Add grid points inside the disk
        grid_points = VGroup()
        for x in range(-5, 6):
            for y in range(-5, 6):
                if x**2 + y**2 <= 25:  # Inside the unit disk (radius 2)
                    point = Dot(point=[x*0.4, y*0.4, 0], radius=0.05, color=YELLOW) if not (x ==0 and y == 0) else Dot(point=[x*0.4, y*0.4, 0], radius=0.05, color=RED)
                    grid_points.add(point)
        self.play(FadeIn(grid_points))
        
        # Define the transformation function
        def transform_func(p):
            x, y, _ = p
            # Rotate and slightly scale towards origin
            new_x = 0.5 * (x * 0.866 - y * 0.5)  # cos(30°), -sin(30°)
            new_y = 0.5 * (x * 0.5 + y * 0.866)  # sin(30°), cos(30°)
            return [new_x, new_y, 0]
        
        # Animate the transformation
        self.play(
            Transform(grid_points, grid_points.copy().apply_function(transform_func)),
            run_time=4
        )
        
        # Highlight the fixed point
        fixed_point = Dot(point=[0,0, 0], radius=0.1, color=RED)
        fixed_label = Text("Ponto fixo", font_size=24).next_to(fixed_point, UP)
        self.play(GrowFromCenter(fixed_point), Write(fixed_label))
        
        # Final message
        conclusion = Text(
            "Toda função contínua na bola possui um ponto",
            font_size=32,
            color=WHITE
        ).to_edge(DOWN)
        self.play(Write(conclusion))
        self.wait(3)
