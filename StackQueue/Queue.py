import sys
from collections import deque


class NodeQueue:
    def __init__(self, data=None):
        self.data = data
        self.next = None


# Implement a Queue structure from scratch
class Queue:
    first_node = None
    last_node = None

    # Add an item to the end of the queue
    def add(self, data):
        n = NodeQueue(data)
        # End has been assigned
        if self.last_node is not None:
            self.last_node.next = n
        self.last_node = n
        # Start has not been assigned
        if self.first_node is None:
            self.first_node = self.last_node

    # Remove the first added item from the queue
    def remove(self):
        if self.first_node is None:
            raise ValueError('Stack is empty')
        n = self.first_node.data
        self.first_node = self.first_node.next
        # Mark both start and end empty
        if self.first_node is None:
            self.last_node = None
        return n

    # Return the first added item of the queue
    def peek(self):
        return self.first_node.data

    # Return true if the queue is empty
    def isEmpty(self):
        return self.first_node.data is None

    # Print the content of the queue
    def print(self):
        n = self.first_node
        while n:
            print(n.data)
            n = n.next


queue = Queue()
queue.add(10)
queue.add(20)
queue.add(30)
queue.print()
print(queue.peek())
print("removing ", queue.remove())
print("removing ", queue.remove())
print("removing ", queue.remove())
queue.add(40)
queue.print()