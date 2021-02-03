class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Appends at the end of a Linked List
    def append(self, val):
        temp = Node(val)
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


linkedList = LinkedList()
linkedList.append(6)
linkedList.append(3)
linkedList.append(4)
linkedList.append(3)
linkedList.append(6)
linkedList.append(8)
# print(linkedList.kthToLast(6).val)
# linkedList.deleteNode(node)
linkedList.partition(5)
linkedList.print()

"""
import math

    # Adds new node containing 'data' to the end of the linked list.
    def append_node(self, node):
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = node

    # Returns the length (integer) of the linked list.
    def length(self):
        count = 0
        curr = self.head
        while curr.next is not None:
            count += 1
            curr = curr.next
        return count

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
        if self.length() <= index or index < 0:
            print("ERROR: 'Set' Index out of range!")
            return
        count = -1
        curr = self.head
        while index != count:
            curr = curr.next
            count += 1
        curr.data = data
        return

    def sum_list_not_forward(self, list1, list2):
        res_inv = LinkedList()
        n1 = list1.length()
        n2 = list2.length()
        if n1 == 0 or n2 == 0:
            return
        count = 0
        carry = 0
        while count < max(n1, n2):
            num1 = list1.get(count)
            num2 = list2.get(count)
            if num1 is not None and num2 is not None:
                new_carry = 1 if num1.data + num2.data + carry >= 10 else 0
                res_inv.append(num1.data + num2.data + carry) if num1.data + num2.data + carry < 10 else res_inv.append(
                    num1.data + num2.data + carry - 10)
                carry = new_carry
            elif num1 is not None:
                res_inv.append(num1.data)
            elif num2 is not None:
                res_inv.append(num2.data)
            count += 1
        i = 0
        res = LinkedList()
        return res_inv

    #O(n2) time, O(n) space
    def sum_list_forward(self, list1, list2):
        res_inv = LinkedList()
        n1 = list1.length()
        n2 = list2.length()
        if n1 == 0 or n2 == 0:
            return
        count = 0
        carry = 0
        while count < max(n1, n2):
            num1 = list1.get(max(n1, n2) - count - 1)
            num2 = list2.get(max(n1, n2) - count - 1)
            if num1 is not None and num2 is not None:
                new_carry = 1 if num1.data + num2.data + carry >= 10 else 0
                res_inv.append(num1.data + num2.data + carry) if num1.data + num2.data + carry < 10 else res_inv.append(num1.data + num2.data + carry - 10)
                carry = new_carry
            elif num1 is not None:
                res_inv.append(num1.data)
            elif num2 is not None:
                res_inv.append(num2.data)
            count += 1
        i = 0
        res = LinkedList()
        while i < count:
            res.append(res_inv.get(count - i - 1).data)
            i += 1
        return res

    #O(kn) time, where k is n/2 and n is list.length, O(1) space
    def palindrome(self):
        i = 0
        n = math.floor(self.length()/2)
        le = self.length() - 1
        while i < n:
            if self.get(i).data != self.get(le - i).data:
                return False
            i += 1
        return True

    # O(n) time, O(n) space
    def reverse(self):
        # Initializing values
        prev = None
        curr = self.head.next
        nex = curr.next
        while curr is not None:
            print(curr.data)
            # reversing the link
            curr.next = prev
            # moving to next node
            prev = curr
            curr = nex
            if nex is not None:
                nex = nex.next
        # initializing head
        self.head.next = prev
        return self

    # O(nXm) time, O(1) space
    def intersect(self, list1, list2):
        len1 = list1.length()
        len2 = list2.length()
        # Chop until they are same length
        if len1 > len2:
            dif = len1 - len2
            while dif > 0:
                list1.erase(0)
                dif -= 1
        elif len2 > len1:
            dif = len2 - len1
            while dif > 0:
                list2.erase(0)
                dif -= 1
        head1 = list1.head.next
        head2 = list2.head.next
        while head1 is not None:
            if head1 == head2:
                return True
            head1 = head1.next
            head2 = head2.next
        return False

    def loop_detection(self):
        dic = dict()
        head = self.head.next
        while head is not None:
            if dic.get(head) is None:
                dic[head] = True
            else:
                return head.data
            head = head.next
"""
