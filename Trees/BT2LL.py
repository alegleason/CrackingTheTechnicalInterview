#  Python program to convert a binary
#  tree to a doubly linked list

class Node:
    def __init__(self, val):
        self.right = None
        self.left = None
        self.val = val


class BT2LL:
    def __init__(self):
        self.head = None
        self.tail = None

    def convert(self, root):
        # base case
        if root is None:
            return

        # convert recursively left tree
        self.convert(root.left)

        node = root
        # left most element
        if self.head is None:
            self.head = node
        else:
            self.tail.right = node
            node.left = self.tail
        self.tail = node

        self.convert(root.right)
        return self.head

def printDLL(head):
    # Function to print nodes in given doubly linked list
    while head is not None:
        print(head.val, end=" ")
        head = head.right


if __name__ == '__main__':
    root = Node(15)
    root.left = Node(10)
    root.right = Node(20)
    root.left.left = Node(5)

    converter = BT2LL()

    # convert to DLL
    head = converter.convert(root)

    # Print the converted list
    printDLL(head)
