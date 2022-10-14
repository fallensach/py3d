import numpy as np
from shape import Shape


class Rectangle(Shape):
    """
    RECTANGLE = [
            np.matrix([-1, -1, 1]), np.matrix([1, -1, 1]),
            np.matrix([1, 1, 1]), np.matrix([-1, 1, 1]),
            np.matrix([-1, -1, -1]), np.matrix([1, -1, -1]),
            np.matrix([1, 1, -1]), np.matrix([-1, 1, -1])
        ]
    """
    # Rectangle composed of 12 triangles, 36 vertices
    RECTANGLE = [
            # South
            np.matrix([0, 0, 0, 1]), np.matrix([0, 1, 0, 1]), np.matrix([1, 1, 0, 1]),
            np.matrix([0, 0, 0, 1]), np.matrix([1, 1, 0, 1]), np.matrix([1, 0, 0, 1]),

            # East
            np.matrix([1, 0, 0, 1]), np.matrix([1, 1, 0, 1]), np.matrix([1, 1, 1, 1]),
            np.matrix([1, 0, 0, 1]), np.matrix([1, 1, 1, 1]), np.matrix([1, 0, 1, 1]),

            # North
            np.matrix([1, 0, 1, 1]), np.matrix([1, 1, 1, 1]), np.matrix([0, 1, 1, 1]),
            np.matrix([1, 0, 1, 1]), np.matrix([0, 1, 1, 1]), np.matrix([0, 0, 1, 1]),

            # West
            np.matrix([0, 0, 1, 1]), np.matrix([0, 1, 1, 1]), np.matrix([0, 1, 0, 1]),
            np.matrix([0, 0, 1, 1]), np.matrix([0, 1, 0, 1]), np.matrix([0, 0, 0, 1]),

            # Top
            np.matrix([0, 1, 0, 1]), np.matrix([0, 1, 1, 1]), np.matrix([1, 1, 1, 1]),
            np.matrix([0, 1, 0, 1]), np.matrix([1, 1, 1, 1]), np.matrix([1, 1, 0, 1]),

            # Bottom
            np.matrix([1, 0, 1, 1]), np.matrix([0, 0, 1, 1]), np.matrix([0, 0, 0, 1]),
            np.matrix([1, 0, 1, 1]), np.matrix([0, 0, 0, 1]), np.matrix([1, 0, 0, 1])
        ]

    DIMENSION = 3

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
                    self.points_3d[i][0, 0] *= self.width
                elif x == 1:
                    self.points_3d[i][0, 1] *= self.height
                elif x == 2:
                    self.points_3d[i][0, 2] *= self.depth

        self.update_2d_projection()

    def flip(self, axis):
        """
        flip the rectangle on the given axis

        axis: string - axis to flip on
        """
        for i in range(len(self.points_3d)):
            self.points_3d[i][0, self.AXES[axis.upper()]] *= -1

        self.update_2d_projection()



