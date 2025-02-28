#linear search in lists
# basically traversing the list and checking if the element is present in the list

class sort_search_algorithms:
    def __init__(self, lst, key):
        self.lst = lst
        self.key = key

    def linear_search(self):
        for i in range(len(self.lst)):
            if self.lst[i] == self.key:
                return i
        return -1

    # Binary search in lists
    # this is suited when the list is sorted

    # Bubble sort
    # my solution

    def bubble_sort(self):
        # Your code goes here
        size = len(self.lst)
        for i in range(size):
            for j in range(i+1, size):
                if self.lst[i] > self.lst[j]:
                    # Swap the elements
                    self.lst[i], self.lst[j] = self.lst[j], self.lst[i]
        return self.lst

    def bubble_sort_2(self):
        n = len(self.lst)
        
        # Traverse through all elements in the list
        for i in range(n):
            # Last i elements are already sorted, so we skip them
            print("i counter:", i)
            print("n-i-1", n-i-1)   
            for j in range(0, n - i - 1):
                # Swap if the element found is greater than the next element
                if self.lst[j] > self.lst[j + 1]:
                    self.lst[j], self.lst[j + 1] = self.lst[j + 1], self.lst[j]
        
        return self.lst

# Selection sort

    def selection_sort(self):
        # Traverse through all elements in the list
        #MAJOR ASSUMPTION IN THIS SORT AL GORITHM IS THAT THE FIRST ELEMENT IS THE MINIMUM ELEMENT
        for i in range(len(self.lst)):
            # Find the minimum element in remaining unsorted array
            min_index = i
            for j in range(i + 1, len(self.lst)):
                if self.lst[j] < self.lst[min_index]:
                    min_index = j
            # Swap the found minimum element with the first element
            self.lst[i], self.lst[min_index] = self.lst[min_index], self.lst[i]
        return self.lst


    def insertion_sort(self):
        # Traverse through 1 to len(lst)
        for i in range(1, len(self.lst)):
            key = self.lst[i]
            j = i - 1
            # Move elements of lst[0..i-1], that are greater than key,
            # to one position ahead of their current position
            while j >= 0 and key < self.lst[j]:
                self.lst[j + 1] = self.lst[j]
                j -= 1
            self.lst[j + 1] = key
        return self.lst

    #regular linear search in a rotated array is time consuming and inefficient
    # we can use binary search to find the element in a rotated array
    # explain log(n) time complexity
    # the array is rotated at some pivot point
    # the array is divided into two parts
    # we can use binary search to find the element in the rotated array
    # we can use binary search to find the pivot point
    def search_rotated_array(self):
        # Implement your solution here
        left, right = 0, len(self.lst) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # Check if mid is the target
            if self.lst[mid] == self.key:
                return mid
            
            # Identify the sorted half
            if self.lst[left] <= self.lst[mid]:  # Left half is sorted
                if self.lst[left] <= self.key < self.lst[mid]:  # Target is in the sorted left half
                    right = mid - 1
                else:  # Search in the right half
                    left = mid + 1
            else:  # Right half is sorted
                if self.lst[mid] < self.key <= self.lst[right]:  # Target is in the sorted right half
                    left = mid + 1
                else:  # Search in the left half
                    right = mid - 1
                    
        return -1 

# my leetcode solution
# implement a function that returns the length of the longest substring without repeating characters
# use a sliding window approach (also known as the two-pointer technique).
# use a set to store the unique characters
# use a left pointer to keep track of the leftmost character in the substring
# use a right pointer to keep track of the rightmost character in the substring
# iterate through the string
# if the character is not in the set, add it to the set
# if the character is in the set, remove the character from the set and increment the left pointer
# add the substring to a set
# return the length of the longest substring

    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_substrings = set()
        char_set = set()
        left = 0
        
        # sliding window approach

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            unique_substrings.add(s[left:right + 1])
        
        # find out the longest substring from the set
        longest = ""
        for substring in unique_substrings:
            if len(substring) > len(longest):
                longest = substring
        return len(longest) if unique_substrings else 0


    # longest palindrome - leetcode solution

    def longestPalindrome(self, s: str) -> str:
            palindromes = []
            for i in range(len(s)):
                for j in range(i + 1, len(s) + 1):
                    if s[i:j] == s[i:j][::-1]:
                        palindromes.append(s[i:j])
            longest = ""
            for i in palindromes:
                if len(i) > len(longest):
                    longest = i
            return longest if palindromes else ""
