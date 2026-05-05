

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

    def dfs(r,c):
        if r > m or c > n:
            return 0
        if r == m and c == n:
            return 1

        return dfs(r+1, c) + dfs(r, c + 1)

    return dfs(1,1)


if __name__ == "__main__":
    pass

   