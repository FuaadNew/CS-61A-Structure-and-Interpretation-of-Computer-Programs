def swipe(n):
    """Print the digits of n, one per line, first backward then forward.

    >>> swipe(2837)
    7
    3
    8
    2
    8
    3
    7
    """
    if n < 10:
        print(n)
    else:
       
       print(n%10)
       swipe(n//10)
       print(n%10)

def skip_factorial(n):
    """Return the product of positive integers n * (n - 2) * (n - 4) * ...

    >>> skip_factorial(5) # 5 * 3 * 1
    15
    >>> skip_factorial(8) # 8 * 6 * 4 * 2
    384
    """
    if n <= 0:
        return 1
    else:
        return n * skip_factorial(n - 2)



def is_prime(n):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"

    def f(i):   
        ''' return Fakse if a number between 2 and n - 1 divides n evenly,
             else return True '''
        if i == n:
            return True
        if n % i == 0:
            return False
        return f(i + 1)
    
    return f(2)
        




    #while num > 1:
     #   if n % num == 0:
      #      return False
       # num-=1
    #return True
    

if __name__ == '__main__':
   print(is_prime(2))
   print(is_prime(16))
   print(is_prime(521))

