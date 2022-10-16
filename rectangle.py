import numpy as np
from shape import Shape


class Rectangle(Shape):
    """
    RECTANGLE = [
            np.array([-1, -1, 1]), np.array([1, -1, 1]),
            np.array([1, 1, 1]), np.array([-1, 1, 1]),
            np.array([-1, -1, -1]), np.array([1, -1, -1]),
            np.array([1, 1, -1]), np.array([-1, 1, -1])
        ]
    """
    # Rectangle composed of 12 triangles, 36 vertices

    DIMENSION = 3

    RECTANGLE = [
            # South
            np.array([0, 0, 0, 1.0]), np.array([0, 1.0, 0, 1]), np.array([1.0, 1.0, 0, 1.0]),
            np.array([0, 0, 0, 1.0]), np.array([1.0, 1.0, 0, 1.0]), np.array([1.0, 0, 0, 1.0]),

            # East
            np.array([1.0, 0, 0, 1.0]), np.array([1.0, 1.0, 0, 1.0]), np.array([1.0, 1.0, 1.0, 1.0]),
            np.array([1.0, 0, 0, 1.0]), np.array([1.0, 1.0, 1.0, 1.0]), np.array([1.0, 0, 1.0, 1.0]),

            # North
            np.array([1.0, 0, 1.0, 1.0]), np.array([1.0, 1.0, 1.0, 1.0]), np.array([0, 1.0, 1.0, 1.0]),
            np.array([1.0, 0, 1.0, 1.0]), np.array([0, 1.0, 1.0, 1.0]), np.array([0, 0, 1.0, 1.0]),

            # West
            np.array([0, 0, 1.0, 1.0]), np.array([0, 1.0, 1.0, 1.0]), np.array([0, 1.0, 0, 1.0]),
            np.array([0, 0, 1.0, 1.0]), np.array([0, 1.0, 0, 1.0]), np.array([0, 0, 0, 1.0]),

            # Top
            np.array([0, 1.0, 0, 1.0]), np.array([0, 1.0, 1.0, 1.0]), np.array([1.0, 1.0, 1.0, 1.0]),
            np.array([0, 1.0, 0, 1.0]), np.array([1.0, 1.0, 1.0, 1.0]), np.array([1.0, 1.0, 0, 1.0]),

            # Bottom
            np.array([1.0, 0, 1.0, 1.0]), np.array([0, 0, 1.0, 1.0]), np.array([0, 0, 0, 1.0]),
            np.array([1.0, 0, 1.0, 1.0]), np.array([0, 0, 0, 1.0]), np.array([1.0, 0, 0, 1.0])
        ]

    def __init__(self, width, height, depth, pos):
        super().__init__(self.RECTANGLE, pos)
        self.width = width
        self.height = height
        self.depth = depth
        self.volume = width * height * depth
        self.init_rectangle()

    def init_rectangle(self):
        """
        Initializes the 3d rectangle with the given width, height and depth.
        """
        for i in range(len(self.points_3d)):
            for x in range(self.DIMENSION):
                if x == 0:
                    self.points_3d[i][0] *= self.width
                elif x == 1:
                    self.points_3d[i][1] *= self.height
                elif x == 2:
                    self.points_3d[i][2] *= self.depth

        self.update_2d_projection(self.points_3d)

    def flip(self, axis):
        """
        flip the rectangle on the given axis

        axis: string - axis to flip on
        """
        for i in range(len(self.points_3d)):
            self.points_3d[i][0, self.AXES[axis.upper()]] *= -1

        self.update_2d_projection(self.points_3d)



