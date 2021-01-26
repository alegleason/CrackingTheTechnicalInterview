from collections import deque

# Helper classes
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Binary Tree Zigzag Level Order Traversal - Top Interview Questions Medium
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


# tn = TreeNode(3)
# tn.left = TreeNode(9)
# tn.right = TreeNode(20)
# tn.right.left = TreeNode(15)
# tn.right.right = TreeNode(7)

sol = Solution()
# print(sol.zigzagLevelOrder(tn))