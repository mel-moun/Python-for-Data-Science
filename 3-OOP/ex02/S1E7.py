from S1E9 import Character


class Baratheon(Character):
    """
    Represents a member of the Baratheon family, inheriting from the Character class.
    """

    def __init__(self, first_name, is_alive=True):
        """
        Initializes a Baratheon family member with default physical traits and a family name.
        """
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = 'Baratheon'
        self.eyes = 'brown'
        self.hairs = 'dark'

    def die(self):
        """
        Marks the Baratheon family member as no longer alive.
        """
        self.is_alive = False

    def __str__(self):
        """
        Returns a string representation of the Baratheon family member's traits.
        """
        return str((self.family_name, self.eyes, self.hairs))

    def __repr__(self):
        """
        Returns a formal string representation of the Baratheon family member's traits.
        """
        return str((self.family_name, self.eyes, self.hairs))


class Lannister(Character):
    """
    Represents a member of the Lannister family, inheriting from the Character class.
    """

    def __init__(self, first_name, is_alive=True):
        """
        Initializes a Lannister family member with default physical traits and a family name.
        """
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = 'Lannister'
        self.eyes = 'blue'
        self.hairs = 'light'

    def die(self):
        """
        Marks the Lannister family member as no longer alive.
        """
        self.is_alive = False

    def __str__(self):
        """
        Returns a string representation of the Lannister family member's traits.
        """
        return str((self.family_name, self.eyes, self.hairs))

    def __repr__(self):
        """
        Returns a formal string representation of the Lannister family member's traits.
        """
        return str((self.family_name, self.eyes, self.hairs))

    @classmethod
    def create_lannister(cls, first_name, is_alive):
        """
        Creates a new Lannister family member instance.
        """
        return Lannister(first_name, is_alive)
