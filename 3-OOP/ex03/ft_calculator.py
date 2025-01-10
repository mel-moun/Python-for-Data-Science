class calculator:
    """
    A class to perform basic mathematical 
    operations (addition, subtraction, 
    multiplication, division) on a vector of numbers.
    """

    def __init__(self, vector):
        """
        Initializes the calculator with a vector.
        Ensures all elements are numeric (int or float).
        """
        try:
            for x in vector:
                if type(x) is not int and type(x) is not float:
                    raise AssertionError("bad arguments.")
            self.vector = vector

        except BaseException as e:
            print(type(e).__name__, ":", e)


    def __add__(self, object) -> None:
        """
        Adds a scalar value to each element of the vector.
        """
        self.vector = [x + object for x in self.vector]
        print(self.vector)


    def __mul__(self, object) -> None:
        """
        Multiplies each element of the vector by a scalar value.
        """
        self.vector = [x * object for x in self.vector]
        print(self.vector)


    def __sub__(self, object) -> None:
        """
        Subtracts a scalar value from each element of the vector.
        """
        self.vector = [x - object for x in self.vector]
        print(self.vector)


    def __truediv__(self, object) -> None:
        """
        Divides each element of the vector by a scalar value.
        Raises an error if division by zero is attempted.
        """
        try:
            if object == 0:
                raise AssertionError("Division by zero is not allowed.")
            self.vector = [x / object for x in self.vector]
            print(self.vector)
        except BaseException as e:
            print(type(e).__name__, ":", e)
