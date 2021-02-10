import sys
from collections import deque


class NodeStack:
    def __init__(self, data=None):
        self.data = data
        self.next = None


# Implement a Stack structure from scratch
class Stack:
    top_node = None

    # Remove the top item from the stack
    def pop(self):
        if self.top_node is None:
            raise ValueError('Stack is empty')
        n = self.top_node
        self.top_node = n.next
        return n.data

    # Add an item to the top of the stack
    def push(self, data):
        n = NodeStack(data)
        n.next = self.top_node
        self.top_node = n
        return self.top_node

    # Return the top of the stack
    def peek(self):
        if self.top_node.data is None:
            raise ValueError('Stack is empty')
        return self.top_node.data

    # Return true if the stack is empty
    def isEmpty(self):
        return self.top_node is None

    # Print the content of the stack
    def print(self):
        n = self.top_node
        while n.next:
            print(n.data)
            n = n.next

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.print()
print("Peek ", stack.peek())
print("Popping ", stack.pop())
print("Peek ", stack.peek())
print("Popping ", stack.pop())
stack.push(50)
stack.print()
print(stack.isEmpty())
print("Peek ", stack.peek())
print("Popping ", stack.pop())
print("Peek ", stack.peek())
print("Popping ", stack.pop())

print(stack.isEmpty())