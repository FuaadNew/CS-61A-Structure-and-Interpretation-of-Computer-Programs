



def race(x, y):
    """The tortoise always walks x feet per minute, while the hare repeatedly
    runs y feet per minute for 5 minutes, then rests for 5 minutes. Return how
    many minutes pass until the tortoise first catches up to the hare.

    >>> race(5, 7)  # After 7 minutes, both have gone 35 steps
    7
    >>> race(2, 4) # After 10 minutes, both have gone 20 steps
    10
    """
    assert y > x and y <= 2 * x, 'the hare must be fast but not too fast'
    tortoise, hare, minutes = 0, 0, 0
    while minutes == 0 or tortoise - hare:
        print(tortoise, hare)
        print("hello")
        tortoise += x
        if minutes % 10 < 5:
            hare += y
        minutes += 1
    return minutes


def fizzbuzz(n):
    """
    >>> result = fizzbuzz(16)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    >>> print(result)
    None
    """
    "*** YOUR CODE HERE ***"

       
    i = 1
    
    while i <=n:
        
        if i % 15 == 0:
            print("fizzbuzz")
        
        elif i % 3 == 0:
            print("fizz")
        
        elif i % 5 == 0:
            print("buzz")
            
        else:
            print(i)
            
        
        i+=1



def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    >>> is_prime(1) # one is not a prime number!!
    False
    """
    "*** YOUR CODE HERE ***"

    i = 2
    
    if n < 2:
        return False

    if n == 2:
        return True

    while i < n:

        if n % i == 0:
            return False
        i+=1
    
    return True



def unique_digits(n):
    """Return the number of unique digits in positive integer n.

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(101) # 0 and 1
    2
    """
    "*** YOUR CODE HERE ***"

    res = 0

    while n:
        lastDigit = n % 10
        n = n // 10

        if not has_digit(n, lastDigit):
            res+=1
    
    return res



def has_digit(n, k):
    """Returns whether k is a digit in n.

    >>> has_digit(10, 1)
    True
    >>> has_digit(12, 7)
    False
    """
    assert k >= 0 and k < 10
    "*** YOUR CODE HERE ***"

    while n:
        lastDigit = n % 10
        n = n // 10

        if lastDigit == k:
            return True
    return False

if __name__ == "__main__":
    print(unique_digits(8675309))
    print(unique_digits(13173131))
    print(unique_digits(101))
