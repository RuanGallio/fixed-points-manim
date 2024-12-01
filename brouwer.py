from manim import *


class BrouwerFixedPointVisualization(Scene):
    def construct(self):
        # create the xy-plane
        plane = NumberPlane(
            x_range=[-7, 7, 1],
            y_range=[-7, 7, 1],
            background_line_style={"stroke_color": BLUE},
        )
        plane.scale_to_fit_height(self.camera.frame_height)
        plane.scale_to_fit_width(self.camera.frame_width)

        # Extract components
        x_axis = plane.get_x_axis()
        y_axis = plane.get_y_axis()
        grid_lines = plane.get_background_lines()

        # 2. Animate the grid lines with a fade-in effect
        self.play(
            LaggedStartMap(FadeIn, grid_lines, lag_ratio=0.05),
            run_time=3,
        )
        self.wait(0.2)

        # 1. Animate the creation of axes
        self.play(
            Create(x_axis),
            Create(y_axis),
            run_time=2,
            rate_func=smooth,
        )
        self.wait(0.2)

        # 4. Add labels to axes
        x_label = plane.get_x_axis_label("x", direction=UP * 0.5)
        y_label = plane.get_y_axis_label("y", direction=RIGHT * 0.5)
        x_label.scale(0.75)
        y_label.scale(0.75)
        self.play(FadeIn(x_label), FadeIn(y_label), run_time=1.5)
        self.wait(1)

        circle = Circle(radius=5, color=RED, stroke_width=2)
        circle.move_to(ORIGIN)
        self.play(Create(circle), run_time=2)

        def vector_field_func(point):
            

        def get_color_by_norm(norm, max_norm):
            return interpolate_color(BLUE, RED, norm / max_norm)

        # Calculate max norm for normalization
        max_norm = max(
            np.linalg.norm(vector_field_func(np.array([x, y, 0])))
            for x in np.arange(-5, 5, 1)
            for y in np.arange(-5, 5, 1)
        )

        vector_field = VGroup()
        for x in np.arange(-7, 7, 1):
            for y in np.arange(-7, 7, 1):
                point = np.array([x, y, 0])
                vector = vector_field_func(point)
                vector_length = np.linalg.norm(vector)
                if (
                    vector_length != 0 and vector_length <= 5
                ):  # Skip zero-length vectors
                    color = get_color_by_norm(
                        vector_length, max_norm
                    )  # Get color by norm
                    arrow = Arrow(
                        start=point,
                        end=point
                        + 0.5 * vector / vector_length,  # Normalize and scale vector
                        buff=0,
                        stroke_width=2,
                        color=color,  # Apply gradient color
                    )
                    vector_field.add(arrow)

                # Animate vector field creation with a smooth appearance
        self.play(LaggedStartMap(GrowArrow, vector_field, lag_ratio=0.05), run_time=4)
        self.wait(2)
