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

    @staticmethod
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
                queue.append((node.left, depth + 1, pos * 2)) # good technique to use depth to track the current level
                queue.append((node.right, depth + 1, pos * 2 + 1))
                if depth != curr_depth:
                    curr_depth = depth
                    left = pos
                ans = max(pos - left + 1, ans)
        return ans






class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


sol = Solution()
# print(sol.numIslands([
#     ["1", "1", "0", "0", "0"],
#     ["1", "1", "0", "0", "0"],
#     ["0", "0", "1", "0", "0"],
#     ["0", "0", "0", "1", "1"]
# ]))

tn = TreeNode(1)
tn.left = TreeNode(3)
tn.right = TreeNode(2)
tn.left.left = TreeNode(5)
tn.left.right = TreeNode(3)
tn.right.right = TreeNode(9)

print(sol.widthOfBinaryTree(tn))
