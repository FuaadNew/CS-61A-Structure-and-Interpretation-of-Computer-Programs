

def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    "*** YOUR CODE HERE ***"

    if n == 1 or m == 1:
        return 1
    return paths(m - 1, n) + paths(m, n - 1)


def max_product(s):
    """Return the maximum product of non-consecutive elements of s.

    >>> max_product([10, 3, 1, 9, 2])   # 10 * 9
    90
    >>> max_product([5, 10, 5, 10, 5])  # 5 * 5 * 5
    125
    >>> max_product([])                 # The product of no numbers is 1
    1
    """
   


    def dfs(s):
        if len(s) == 1:
            return s[0]

        if len(s) == 0:
            return 1

        #include 
        include = s[0] * dfs(s[2:])

        #exclude
        exclude = dfs(s[1:])

        return max(include,exclude)

    return dfs(s)







if __name__ == "__main__":
    50 
    print(max_product([5, 10, 5, 10, 5]))

   

   

