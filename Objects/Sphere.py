""" Sphere Object Representation """

from Objects.Color import Color


class Sphere:
    """
    Class Representing a Sphere
    """

    def __init__(self, position=None, radius=1.0, color=None, index=1, parent=None, translation=None, rotation=None,
                 scaling=None) -> None:
        """
        Class representing a Sphere Object.
        :param position: (X, y, z) Example: [0, 0, 0]
        :param radius: Radius of Sphere
        :param color: Color Object
        :param index: (int) Index of Sphere.
        :param parent: Parent of Object.
        """

        if color is None:
            color = Color()
        if position is None:
            position = [0, 0, 0]
        if radius is None:
            radius = 1.0
        if index is None:
            index = 1

        self.position = position
        self.radius = radius
        self.color = color
        self.index = index
        self.parent = parent

        # Special Attributes
        self.translation = translation
        self.rotation = rotation
        self.scaling = scaling

    def check_if_default(self, variable) -> bool:
        """
        Checks if a given parameter of a sphere is a default value.
        :param variable: (Example: self . position) Must be a variable in sphere.
        :return: True if default and false if not.
        """

        if variable is self.position:
            if variable == [0, 0, 0]:
                return True
            else:
                return False

        elif variable is self.radius:
            if variable == 1.0:
                return True
            else:
                return False

        elif variable is self.index:
            if variable == 1:
                return True
            else:
                return False

        elif variable is self.parent:
            if variable is None:
                return True
            else:
                return False

        elif variable is self.color:
            if variable == Color():
                return True
            else:
                return False

        elif variable is self.translation:
            if variable is None:
                return True
            else:
                return False

        elif variable is self.rotation:
            if variable is None:
                return True
            else:
                return False

        elif variable is self.scaling:
            if variable is None:
                return True
            else:
                return False

        else:
            return False
