from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """
    Represents a King, inheriting traits from both Baratheon and Lannister families.
    """

    def __init__(self, first_name, is_alive=True):
        """
        Initializes a King with Baratheon family traits by default.
        """
        super().__init__(first_name, is_alive)
        self.family_name = 'Baratheon'
        self.eyes = 'brown'
        self.hairs = 'dark'

    def set_eyes(self, eyes_color):
        """
        Sets the eye color of the King.
        """
        self.eyes = eyes_color

    def set_hairs(self, hair_color):
        """
        Sets the hair color of the King.
        """
        self.hairs = hair_color

    def get_eyes(self):
        """
        Gets the current eye color of the King.
        """
        return self.eyes

    def get_hairs(self):
        """
        Gets the current hair color of the King.
        """
        return self.hairs

    def __str__(self):
        """
        Returns a string representation of the King's family name, eye color, and hair color.
        """
        return str((self.family_name, self.eyes, self.hairs))

    def __repr__(self):
        """
        Returns a formal string representation of the King's family name, eye color, and hair color.
        """
        return str((self.family_name, self.eyes, self.hairs))
