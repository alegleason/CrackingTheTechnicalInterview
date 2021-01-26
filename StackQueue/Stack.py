import sys
from collections import deque


class Stack:
    # Private structure
    __stack = deque()
    # Stack that saves min values
    __min_stack = deque()

    # Remove the top item from a stack
    def pop(self):
        if self.__stack[len(self.__stack) - 1] == self.min():
            self.__min_stack.pop()
        self.__stack.pop()

    # Add an item to the top of the stack
    def push(self, item):
        if item < self.min():
            self.__min_stack.append(item)
        self.__stack.append(item)

    # Return the top of the stack
    def peek(self):
        return self.__stack[len(self.__stack) - 1]

    # Return true if and only if the stack is empty.
    def isEmpty(self):
        return True if len(self.__stack) == 0 else False

    # Returns the minimum element
    def min(self):
        return self.__min_stack[len(self.__min_stack) - 1] if len(self.__min_stack) > 0 else sys.maxsize


st = Stack()
st.push(-1)
print(st.peek())
print(st.min())

# Calculates Fibonacci using a stack, O(n) time complexity
def fibonacci(n):
    stack = Stack()
    if n == 1 or n == 2:
        return 1
    stack.push(1)
    stack.push(1)
    i = 0
    while i < n - 2:
        num1 = stack.peek()
        stack.pop()
        num2 = stack.peek()
        stack.pop()
        stack.push(num1)
        stack.push(num1 + num2)
        i += 1
    return stack.peek()


def sort_stack(s):
    r = deque()
    while len(s) > 0:
        # Insert each element in s in sorted order into r
        temp = s[len(s) - 1]
        s.pop()
        while len(r) > 0 and r[len(r) - 1] > temp:
            s.append(r[len(r) - 1])
            r.pop()
        r.append(temp)

    # Copy the elements form r back into s
    while len(r) > 0:
        s.append(r[len(r) - 1])
        r.pop()

    return s

class SetOfStacks:
    # Private structure
    __set_of_stacks = deque()
    __set_of_stacks.append(deque())
    __current_capacity = 0
    max_capacity_of_stack = 5

    # Remove the top item from a stack
    def pop(self):
        current_stack = self.__set_of_stacks[len(self.__set_of_stacks) - 1]
        current_stack.pop()
        if len(current_stack) == 0:
            self.__set_of_stacks.pop()

    # Add an item to the top of the stack
    def push(self, item):
        if self.max_capacity_of_stack == self.__current_capacity:
            # Push a new stack
            self.__set_of_stacks.append(deque())
            self.__current_capacity = 0
        current_stack = self.__set_of_stacks[len(self.__set_of_stacks) - 1]
        current_stack.append(item)
        self.__current_capacity += 1

    def print(self):
        for stack in self.__set_of_stacks:
            print(stack)

    # Performs a pop operation on a specific sub-stack.
    def pop_at(self, index):
        if index > len(self.__set_of_stacks) or index < 1:
            return
        desired_stack = self.__set_of_stacks[len(self.__set_of_stacks) - index]
        desired_stack.pop()
        if len(desired_stack) == 0:
            del self.__set_of_stacks[len(self.__set_of_stacks) - index]
