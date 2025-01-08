from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""
    def __init__(self, first_name, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = 'Baratheon'
        self.eyes = 'brown'
        self.hairs = 'dark'

    def die(self):
        self.is_alive = False

    def __str__(self):
        return str((self.family_name, self.eyes, self.hairs))

    def __repr__(self):
        return str((self.family_name, self.eyes, self.hairs))

class Lannister(Character):
    """Representing the Baratheon family."""
    def __init__(self, first_name, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = 'Lannister'
        self.eyes = 'blue'
        self.hairs = 'light'
    
    def __str__(self):
        return str((self.family_name, self.eyes, self.hairs))

    def __repr__(self):
        return str((self.family_name, self.eyes, self.hairs))

    def die(self):
        self.is_alive = False