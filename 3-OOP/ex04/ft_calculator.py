class calculator:
    """
    A class providing static methods
    to perform operations on vectors such as
    dot product, vector addition, and vector subtraction.
    """

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """
        Computes and prints the dot product of two vectors.
        """
        product = [(a * b) for a, b in zip(V1, V2)]
        print(sum(product))

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """
        Adds two vectors element-wise
        and prints the resulting vector.
        """
        sums = [(a + b) for a, b in zip(V1, V2)]
        print(sums)

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """
        Subtracts two vectors element-wise
        and prints the resulting vector.
        """
        subs = [(a - b) for a, b in zip(V1, V2)]
        print(subs)
