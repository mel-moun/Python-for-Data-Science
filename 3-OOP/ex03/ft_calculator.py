class calculator:
    def __init__(self, vector):
        try:
            for x in vector:
                if type(x) is not int and type(x) is not float:
                    raise AssertionError("bad arguments.")
            self.vector = vector

        except BaseException as e:
            print(type(e).__name__, ":", e)

    def __add__(self, object) -> None:
        self.vector = [x + object for x in self.vector]
        print(self.vector)

    def __mul__(self, object) -> None:
        self.vector = [x * object for x in self.vector]
        print(self.vector)

    def __sub__(self, object) -> None:
        self.vector = [x - object for x in self.vector]
        print(self.vector)

    def __truediv__(self, object) -> None:
        try:
            if object == 0:
                raise AssertionError("Division by zero is not allowed.")
            self.vector = [x / object for x in self.vector]
            print(self.vector)
        except BaseException as e:
            print(type(e).__name__, ":", e)
