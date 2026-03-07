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



def divisible_by_k(n, k):
    """
    >>> a = divisible_by_k(10, 2)  # 2, 4, 6, 8, and 10 are divisible by 2
    2
    4
    6
    8
    10
    >>> a
    5
    >>> b = divisible_by_k(3, 1)  # 1, 2, and 3 are divisible by 1
    1
    2
    3
    >>> b
    3
    >>> c = divisible_by_k(6, 7)  # There are no integers up to 6 divisible by 7
    >>> c
    0
    """
    "*** YOUR CODE HERE ***"

    i = 1
    res = 0
    while i <=n:
        if i % k == 0:
            print(i)
            res+=1
        i+=1
    return res
    

def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    res = 0
    while y > 0:
        res+= y % 10
        y = y //10
    return res



if __name__ == "__main__":
    print(sum_digits(10))
    print(sum_digits(4224))
    print(sum_digits(1234567890))