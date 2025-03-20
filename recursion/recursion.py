class recursion_basics:
    def __init__(self, number):
        self.number = number
    
    # very important to have a base case in all recursive functions to avoid infinite recursion
    # in the case of factorial, the base case is when n = 0, after it reaches 0, the recursion stops and it will return the value
    def factorial(self, n):
        if n == 0:
            return 1
        else:
            return n * self.factorial(n-1)
        
    def sum_of_natural_numbers(self,n):
        """
        Function to calculate the sum of the first n natural numbers using recursion.
        
        Parameters:
        n (int): The non-negative integer for which the sum is to be calculated.
        
        Returns:
        int: The sum of the first n natural numbers.
        """
        # Your code here
        if n == 0:
            return 0
        smallAns = n + self.sum_of_natural_numbers(n-1)
        return smallAns
    
    def powerof2(self, n):
        """
        Function to calculate the power of 2 using recursion.
        
        Parameters:
        n (int): The non-negative integer for which the power of 2 is to be calculated.
        
        Returns:
        int: The power of 2 for the given integer.
        """
        # Your code here
        if n == 0:
            return 1
        smallAns = self.powerof2(n-1)
        return smallAns * 2
    

    def fibonacci(self, n):
        """
        Function to calculate the nth Fibonacci number using recursion.
        
        Parameters:
        n (int): The non-negative integer for which the Fibonacci number is to be calculated.
        
        Returns:
        int: The nth Fibonacci number.
        """
        # Your code here
        if n == 0:
            return 0
        if n == 1:
            return 1
        last = self.fibonacci(n-1)
        secondLast = self.fibonacci(n-2)
        return last + secondLast
    
    # tail recursion of fibonacci

    def fibonacci_tail(self, n, a = 0, b = 1):
        """
        Function to calculate the nth Fibonacci number using tail recursion.
        
        Parameters:
        n (int): The non-negative integer for which the Fibonacci number is to be calculated.
        
        Returns:
        int: The nth Fibonacci number.
        """
        # Your code here
        if n == 0:
            return a
        if n == 1:
            return b
        return self.fibonacci_tail(n-1, b, a+b)
    
    # head recursion of count to n
    # this will print 1, 2, 3, 4, 5

    def count_to_n(self, n):
        """
        Function to return a list of integers from 1 to n using recursion.
        
        Parameters:
        n (int): The positive integer representing the upper limit of the range.
        
        Returns:
        list: A list of integers from 1 to n.
        """
        # Your code here
    
        if n ==1:
            return [1]
        
        return self.count_to_n(n-1) + [n]
    

    # tail recursion of count to n
    # this will print 5, 4, 3, 2, 1

    def count_to_n_tail(self, n):
        """
        Function to return a list of integers from 1 to n using tail recursion.
        
        """
        if n ==1:
            return [1]
        
        return [n] +self.count_to_n(n-1)
    """
    # head or tail depends on when the recursive call is made and in which order see below 

    # head recursion
    base case
    recursive call
    calculation - actual work

    tail recursion
    base case
    calculation - actual work
    recursive call

    """
    