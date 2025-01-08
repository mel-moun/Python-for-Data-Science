from S1E9 import Character


class Baratheon(Character):
    def __init__(self, first_name):
        super().__init__(first_name)
        self.family_name = 'Baratheon'
        self.eyes = 'brown'
        self.hairs = 'dark'

    def die():
        super().die()
