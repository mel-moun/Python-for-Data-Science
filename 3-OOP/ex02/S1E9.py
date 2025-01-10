from abc import ABC, abstractmethod


class Character(ABC):
    """
    Abstract base class representing a character
    with a name and life status.
    """

    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """
        Initializes a character with a first name
        and a default status of being alive.
        """
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """
        Marks the character as no longer alive.
        """
        pass


class Stark(Character):
    """
    Represents a member of the Stark family,
    inheriting from the Character class.
    """

    def __init__(self, first_name, is_alive=True):
        """
        Initializes a Stark family member with a first name
        and a default status of being alive.
        """
        super().__init__(first_name, is_alive)

    def die(self):
        """
        Marks the Stark family member as no longer alive.
        """
        self.is_alive = False
