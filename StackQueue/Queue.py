from collections import deque


class QueueFromStacks:
    # NOTE: This was implemented with stacks using deque() should you
    # want to use Stack class, just replace with the reverse translation,
    # which can be found at Stack.py
    __s1 = deque()
    __s2 = deque()

    # Add an item to the end of the list.
    def add(self, item):
        self.__s1.append(item)

    # Remove the first item in the list.
    def remove(self):
        while len(self.__s1) > 0:
            curr = self.__s1[len(self.__s1) - 1]
            self.__s1.pop()
            self.__s2.append(curr)
        self.__s2.pop()

        # Re assigning the values to s1
        while len(self.__s2) > 0:
            curr = self.__s2[len(self.__s2) - 1]
            self.__s2.pop()
            self.__s1.append(curr)

    # Return the top of the queue.
    def peek(self):
        while len(self.__s1) > 0:
            curr = self.__s1[len(self.__s1) - 1]
            self.__s1.pop()
            self.__s2.append(curr)

        res = self.__s2[len(self.__s2) - 1]

        while len(self.__s2) > 0:
            curr = self.__s2[len(self.__s2) - 1]
            self.__s2.pop()
            self.__s1.append(curr)

        return res

    # Return true if and only if the queue is empty.
    def isEmpty(self):
        return True if len(self.__s1) == 0 else False


class Queue:
    __queue = deque()

    # Add an item to the end of the list.
    def add(self, item):
        self.__queue.append(item)

    # Remove the first item in the list.
    def remove(self):
        self.__queue.popleft()

    # Return the top of the queue.
    def peek(self):
        return self.__queue[0]

    # Return true if and only if the queue is empty.
    def isEmpty(self):
        return True if len(self.__queue) == 0 else False
