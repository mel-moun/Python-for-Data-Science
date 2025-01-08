class calculator:
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        product = [(a * b) for a, b in zip(V1, V2)]
        print(sum(product))

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        sums = [(a + b) for a, b in zip(V1, V2)]
        print(sums)

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        subs = [(a - b) for a, b in zip(V1, V2)]
        print(subs)
