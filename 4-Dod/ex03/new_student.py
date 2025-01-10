import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """
    Generates a random 15-character string consisting of lowercase letters.
    """
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass()
class Student:
    """
    A dataclass representing a student with attributes: name, surname,
    active status, login, and a unique ID. The ID is generated automatically.
    """
    name: str
    surname: str
    active: bool = field(init=False, default=True)
    login: str = field(init=False)
    id: str = field(init=False, default=generate_id())

    def __post_init__(self):
        """
        Automatically sets the student's login based on their name and surname.
        The login is the first letter of the name followed by the surname.
        """
        self.login = self.name[0] + self.surname
