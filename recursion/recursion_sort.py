class recursion_sort:
    def __init__(self, lst):
        self.lst = lst

    # def basic_sort(self, lst):

    # head recursion
    def sumOfArrays(self, lst=None):
        if lst is None:
            lst = self.lst
        if len(lst) == 0:
            return 0
        sumOfLeftOverArray = self.sumOfArrays(lst[1:])
        print(sumOfLeftOverArray)
        ans = lst[0]+sumOfLeftOverArray 
        return ans
    
    def sumOfArrays2(self, accumulator=0, lst=None):
        if lst is None:
            lst = self.lst
        if len(lst) == 0:
            return accumulator
        accumulator += lst[0]
        return self.sumOfArrays2(accumulator, lst[1:])
    

    def find_first_index(self, element, arr=None):
        """
        Function to find the first index of a given element in an array using recursion.
        
        Parameters:
        arr (list of int): The array to search through.
        element (int): The element to find.
        
        Returns:
        int: The first index of the element in the array, or -1 if not found.
        """
        # Your code here
        if arr is None:
            arr = self.lst
        if len(arr) ==0:
            return -1
            
        if arr[0] == element:
            return 0
        
        ans = self.find_first_index(element, arr[1:])
        
        if ans == -1:
            return ans
        else:
            return ans+1
    
    

recursion_sort1 = recursion_sort([1, 2])

recursion_sort2 = recursion_sort([1, 2, 3, 4, 5])
#print(recursion_sort1.sumOfArrays())
#print(recursion_sort1.sumOfArrays2())

print(recursion_sort2.find_first_index(3))