class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


tn = TreeNode(1)
tn.left = TreeNode(3)
tn.right = TreeNode(2)
tn.left.left = TreeNode(5)
tn.left.right = TreeNode(3)
tn.right.right = TreeNode(9)

ll = ListNode(1)
ll.next = ListNode(2)
ll.next.next = ListNode(3)
ll.next.next.next = ListNode(4)
ll.next.next.next.next = ListNode(5)


class Solution:
    # 200. Number of Islands
    def numIslands(self, grid):
        numIslands = 0
        rows, cols = len(grid), len(grid[0])
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    self.numIslandsHelper(grid, rows, cols, row, col)
                    numIslands += 1
        return numIslands

    def numIslandsHelper(self, grid, num_rows, num_cols, row, col):
        # If visited just return false
        movements_i = [1, -1, 0, 0]
        movements_j = [0, 0, 1, -1]
        # Since we are in land, explore as much as we can (BFS)
        grid[row][col] = "*"
        queue = [[row, col]]
        while queue:
            row, col = queue.pop(0)
            for k in range(len(movements_i)):
                new_row = row + movements_i[k]
                new_col = col + movements_j[k]
                if self.isValidPosition(num_rows, num_cols, new_row, new_col) and grid[new_row][new_col] == "1":
                    grid[new_row][new_col] = "*"
                    queue.append([new_row, new_col])

    def isValidPosition(self, num_rows, num_cols, row, col):
        return 0 <= row < num_rows and 0 <= col < num_cols

    # 662. Maximum Width of Binary Tree
    def widthOfBinaryTree(self, root):
        # BFS position and depth iteration-calc approach
        queue = [(root, 1, 0)]  # (node, depth, pos)
        curr_depth = left = maxWidth = 0
        while queue:
            node, depth, pos = queue.pop(0)
            if node:
                # append children
                queue.append((node.left, depth + 1, pos * 2))
                queue.append((node.left, depth + 1, pos * 2 + 1))
                # we're at a new level, update left pointer
                if curr_depth != depth:
                    curr_depth = depth
                    left = pos
                maxWidth = max(pos - left + 1, maxWidth)  # subtract right most pointer, minus left to get widths
        return maxWidth

    # 109. Convert Sorted List to Binary Search Tree
    def sortedListToBST(self, head):
        if not head:
            return

        # case we're at the end of the list
        if not head.next:
            return TreeNode(head.val)

        mid = self.midAndCut(head)
        root = TreeNode(mid.val)

        # recursively fill left and right subtree
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)

        return root

    def midAndCut(self, head):
        # helper function to find the mid node of a linked list using fast-slow technique
        slow = head
        fast = head.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        tmp = slow.next
        slow.next = None
        return tmp

    def DLLtoBST(self, head):
        return self.DLLtoBSTHelper(head)

    def DLLtoBSTHelper(self, head, prev=None):
        if not head:
            return

        if not prev:
            prev = head
        else:
            head.prev = prev

        return self.DLLtoBSTHelper(head.next, prev)


sol = Solution()

# DONE
# sol.numIslands([
#     ["1", "1", "1", "1", "0"],
#     ["1", "1", "0", "1", "0"],
#     ["1", "1", "0", "0", "0"],
#     ["0", "0", "0", "0", "0"]
# ])
# sol.widthOfBinaryTree(tn)
# sol.sortedListToBST(ll)
print(sol.DLLtoBST(dll1).val)

# TO DO
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
# sol.nextGreaterElement([4,1,2], [1,3,4,2])
# sol.moveZeroes([0,1,0,3,12])
# sol.uniquePaths(23, 12)
# sol.uniquePathsWithObstacles([[0,0]])
# sol.nextGreaterElements([1, 2, 1])
# sol.nextGreaterElementIII(23102431)
# sol.generateParenthesis(3)
# sol.printList(sol.oddEvenList(ll))
# sol.longestSubstring("ababacb", 3)
# sol.maxSubArray([5,4,-1,7,8])
# sol.minDeletions("bbcebab")
# sol.validPalindrome("race a car")
# sol.minSwapsToPalindrome("ntiin")
# sol.minStepsPilesEqual([1, 1, 2, 2, 2, 3, 3, 3, 4, 4])
# sol.largestK([3,2,-2,5,-3])
# sol.maxLength(["un","iq","ue"]) # -> 4
# sol.sumZero(3)
# sol.canPartitionKSubsets([2, 2, 2, 2, 3, 4, 5], 4)
# sol.findLargestAlphabeticChar("dAeB")
