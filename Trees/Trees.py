from collections import deque


# Helper classes
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Binary Tree Zigzag Level Order Traversal
    def zigzagLevelOrder(self, root):
        if not root:
            return []

        # Perform BFS
        zigZagOrder = []
        auxQueue = deque()
        leftToRight = True

        auxQueue.append(root)
        while auxQueue:
            level = deque()
            currLen = len(auxQueue)
            for i in range(currLen):
                v = auxQueue.popleft()
                if leftToRight:
                    level.append(v.val)
                else:
                    level.appendleft(v.val)
                if v.left:
                    auxQueue.append(v.left)
                if v.right:
                    auxQueue.append(v.right)
            zigZagOrder.append(list(level))
            leftToRight = not leftToRight
        return zigZagOrder

    # Construct Binary Tree from Preorder and Inorder Traversal
    def buildTree(self, preorder, inorder):
        return self.helper(0, 0, len(inorder) - 1, preorder, inorder)

    def helper(self, instart, prestart, inend, preorder, inorder):
        # Base case
        if prestart > len(preorder) - 1 or instart > inend:
            return None

        # Create root and separate the left and right subtree using inorder
        root = TreeNode(preorder[prestart])
        splitIdx = 0
        for i in range(instart, inend):
            if inorder[i] == root.val:
                splitIdx = i
        # Recursion
        root.left = self.helper(instart, prestart + 1, splitIdx - 1, preorder, inorder)
        root.right = self.helper(splitIdx + 1, prestart + splitIdx - instart + 1, inend, preorder, inorder)
        return root

    # Kth Smallest Element in a BST
    def kthSmallest(self, root, k):
        # Time complexity of O(Height + lenStack)
        st = deque()
        while True:
            while root:
                st.appendleft(root)
                root = root.left
            root = st.popleft()
            k -= 1
            if k == 0:
                return root.val
            root = root.right  # Ensure not going back and adding right numbers on the correct position


tn = TreeNode(4)
tn.left = TreeNode(2)
tn.right = TreeNode(5)
tn.left.right = TreeNode(3)

sol = Solution()
print(sol.kthSmallest(tn, 1))
