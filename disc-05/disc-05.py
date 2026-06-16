def has_path(t, p):
    """Return whether tree t has a path from the root with labels p.

    >>> t2 = tree(5, [tree(6), tree(7)])
    >>> t1 = tree(3, [tree(4), t2])
    >>> has_path(t1, [5, 6])        # This path is not from the root of t1
    False
    >>> has_path(t2, [5, 6])        # This path is from the root of t2
    True
    >>> has_path(t1, [3, 5])        # This path does not go to a leaf, but that's ok
    True
    >>> has_path(t1, [3, 5, 6])     # This path goes to a leaf
    True
    >>> has_path(t1, [3, 4, 5, 6])  # There is no path with these labels
    False
    """
    if p == ____:  # when len(p) is 1
        return True
    elif label(t) != ____:
        return False
    else:
        "*** YOUR CODE HERE ***"


if __name__ == "__main__":
    t2 = tree(5, [tree(6), tree(7)])
    t1 = tree(3, [tree(4), t2])

    print(has_path(t1, [5, 6]))        # False
    print(has_path(t2, [5, 6]))        # True
    print(has_path(t1, [3, 5]))        # True
    print(has_path(t1, [3, 5, 6]))     # True
    print(has_path(t1, [3, 4, 5, 6]))  # False
