class calculator:
    def __init__(self, vector):
        try:
            for x in vector:
                if type(x) != int and type(x) != float:
                    raise AssertionError("All elements in the vector must be of type int or float.")
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
        pass
