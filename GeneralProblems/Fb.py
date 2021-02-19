from collections import deque, defaultdict
import heapq
import sys


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


def CalculateTaxes(income, tax_brackets_table):  # 8,000
    if len(tax_brackets_table) == 0:
        raise Exception('Please check table')
    if income <= 0:
        return 0
    total_tax = 0
    # O(b) time complexity where b is the number of elements we have on the bracket table
    for tax_entree in tax_brackets_table:
        # We are on the last line
        if not tax_entree[0]:
            total_tax += income * tax_entree[1]
            return total_tax

        # Check if we can subtract
        new_income = income - tax_entree[0]  # -7,000
        if new_income >= 0:
            # Perform the tax calculation
            income = new_income  # 3,000
            total_tax += tax_entree[1] * tax_entree[0]
            # total_tax += tax_entree[1] * min(tax_entree[0], income)
        else:
            total_tax += tax_entree[1] * income  # 3,000 * .1
            break
    return total_tax


# CalculateTaxes(8000, [[5000, 0], [10000, .1], [20000, .2], [10000, .3], [None, .4]])

class Solution:
    # 39. Combination Sum LeetCode
    def combinationSum(self, candidates, target):
        # O(n^n) time and O(n*n) space complexity
        res = []
        self.combinationHelper(candidates, target, 0, [], res)
        return res

    def combinationHelper(self, candidates, target, idx, curr_candidates, res):
        # Base cases
        if target == 0:
            # Valid combination
            res.append(curr_candidates)
            return
        elif target < 0:
            # Invalid number
            return
        # Perform DFS
        for i in range(idx, len(candidates)):
            self.combinationHelper(candidates, target - candidates[i], i, curr_candidates + [candidates[i]],
                                   res)  # Same position

    # 22. Generate Parentheses LeetCode
    def generateParenthesis(self, n):
        # O(2^n) time and O(n*2) space complexity
        res = []
        self.generateParenthesisHelper(n, n, "", res)
        return res

    # Inside fx so res has same scope
    def generateParenthesisHelper(self, left, right, curr, res):
        # Base case
        if not left and not right:
            res.append(curr)
            return
        # Recursion - Depth First
        temp = curr + "("
        if left > 0:
            self.generateParenthesisHelper(left - 1, right, temp, res)
        if right > left:
            curr += ")"
            self.generateParenthesisHelper(left, right - 1, curr, res)

    # 50. Pow(x, n) LeetCode
    def myPow(self, x, n):
        # Lets use the idea that x^5 is the same as x^2 * x^2 * x^1 and save 50% of the time
        # O(logn) time and O(n) space complexity (call stack)
        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n < 0:
            # Convert to fraction and positive, which is equivalent
            x = 1 / x
            n *= -1
        result = self.myPow(x, n // 2)
        result *= result
        if n % 2 == 1:
            result *= x
        return result

    # 93. Restore IP Addresses LeetCode
    def restoreIpAddresses(self, s):
        # O(2^n) time and O(n^2) space complexity
        res = []
        # Actual DFS call
        self.restoreIPAddressesHelper(s, 0, "", res)
        return res

    def restoreIPAddressesHelper(self, s, idx, path, res):
        # We do not want to have combinations greater than 3 chars
        if idx > 4:
            return
        # Just add if there are no more numbers to look at
        if idx == 4 and not s:
            res.append(path[:-1])  # Remove the last '.'
            return
        # Advance at most 4 positions, or at the end of the total numbers
        for i in range(1, min(len(s) + 1, 4)):
            # Allowing alone, intermediate or final 0s, but blocking format '.0xx.' or IPs greater than 256
            if s[:i] == '0' or (s[0] != '0' and 0 < int(s[:i]) < 256):
                self.restoreIPAddressesHelper(s[i:], idx + 1, path + s[:i] + ".", res)

    # 121. Best Time to Buy and Sell Stock LeetCode
    def maxProfit(self, prices):
        # Using Kadane's algorithm so we can handle negative inputs
        max_cur, max_so_far = 0, 0
        for i in range(1, len(prices)):
            temp = max_cur + prices[i] - prices[i - 1]
            max_cur = max(0, temp)
            max_so_far = max(max_cur, max_so_far)
        return max_so_far

    # 53. Maximum Subarray LeetCode
    def maxSubArray(self, nums):
        # Using DP
        max_so_far = nums[0]
        for i in range(1, len(nums)):
            if nums[i] + nums[i - 1] > nums[i]:
                nums[i] += nums[i - 1]
            if nums[i] > max_so_far: max_so_far = nums[i]
        return max_so_far

    # 71. Simplify Path LeetCode
    def simplifyPath(self, path):
        stack = deque()
        path = path.split('/')
        for p in path:
            if p == '.':
                continue
            elif p == '..':
                if stack:
                    stack.pop()
            elif p != '':
                stack.append(p)
        return '/' + '/'.join(list(stack))

    # 138. Copy List with Random Pointer LeetCode
    def copyRandomList(self, head: 'Node') -> 'Node':
        # O(2n) time and O(1) space complexity
        new_list = defaultdict(lambda: None)
        # Copy as a dictionary on a first pass to have acess to all node objects
        n = head
        while n:
            # We basically copy the list to have access to the node by object reference
            new_list[n] = Node(n.val)
            n = n.next
        # Now, update both the random and next pointers
        n = head
        while n:
            new_list[n].next = new_list[n.next]
            new_list[n].random = new_list[n.random]
            n = n.next
        return new_list[head]

    # 140. Word Break II LeetCode
    def wordBreak(self, s, wordDict):
        return self.wordBreakHelper(s, wordDict, dict())

    def wordBreakHelper(self, s, wordDict, dp):
        results = []
        # Base case
        if s == "":
            results.append("")
            return results
        elif s in dp:
            # Use memoization
            return dp[s]

        # Recursive calls
        for word in wordDict:
            if s.startswith(word):
                subset = self.wordBreakHelper(s[len(word):], wordDict, dp)

                for subst in subset:
                    # Just add the space if we actually got a result back
                    opt_space = " " if subst != "" else ""
                    results.append(word + opt_space + subst)

        dp[s] = results
        return results

    # 199. Binary Tree Right Side View LeetCode
    def rightSideView(self, root):
        # BFS approach
        if not root: return []
        queue = deque()
        queue.append(root)
        res = [root.val]
        while queue:
            # BFS uses a queue DS
            q = len(queue)
            level = []
            for i in range(q):
                curr_node = queue.popleft()
                # Append child nodes
                if curr_node.left:
                    queue.append(curr_node.left)
                    level.append(curr_node.left.val)
                if curr_node.right:
                    queue.append(curr_node.right)
                    level.append(curr_node.right.val)
            if level: res.append(level[-1])
        return res

    # 347. Top K Frequent Elements LeetCode
    def topKFrequent(self, nums, k):
        # O(NlogK) time and O(N) space complexity
        ans = []
        freq = dict()
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        # Use a min heap to store the most frequent elements
        for key, value in freq.items():
            if len(ans) < k:
                heapq.heappush(ans, [value, key])
            else:
                # heappushpop() removes and returns the smallest element
                heapq.heappushpop(ans, [value, key])

        # Return the top k frequent elements, which are stored in the key part
        return [key for value, key in ans]

    # 238. Product of Array Except Self LeetCode
    def productExceptSelf(self, nums):
        # O(n) time and O(1) space complexity
        n = len(nums)
        ans = [0] * n
        R = ans[0] = 1
        # Fill left and right product arrays
        for i in range(1, n):
            ans[i] = nums[i - 1] * ans[i - 1]
        for i in reversed(range(n)):
            ans[i] = ans[i] * R
            R *= nums[i]
        return ans

    # 286. Walls and Gates LeetCode
    def wallsAndGates(self, rooms):
        if not rooms: return []
        for row in range(len(rooms)):
            for col in range(len(rooms[row])):
                if rooms[row][col] == 0:
                    self.DFS(row, col, 0, rooms)
        return rooms

    def DFS(self, row, col, count, rooms):
        if self.isValidCell(row, col, count, rooms):
            rooms[row][col] = count
            # Traverse neighboring cells
            row_movements = [-1, 0, 1, 0]
            col_movements = [0, 1, 0, -1]
            for i in range(len(row_movements)):
                self.DFS(row+row_movements[i], col+col_movements[i], count + 1, rooms)

        return

    def isValidCell(self, row, col, count, rooms):
        # Inside boundaries
        if 0 <= row < len(rooms) and 0 <= col < len(rooms[0]):
            if rooms[row][col] < count:
                return False
            else:
                return True
        return False


sol = Solution()
# print(sol.generateParenthesis(3))
# print(sol.combinationSum([2, 3, 6, 7], 7))
# print(sol.myPow(2.0, 10))
# print(sol.restoreIpAddresses("101023"))
# print(sol.maxProfit([7, 1, 5, 6]))
# print(sol.maxSubArray([7, 1, 5, 6]))
# print((sol.simplifyPath("/home/")))
# print(sol.wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]))
# print(sol.rightSideView(root))
# print(sol.topKFrequent([1,1,1,2,2,3], 2))
# print(sol.productExceptSelf([1,2,3,4]))
inf = sys.maxsize
mat = [
    [inf,inf, inf],
    [0,inf,-1],
    [inf,-1,inf]
    ]
print(sol.wallsAndGates(mat))

