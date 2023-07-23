""" Sphere Object Representation """

from Objects.Color import Color


class Sphere:
    """
    Class Representing a Sphere
    """

    def __init__(self, position=None, radius=1.0, color=None, index=1, parent=None) -> None:
        """
        Class representing a Sphere Object.
        :param position: (x,y,z) Example: [0, 0, 0]
        :param radius: Radius of Sphere
        :param color: Color Object
        :param index: (int) Index of Sphere.
        :param parent: Parent of Object.
        """

        if color is None:
            color = Color()
        if position is None:
            position = [0, 0, 0]

        self.position = position
        self.radius = radius
        self.color = color
        self.index = index
        self.parent = parent
