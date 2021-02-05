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

    # Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.
    def numIslands(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        # Shared matrix for visited cells
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        count = 0
        # O(NxM) time and space complexity
        for row in range(rows):
            for col in range(cols):
                if not visited[row][col] and grid[row][col] == "1":
                    self.DFS(grid, visited, row, col)
                    count += 1
        return count

    def DFS(self, grid, visited, row, col):
        # Generate movements (up, down, left, right)
        rowsComb = [-1, 0, 1, 0]
        colsComb = [0, 1, 0, -1]

        # Mark current as visited
        visited[row][col] = True

        for k in range(4):
            if self.isSafe(row + rowsComb[k], col + colsComb[k], visited, grid):
                self.DFS(grid, visited, row + rowsComb[k], col + colsComb[k])

    def isSafe(self, row, col, visited, grid):
        if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and not visited[row][col] and grid[row][col] == "1":
            return True
        return False

    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        print(root.val)
        self.inorder(root.right)


tn = TreeNode(10)
tn.left = TreeNode(12)
tn.left.left = TreeNode(25)
tn.left.right = TreeNode(30)
tn.right = TreeNode(15)
tn.right.left = TreeNode(36)

sol = Solution()
sol.inorder(tn)

