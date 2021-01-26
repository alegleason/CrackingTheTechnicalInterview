import math


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        # Head is only an empty node pointing to the first value
        self.head = Node()

    # Adds new node containing 'data' to the end of the linked list.
    def append(self, data):
        new_node = Node(data)
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = new_node

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

    # Prints out the linked list in traditional Python list format.
    def display(self):
        elements = []
        curr = self.head
        while curr.next is not None:
            curr = curr.next
            elements.append(curr.data)
        return elements

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
    # equal to the length of the linked list the 'data' will be appended.
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

    # O(n) time, buffer allowed
    def remove_dups(self):
        curr = self.head
        index = 0
        occurrences = dict()
        deleted = 0
        length = self.length()
        while index < length:
            curr = curr.next
            if occurrences.get(curr.data) is None:
                occurrences[curr.data] = True
            else:
                # If we did not have erase, just create a new list, push it and return it
                self.erase(index - deleted)
                deleted += 1
            index += 1

    # O(n2) time, no buffer allowed
    def remove_dups_no_buffer(self):
        curr = self.head
        while curr is not None:
            runner = curr
            while runner.next is not None:
                if runner.next.data == curr.data:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            curr = curr.next

    # O(n) time, we have to return the element that is kth positions from the end.
    # If we actually want the element, an alternative would be to wrap the index
    # in a class and return in that way the node, zero based index.
    def return_kth_to_last(self, head, kth):
        if kth > self.length() - 1 or kth < 0:
            print("ERROR: 'Get' Index out of range!")
            return
        if head is None:
            return 0
        index = self.return_kth_to_last(head.next, kth) + 1
        if index - 1 == kth:
            print("Kth element is: " + str(head.data))
        return index

    # O(n) time, iterative way, zero based index
    def return_kth_to_last_iterative(self, kth):
        if kth > self.length() - 1 or kth < 0:
            print("ERROR: 'Get' Index out of range!")
            return
        p1 = self.head.next
        p2 = p1
        index = 1
        while index <= kth:
            p2 = p2.next
            index += 1
        while p2.next is not None:
            p1 = p1.next
            p2 = p2.next
        print(p1.data)

    # Delete the node passed by reference, we can only access it, not head
    @staticmethod
    def delete_middle_node(node):
        curr = node
        while curr.next is not None:
            curr.data = curr.next.data
            past = curr
            curr = curr.next
        past.next = None

    # Partition the list given a value so that elements at left are smaller
    # and at right are bigger than it.
    def partition(self, value):
        smaller = LinkedList()
        bigger = LinkedList()
        head = self.head.next
        present_flag = 0
        while head is not None:
            if head.data < value:
                smaller.append(head.data)
            elif head.data > value:
                bigger.append(head.data)
            else:
                present_flag = 1
            head = head.next
        if present_flag == 1:
            smaller.append(value)
        head = bigger.head.next
        while head is not None:
            smaller.append(head.data)
            head = head.next
        return smaller

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