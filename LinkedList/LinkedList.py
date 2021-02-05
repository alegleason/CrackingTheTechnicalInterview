from collections import deque


class PartialSum:
    def __init__(self):
        self.sum = None
        self.carry = 0


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Appends at the end of a Linked List
    def append(self, val):
        if not isinstance(val, Node):
            temp = Node(val)
        else:
            temp = val
        if self.head is None:
            self.head = temp
            return temp

        n = self.head
        while n:
            if n.next is None:
                n.next = temp
                return temp
            n = n.next
        return temp

    # Print the current list contents
    def print(self):
        n = self.head
        while n:
            print(n.val)
            n = n.next

    # Returns the length (integer) of the linked list.
    def length(self):
        count = 0
        n = self.head
        while n:
            n = n.next
            count += 1
        return count

    # Remove duplicates in a linked list
    def removeDupsBuffer(self):
        # O(n) both space and time
        if not self.head or not self.head.next:
            return self.head
        buffer = set()
        n = self.head
        buffer.add(n.val)
        while n.next:
            if n.next.val in buffer:
                n.next = n.next.next
            else:
                buffer.add(n.next.val)
                n = n.next
        return self.head

    # Remove duplicates in a linked list with no buffer
    def removeDupsNoBuffer(self):
        # O(1) space, O(n2) time
        if not self.head or not self.head.next:
            return self.head

        # First manage head
        while self.isInList(self.head.val, self.head):
            self.head = self.head.next

        prev = self.head
        n = self.head.next

        while n:
            if self.isInList(n.val, n):
                prev.next = n.next
            else:
                prev = n
            n = n.next
        return self.head

    # Returns true if the val is on list, else false. Starts searching on start node
    def isInList(self, val, startNode):
        n = startNode.next
        while n:
            if n.val == val:
                return True
            n = n.next
        return False

    # Returns the elements that is at len(list) - k position
    def kthToLast(self, k):
        # O(n) time and O(1) space complexity
        # Move fast pointer k positions
        k -= 1
        fast = self.head
        while k:
            fast = fast.next
            if fast is None:
                raise IndexError("Error index out of range")
            k -= 1

        slow = self.head
        while fast.next:
            slow = slow.next
            fast = fast.next

        return slow

    # Deletes the node of a list, only being provided with it, no head
    def deleteNode(self, n):
        # We will do this by overwriting until we get to the end
        prev = n
        while n.next:
            n.val = n.next.val
            prev = n
            n = n.next
        prev.next = None

    # Partitions a list taking x as a divisor, with all < elements at the left, and >= at the right
    def partition(self, x):
        # O(n) time and O(1) space complexity
        n = self.head
        leftLast = leftFirst = rightLast = rightFirst = None
        while n:
            if n.val < x:
                # Save first node from the left list
                if not leftFirst:
                    leftFirst = Node(n.val)
                    leftLast = leftFirst
                else:
                    # Continue appending, order does not matters
                    leftLast.next = Node(n.val)
                    leftLast = leftLast.next
            else:
                # Save first node from the last list
                if not rightFirst:
                    rightFirst = Node(n.val)
                    rightLast = rightFirst
                else:
                    rightLast.next = Node(n.val)
                    rightLast = rightLast.next
            n = n.next
        # Point the head of our list to our first node
        if leftLast:
            leftLast.next = rightFirst
            self.head = leftFirst
        else:
            self.head = rightFirst

    # Fx that returns the sum as 7 -> 1 -> 6 + 5 -> 9 -> 2 = 2 -> 1 -> 9
    def sum_lists_backward(self, l1, l2, carry=0):
        # O(n) time and space complexity
        if not l1 and not l2:
            return None

        value = carry

        if l1:
            value += l1.val

        if l2:
            value += l2.val

        res = Node(value % 10)

        if l1 or l2:
            res.next = (self.sum_lists_backward(None if not l1 else l1.next, None if not l2 else l2.next,
                                                1 if value >= 10 else 0))
        return res

    # Fx that returns the sum as 6 -> 1 -> 7 + 2- > 9 -> 5 = 9 -> 1 -> 2
    def sum_lists_forward(self, l1, l2):
        # O(n) both time and space complexity
        lenL1 = l1.length()
        lenL2 = l2.length()

        # Fill with zeros so we sum units w units, tens w tens and so on
        if lenL1 < lenL2:
            l1.head = l1.fill_with_zeroes(lenL2 - lenL1)
        elif lenL2 < lenL1:
            l2.head = l2.fill_with_zeroes(lenL1 - lenL2)

        tempSum = self.sum_helper(l1.head, l2.head)

        # Add the final carry
        if tempSum.carry > 0:
            return self.insert_before(tempSum.carry, tempSum.sum)
        else:
            return tempSum.sum

    def sum_helper(self, l1, l2):
        if not l1 and not l2:
            # Empty sum object
            return PartialSum()
        tempSum = self.sum_helper(l1.next, l2.next)
        value = l1.val + l2.val + tempSum.carry
        # Insert the result of the temp sum before our current sum...
        fullResult = self.insert_before(value % 10, tempSum.sum)
        tempSum.sum = fullResult
        # ... and update the carry too with 0 or for the next sum
        tempSum.carry = int(value / 10)
        return tempSum

    def fill_with_zeroes(self, zeros):
        for _ in range(zeros):
            self.head = self.insert_before(0, self.head)
        return self.head

    def insert_before(self, val, l1):
        n = Node(val)
        if l1:
            n.next = l1
        return n

    # Return True if a linked list is palindrome otherwise, false
    def isPalindrome(self):
        # O(n) time and O(n/2) space complexity
        stack = deque()
        slow = fast = self.head
        while fast.next and fast.next.next:
            stack.appendleft(slow.val)
            slow = slow.next
            fast = fast.next.next
        stack.appendleft(slow.val)
        # If we have odd elements, forward one position
        if fast.next:
            slow = slow.next

        # Compare both halves
        while slow:
            if stack.popleft() != slow.val:
                return False
            slow = slow.next

        return True

    def areEqual(self, l1):
        n = l1.head
        m = self.head
        while n and m:
            if n.val != m.val:
                return False
            n = n.next
            m = m.next
        return True

    def reverse(self):
        prev = None
        curr = self.head
        nxt = curr.next
        while curr:
            curr.next = prev
            if not nxt:
                break
            prev = curr
            curr = nxt
            nxt = nxt.next
        self.head = curr

    # Return True if two linked lists intersect, otherwise false
    def intersect(self, l2):
        # O(A+B) time and O(1) space complexity
        # Get both tail and size from each list
        sz1, t1 = self.getTailAndSize()
        sz2, t2 = l2.getTailAndSize()

        # If they have different tails, return immediately
        if t1 != t2:
            return False

        # Move pointers to equal starts
        if sz1 > sz2:
            # Move first list pointer n positions
            self.head = self.returnKthNode(sz1 - sz2)
        elif sz2 > sz1:
            l2.head = l2.returnKthNode(sz2 - sz1)

        # Now just iterate to find the common node and return it
        n = self.head
        m = l2.head
        # They have the same size already
        while n:
            if n == m:
                return n
            n = n.next
            m = m.next

        return False

    def returnKthNode(self, k):
        n = self.head
        while k:
            n = n.next
            k -= 1
        return n

    def getTailAndSize(self):
        n = self.head
        count = 1
        while n.next:
            count += 1
            n = n.next
        return count, n


"""
    # Returns the value of the node at 'index' 0 based
    def get(self, index):
        if index >= self.length():
            print("Error: 'Get' Index out of range!")
            return None
        count = -1
        curr = self.head
        while count != index:
            curr = curr.next
            count += 1
        return curr

    # Deletes the node at index 'index'.
    def erase(self, index):
        if index >= self.length():
            print("Error: 'Erase' Index out of range!")
            return
        count = -1
        curr = self.head
        while count != (index - 1):
            curr = curr.next
            count += 1
        curr.next = curr.next.next

    # Allows for bracket operator syntax (i.e. a[0] to return first item).
    def __getitem__(self, index):
        return self.get(index)

    # Inserts a new node at index 'index' containing data 'data'.
    # Indices begin at 0. If the provided index is greater than or
    # equal to the length of the linked list the 'data' will be appended
    def insert(self, index, data):
        if index >= self.length():
            return self.append(data)
        if index < 0:
            print("ERROR: 'Insert' Index cannot be negative!")
            return
        cur_node = self.head
        prior_node = self.head
        cur_idx = 0
        while True:
            cur_node = cur_node.next
            if cur_idx == index:
                new_node = Node(data)
                prior_node.next = new_node
                new_node.next = cur_node
                return
            prior_node = cur_node
            cur_idx += 1

    # Inserts the node 'node' at index 'index'. Indices begin at 0.
    # If the 'index' is greater than or equal to the length of the linked
    # list the 'node' will be appended.
    def insert_node(self, index, node):
        if index >= self.length():
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = node
            return
        if index < 0:
            print("ERROR: 'Insert' Index cannot be negative!")
            return
        curr = self.head
        prev = self.head
        count = -1
        while True:
            curr = curr.next
            count += 1
            if index == count:
                prev.next = node
                node.next = curr
                return
            prev = curr

    # Sets the data at index 'index' equal to 'data'.
    # Indices begin at 0. If the 'index' is greater than or equal
    # to the length of the linked list a warning will be printed
    # to the user.
    def set(self, index, data):
        if self.length ) <= index or index < 0:
            print("ERROR: 'Set' Index out of range!")
            return
        count = -1
        curr = self.head
        while index != count:
            curr = curr.next
            count += 1
        curr.data = data
        return
"""
