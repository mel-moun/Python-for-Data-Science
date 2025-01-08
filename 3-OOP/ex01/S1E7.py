from S1E9 import Character


class Baratheon(Character):
    def __init__(self, first_name, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = 'Baratheon'
        self.eyes = 'brown'
        self.hairs = 'dark'

    def die():
        super().die()

    def __str__(self):
        return str((self.family_name, self.eyes, self.hairs))

    def __repr__(self):
        return str((self.family_name, self.eyes, self.hairs))
