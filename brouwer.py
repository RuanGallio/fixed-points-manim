from manim import *
import numpy as np

# import csv


class BrouwerFixedPointPoints(Scene):
    def construct(self):
        # Create the xy-plane
        plane = NumberPlane(
            x_range=[-5, 1.5, 0.5],
            y_range=[-4, 4, 0.5],
            background_line_style={"stroke_color": BLUE},
        )
        plane.scale_to_fit_height(self.camera.frame_height)
        plane.scale_to_fit_width(self.camera.frame_width)

        # Define the function information in multiple parts for better layout
        function_label = MathTex(
            r"\psi: B^2(0,1) \to B^2(0,1)",
        )
        function_formula = MathTex(
            r"\psi(x,y) = \begin{bmatrix}"
            r"0.7\sqrt{x^2 + y^2}(1 + 0.32\sin(3\tan^{-1}(\frac{y}{x})))\cos(\tan^{-1}(\frac{y}{x})) + 0.06 \\"
            r"0.7\sqrt{x^2 + y^2}(1 + 0.32\sin(3\tan^{-1}(\frac{y}{x})))\sin(\tan^{-1}(\frac{y}{x})) - 0.05"
            r"\end{bmatrix}",
        )

        # Scale all labels
        function_label.scale(0.5)
        function_formula.scale(0.48)

        # Position labels in the center of the rectangle
        label_group = VGroup(function_label, function_formula)
        label_group.arrange(DOWN, aligned_edge=LEFT, buff=0.1)

        # Add semi-transparent background
        background = Rectangle(
            width=label_group.width + 0.5,
            height=self.camera.frame_height,
            fill_color=BLACK,
            fill_opacity=1,
            stroke_width=0,
        )
        background.to_edge(LEFT)

        # Center the label group in the rectangle
        label_group.move_to(background.get_center())

        # Create final group with background
        final_label_group = VGroup(background, label_group)

        self.play(FadeIn(final_label_group))
        self.wait(1)

        def psi(x, y):
            r = np.sqrt(x**2 + y**2)
            theta = np.arctan2(y, x)
            new_r = 0.7 * r * (1 + 0.32 * np.sin(3 * theta))
            x_mapped = new_r * np.cos(theta) + 0.06
            y_mapped = new_r * np.sin(theta) - 0.05
            return np.array([x_mapped, y_mapped, 0])

        # Rest of the code remains the same...
        num_points = 3000
        points = []
        original_coords = []
        mapped_coords = []
        for _ in range(num_points):
            r = np.sqrt(np.random.uniform(0, 1))
            theta = np.random.uniform(0, 2 * np.pi)
            x, y = r * np.cos(theta), r * np.sin(theta)
            point = Dot(plane.c2p(x, y), radius=0.04)
            points.append(point)
            original_coords.append([x, y])
            mapped = psi(x, y)
            mapped_coords.append(mapped[:2])

        possible_FP = [[0, 0], [0.06, -0.05], [0.1210, -0.1010]]

        for x, y in possible_FP:
            point = Dot(plane.c2p(x, y), radius=0.04)
            points.append(point)
            original_coords.append([x, y])
            mapped = psi(x, y)
            mapped_coords.append(mapped[:2])

        distances = [
            np.linalg.norm(np.array(orig) - np.array(mapped))
            for orig, mapped in zip(original_coords, mapped_coords)
        ]

        max_distance = max(distances)
        min_distance = min(distances)
        print(f"Max distance: {max_distance}, Min distance: {min_distance}")
        distance_range = (
            max_distance - min_distance if max_distance != min_distance else 1
        )

        for point, distance in zip(points, distances):
            if distance < 0.001:
                point.set_color(TEAL_C)
                point.scale(2)
            else:
                norm_distance = (distance - min_distance) / distance_range
                color = interpolate_color(RED_C, BLUE_C, norm_distance)
                point.set_color(color)

        original_ball = Circle(radius=1, color=BLUE, fill_opacity=0.1)
        original_ball.move_to(plane.c2p(0, 0))
        original_ball.scale_to_fit_width(2 * plane.x_axis.get_unit_size())
        original_ball.scale_to_fit_height(2 * plane.y_axis.get_unit_size())

        self.play(Create(original_ball))
        self.play(
            LaggedStartMap(Create, points, lag_ratio=0.05),
            run_time=3,
        )
        self.wait(0.3)

        animations = []
        for point, mapped in zip(points, mapped_coords):
            animations.append(point.animate.move_to(plane.c2p(mapped[0], mapped[1])))

        self.play(AnimationGroup(*animations, lag_ratio=0.05, run_time=5))
        self.wait(2)
