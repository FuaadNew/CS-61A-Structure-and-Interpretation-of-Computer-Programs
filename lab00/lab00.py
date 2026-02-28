def twenty_twenty_four():
    """Come up with the most creative expression that evaluates to 2024
    using only numbers and the +, *, and - operators.

    >>> twenty_twenty_four()
    2024
    """

    def g(x):
        return x * 2
    
    def f(x):
        return x - 1


    return g(1000) + g(g(f(f(f(f(g(5)))))))


if __name__ == "__main__":
    print( twenty_twenty_four())
    