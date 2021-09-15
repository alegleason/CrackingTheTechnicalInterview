# Helper classes

import sys
from collections import Counter


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# class Node:
#     def __init__(self, x: int, next=None, random=None):
#         self.val = int(x)
#         self.next = next
#         self.random = random

class Node:
    def __init__(self, val: int = 0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


tn = TreeNode(7)
tn.right = TreeNode(2)
tn.right.right = TreeNode(1)

ll = ListNode(3)
ll2 = ListNode(2)
ll.next = ll2
ll.next.next = ListNode(0)
ll.next.next.next = ListNode(-4)
ll.next.next.next.next = ll2

rl = Node(7)
rl.next = Node(13)
rl.next.next = Node(11)
rl.next.next.next = Node(10)

rl.next.random = rl
rl.next.next.random = rl.next
rl.next.next.next.random = rl

nn = Node(1)
nn.left = Node(2)
nn.right = Node(3)
nn.left.left = Node(4)
nn.left.right = Node(5)
nn.right.left = Node(6)
nn.right.right = Node(7)


# Solution class

class Solution:
    # 200 - Number of Islands
    def bfs(self, grid, row, col, num_rows, num_cols):
        # Perform actual BFS
        i_s = [0, -1, 0, 1]
        j_s = [-1, 0, 1, 0]

        # Push current node
        queue = [[row, col]]
        # Mark node as visited
        grid[row][col] = '2'

        while queue:
            row, col = queue.pop(0)
            # Mark all adjacent nodes that are islands as visited
            for k in range(len(i_s)):
                curr_row = row + i_s[k]
                curr_col = col + j_s[k]
                if self.isValid(curr_row, curr_col, num_rows, num_cols) and grid[curr_row][curr_col] == '1':
                    grid[curr_row][curr_col] = '2'
                    queue.append([curr_row, curr_col])

    def isValid(row, col, num_rows, num_cols):
        return not (row >= num_rows or row < 0 or col >= num_cols or col < 0)

    def numIslands(self, grid):
        totalIslands = 0
        num_rows = len(grid)
        num_cols = len(grid[0])

        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] == '1':
                    totalIslands += 1
                    self.bfs(grid, i, j, len(grid), len(grid[0]))
        return totalIslands

    # 662. Maximum Width of Binary Tree
    def widthOfBinaryTree(self, root):
        # BFS position calc approach
        queue = [(root, 1, 0)]
        curr_depth = left = ans = 0
        while queue:
            node, depth, pos = queue.pop(0)
            if node:
                # this is equivalent to doing a for child in children
                queue.append((node.left, depth + 1, pos * 2))  # good technique to use depth to track the current level
                queue.append((node.right, depth + 1, pos * 2 + 1))
                if depth != curr_depth:
                    curr_depth = depth
                    left = pos
                ans = max(pos - left + 1, ans)
        return ans

    # 98. Validate BST
    def isValidBST(self, root) -> bool:
        return self.isValidBSTHelper(root, sys.maxsize * -1, sys.maxsize) if root else []

    def isValidBSTHelper(self, root, min, max):
        # Base case, no children
        if not root:
            return True
        elif root.val <= min or root.val >= max:
            print(root.val, min, max)
            return False

        # Recursion based on keeping and updating a local min and max
        return self.isValidBSTHelper(root.left, min, root.val) and self.isValidBSTHelper(root.right, root.val, max)

    # 109. Convert Sorted List to Binary Search Tree
    def sortedListToBST(self, head):
        if not head:
            return

        if not head.next:
            return TreeNode(head.val)

        # Find mid of linked list using slow and fast technique
        mid = self.mid(head)
        root = TreeNode(mid.val)

        # Determine children
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)
        return root

    def mid(head):
        slow, fast = head, head.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        tmp = slow.next
        slow.next = None
        return tmp

    # 138. Copy List with Random Pointer
    def copyRandomList(self, head):
        copyMap = {}
        # First iteration we map each original node to the cloned node
        temp = head
        copyHead = None
        while temp:
            copyMap[temp] = Node(temp.val)
            if copyHead is None: copyHead = copyMap[temp]
            temp = temp.next

        # Now, we arrange both next and random nodes for copied nodes
        temp = head
        while temp:
            if temp.next is not None:
                copyMap[temp].next = copyMap[temp.next]
            if temp.random is not None:
                copyMap[temp].random = copyMap[temp.random]
            temp = temp.next

        return copyHead

    # 116. Populating Next Right Pointers in Each Node
    def connect(self, root):
        if not root:
            return root

        # BFS - level approach
        queue = [root]
        while queue:
            lvlLn = len(queue)
            prevNode = None
            for i in range(lvlLn):
                node = queue.pop(0)
                if prevNode is None:
                    prevNode = node
                else:
                    prevNode.next = node
                    prevNode = prevNode.next

                # We can assume both will be present since it is a perfect binary tree
                if node.left and node.right:
                    queue.append(node.left)
                    queue.append(node.right)
        return root

    # 316. Remove Duplicate Letters
    def removeDuplicateLetters(self, s):
        counter = Counter(s)
        stack = []  # use append() to push and pop() to remove
        visited = set()
        for char in s:
            counter[char] -= 1
            # If we have seen the letter, skip, since it's considered
            if char in visited:
                continue
            # If we have characters with greater values, remove if we will see them later on
            while stack and stack[-1] > char and counter[stack[-1]] > 0:
                # Mark the letter as not visited and remove it from the solution stacks
                visited.remove(stack.pop())
            visited.add(char)
            stack.append(char)
        return "".join(stack)

    # 33. Search in Rotated Sorted Array
    def search(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            # check for target value
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            # determine if it is left rotated or right rotated
            if nums[mid] >= nums[left]:  # left rotated
                # in ascending order side
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:  # right rotated
                # in ascending order side
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

    firstElement = None
    secondElement = None
    prevElement = TreeNode(sys.maxsize * -1)

    # 99. Recover Binary Search Tree
    def recoverTree(self, root):
        if not root:
            return root
        # check the inorder traversal
        self.inorder(root)
        # exchange the order

        temp = self.firstElement.val
        self.firstElement.val = self.secondElement.val
        self.secondElement.val = temp
        return root

    def inorder(self, root):
        if root.left:
            self.inorder(root.left)

        if self.firstElement is None and self.prevElement.val >= root.val:
            self.firstElement = self.prevElement

        if self.firstElement is not None and self.prevElement.val >= root.val:
            self.secondElement = root

        self.prevElement = root

        if root.right:
            self.inorder(root.right)

    # 141. Linked List Cycle
    def hasCycle(self, head):
        # If there are no nodes or just one
        if not head.next or not head:
            return False

        # Use slow and fast pointer technique
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False

    # 142. Linked List Cycle II
    def detectCycle(self, head):
        # If there are no nodes or just one
        if not head or not head.next:
            return None
        slow = fast = head
        # Find intersection
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                # Found intersection, both start and intersect nodes will be at the same distance from target node
                start = head
                while start != slow:
                    start = start.next
                    slow = slow.next
                return start

        return None

    ans = None

    def recurse(self, root, p, q):
        # Once reached the end of the branch we return false
        if root is None:
            return False

        # Start traversing recursively
        left = self.recurse(root.left, p, q)

        right = self.recurse(root.right, p, q)

        curr = root.val == p or root.val == q

        # If two values are set, that means the current node is the answer
        if left + right + curr >= 2:
            self.ans = root

        # If any value is set, we'll return true since node has been found
        return left or right or curr

    # 236. Lowest Common Ancestor of a Binary Tree
    def lowestCommonAncestor(self, root, p, q):
        self.recurse(root, p, q)
        return self.ans

    def depth(self, root):
        if not root:
            return 0

        return 1 + max(self.depth(root.right), self.depth(root.left))

    # 110. Balanced Binary Tree
    def isBalanced(self, root):
        if not root:
            return True

        leftHeight = self.depth(root.left)

        rightHeight = self.depth(root.right)

        return abs(rightHeight - leftHeight) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

    # 268. Missing Number
    def missingNumber(self, nums):
        # Will use exclusive or (xor) to cancel each number and be left with the answer
        # (the one that could not be canceled), attaching to the property of xor a^b^b = a
        xor = len(nums)
        for i in range(len(nums)):
            xor ^= i
            xor ^= nums[i]
        return xor

    # 287. Find the Duplicate Number
    def findDuplicate(self, nums):
        slow = nums[0]
        fast = nums[slow]
        # Find the intersection
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        fast = 0
        # At this time, the distance from the beginning and slow node will be the same to the goal node
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow




sol = Solution()

# sol.numIslands([
#     ["1", "1", "0", "0", "0"],
#     ["1", "1", "0", "0", "0"],
#     ["0", "0", "1", "0", "0"],
#     ["0", "0", "0", "1", "1"]
# ])
# sol.widthOfBinaryTree(tn)
# sol.sortedListToBST(ll).val
# sol.checkBST(tn)
# sol.copyRandomList(rl)
# sol.connect(nn)
# sol.removeDuplicateLetters('bcabc')
# sol.search([5, 1, 3], 3)
# sol.recoverTree(tn)
# sol.hasCycle(ll)
# sol.detectCycle(ll)
# sol.lowestCommonAncestor(tn, 8, 6)
# sol.isBalanced(tn)
# sol.missingNumber([3, 0, 1])
# sol.findDuplicate([2, 3, 3, 1, 5])
