# Program to parse a binary tree to DLL

class Node:
    def __init__(self, val):
        self.right = None
        self.left = None
        self.val = val

class BSTToDLLParser:
    def __init__(self):
        self.head = None
        self.tail = None

    def parse(self, root):
        # base case, return
        if not root:
            return

        # recursively parse left subtree
        self.parse(root.left)

        node = root
        # set the head of the list as the left most node (smallest one)
        if not self.head:
            self.head = node
        # else if the head is set, configure left node for the current node and
        else:
            self.tail.right = node
            node.left = self.tail
        # update the tail
        self.tail = node

        self.parse(root.right)
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

    parser = BSTToDLLParser()

    # convert to DLL
    head = parser.parse(root)

    # print the parsed list
    printDLL(head)
