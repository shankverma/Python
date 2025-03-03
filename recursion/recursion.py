class recursion_algorithms:
    def __init__(self, key):
        self.key = key
    
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