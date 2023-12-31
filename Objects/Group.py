""" Group Object Representation """


class Group:
    """
    Class Representing a Group of Objects
    """

    def __init__(self, objects=None, parent=None, translation=None, rotation=None, scaling=None) -> None:
        """
        Class representing a Group of Objects.

        :param parent: Parent of Object.
        """

        if objects is None:
            objects = []

        self.objects = objects
        self.parent = parent

        # Special Attributes
        self.translation = translation
        self.rotation = rotation
        self.scaling = scaling

        # Very special attribute
        self.special = "union"

    def check_if_default(self, variable, name) -> bool:
        """
        Checks if a given parameter of a sphere is a default value.
        :param variable: (Example: self . position) Must be a variable in sphere.
        :param name: Name/Variable Name of the variable to check.
        :return: True if default and false if not.
        """

        print(f"Debug Log: {self} is checking for {name} if default.")

        if name == "translation":
            if variable == [0, 0, 0]:
                return True
            else:
                return False

        elif name == "rotation":
            if variable == [0, 0]:
                return True
            else:
                return False

        elif name == "scaling":
            if variable == [0, 0, 0]:
                return True
            else:
                return False

        else:
            print(f"Medium Error: Cannot recognize {name} if it is part of the object.")
            return False
