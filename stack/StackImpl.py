'''
There are only certain operations that can be performed on a stack.
1. Push: Add an element to the top of the stack.
2. Pop: Remove the top element from the stack.
3. Peek: Get the top element of the stack without removing it.
4. isEmpty: Check if the stack is empty.
5. Size: Get the number of elements in the stack.
6. Display: Display the elements of the stack.
7. Clear: Clear the stack.
8. Search: Search for an element in the stack.
9. Reverse: Reverse the stack.
10. Sort: Sort the stack.
11. Copy: Copy the stack.
12. Merge: Merge two stacks
'''

class Stack:
    def __init__(self, max_size=100):
        self.__stack = []
        self.max_size = max_size

    def push(self, item):
        if len(self.__stack) >= self.max_size:
            raise Exception("Stack overflow")
        self.__stack.append(item)

    def pop(self):
        if self.isEmpty():
            raise Exception("Stack underflow")
        return self.__stack.pop()

    def peek(self):
        if self.isEmpty():
            raise Exception("Stack is empty")
        return self.__stack[-1]
    
    def isEmpty(self):
        return len(self.__stack) == 0
    
    def size(self):
        return len(self.__stack)
    

first_stack = Stack()
first_stack.push(1)
first_stack.push(2)
print(first_stack.peek())
first_stack.push(4)
print(first_stack.peek())