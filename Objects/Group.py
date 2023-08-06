""" Group Object Representation """


class Group:
    """
    Class Representing a Group of Objects
    """

    def __init__(self, objects=None, parent=None) -> None:
        """
        Class representing a Group of Objects.

        :param parent: Parent of Object.
        """

        if objects is None:
            objects = []

        self.objects = objects

        self.parent = parent