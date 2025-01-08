from S1E7 import Baratheon, Lannister

class King(Baratheon, Lannister):
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = 'Baratheon'
        self.eyes = 'brown'
        self.hairs = 'dark'

    def set_eyes(self, eyes_color):
        self.eyes = eyes_color

    def set_hairs(self, hair_color):
        self.hairs = hair_color

    def get_eyes(self):
        return self.eyes

    def get_hairs(self):
        return self.hairs

    def __str__(self):
        return str((self.family_name, self.eyes, self.hairs))

    def __repr__(self):
        return str((self.family_name, self.eyes, self.hairs))
