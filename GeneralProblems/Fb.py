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
                self.DFS(row + row_movements[i], col + col_movements[i], count + 1, rooms)

        return

    def isValidCell(self, row, col, count, rooms):
        # Inside boundaries
        if 0 <= row < len(rooms) and 0 <= col < len(rooms[0]):
            if rooms[row][col] < count:
                return False
            else:
                return True
        return False

    # 300. Longest Increasing Subsequence LeetCode
    def lengthOfLIS(self, nums):
        # O(n2) time and O(n) space complexity
        n = len(nums)
        if n == 1:
            return 1

        dp = [1] * n
        max_dp = 1
        for j in range(1, n):
            lis = 1
            for i in range(j):
                if nums[j] > nums[i]:
                    lis = max(lis, dp[i] + 1)
            dp[j] = lis
            max_dp = max(max_dp, dp[j])

        return max_dp

    # 354. Russian Doll Envelopes
    def maxEnvelopes(self, envelopes):
        # O(n2) time and O(n) space complexity
        n = len(envelopes)
        if n == 1:
            return 1
        elif n == 0:
            return 0
        dp = [1] * n
        dp_max = 1
        # Sort width and height by ascending order
        envelopes.sort()
        for j in range(n):
            lis = 1
            for i in range(j):
                # Compare both width and height to check for fit
                if envelopes[j][0] > envelopes[i][0] and envelopes[j][1] > envelopes[i][1]:
                    lis = max(lis, dp[i] + 1)
            dp[j] = lis
            dp_max = max(dp[j], dp_max)

        return dp_max

    # 674. Longest Continuous Increasing Subsequence LeetCode
    def findLengthOfLCIS(self, nums):
        if not nums: return 0
        # O(n) time and O(1) space
        max_len = 1
        lics = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                lics += 1
            else:
                max_len = max(lics, max_len)
                lics = 1

        return max(max_len, lics)

    # 62. Unique Paths
    def uniquePaths(self, m, n):
        memoize = [[None for _ in range(n + 1)] for _ in range(m + 1)]
        return self.uniquePathsDFS(m, n, 0, 0, memoize)

    def uniquePathsDFS(self, m, n, row, col, grid):
        # Check boundaries
        if row == (m - 1) and col == (n - 1):
            return 1
        elif row < 0 or row >= m or col < 0 or col >= n:
            return 0
        # Achieved goal
        elif grid[row][col] is not None:
            return grid[row][col]
        # DFS
        grid[row][col] = self.uniquePathsDFS(m, n, row, col + 1, grid) + self.uniquePathsDFS(m, n, row + 1, col, grid)
        return grid[row][col]

    # 400. Nth Digit LeetCode
    def findNthDigit(self, n):
        # 1st step: Find tier
        level = low = 1
        top = 9
        while n > level * top:
            n -= level * top
            level += 1
            low *= 10
            top *= 10
        # 2nd step: Find number
        low += (n - 1) / level
        # 3rd step: Find the digit
        return str(low)[(n - 1) % level]

    # 637. Valid Word Abbreviation LeetCode
    def validAbbr(self, s, abbr):
        n = len(s)
        a = len(abbr)
        i = 0
        j = 0
        while i < a:
            if abbr[i].isnumeric():
                t = " "
                while True and i < a:
                    if abbr[i].isnumeric():
                        t += abbr[i]
                    else:
                        break
                    i += 1
                j += int(t)
                if j > n:
                    return False
                elif j == n:
                    return True

            if abbr[i] != s[j]:
                return False
            i += 1
            j += 1

        return True

    # 415. Add Strings LeetCode
    def addStrings(self, num1, num2):
        # O(n) time and O(1) space complexity
        ln1 = len(num1)
        ln2 = len(num2)
        num1 = num1[::-1]
        num2 = num2[::-1]
        carry = res = 0
        # Perform basic math addition
        for i in range(max(ln1, ln2)):
            t1 = t2 = "0"
            if i < ln1:
                t1 = num1[i]
            if i < ln2:
                t2 = num2[i]
            # ord() return the ascii val, converting it
            temp = (ord(t1) - 48 + ord(t2) - 48 + carry)
            if temp > 10:
                res += (temp % 10) * (pow(10, i))
                carry = 1
            else:
                res += temp * (pow(10, i))
                carry = 0
        # Add final carry
        if carry:
            res += 1 * (pow(10, max(ln1, ln2)))
        return str(res)

    memo = {}

    # 494. Target Sum LeetCode
    def findTargetSumWays(self, nums, S):
        if not nums:
            return 0
        idx = len(nums) - 1
        curr_sum = 0
        return self.findTargetSumWaysHelper(nums, S, idx, curr_sum)

    def findTargetSumWaysHelper(self, nums, target, index, curr_sum):
        # Base case - Memoization
        if (index, curr_sum) in self.memo:
            return self.memo[(index, curr_sum)]

        # Going backwards
        if index < 0 and curr_sum == target:
            return 1
        if index < 0:
            return 0

        # Recursive exploration
        pos = self.findTargetSumWaysHelper(nums, target, index - 1, curr_sum + nums[index])
        neg = self.findTargetSumWaysHelper(nums, target, index - 1, curr_sum - nums[index])

        self.memo[(index, curr_sum)] = pos + neg
        return self.memo[(index, curr_sum)]

    def checkOperations(self, a, signs, b, c):
        # Declare output list of same length
        output = [False] * len(a)
        for i, sign in enumerate(signs):
            # Hold the current operation for later compare
            curr = a[i] + b[i] if sign == '+' else a[i] - b[i]  # a[i] sign[i] b[i]
            # Compare the result and adjust if needed
            if curr == c[i]:
                output[i] = True
        # Return boolean like list
        return output

    def binaryPatternMatching(self, pattern, s):
        vowels = {'a', 'e', 'i', 'o', 'u', 'y'} # create a set of vowels for O(1) access
        matches = 0
        i = 0
        # Let's try comparing letter by letter on the run
        while i < (len(s)):
            j = i
            for idx, char in enumerate(pattern):
                currChar = s[j]
                # Break if any condition was not met
                if char == "0" and currChar not in vowels:
                    break
                elif char == "1" and currChar in vowels:
                    break
                # If we have arrived at the end, update the counter
                if idx == len(pattern) - 1:
                    matches += 1
                j += 1
            i += 1
        return matches


sol = Solution()
# print(sol.binaryPatternMatching("010", "amazing"))
# print(sol.checkOperations([3, 2, -1, 4], ['+', '-', '-', '+'], [2, 7, -5, 2], [5, 5, 4, 2]))
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
# print(sol.wallsAndGates(mat))
# print(sol.lengthOfLIS([0,3,1,6,2,2,7]))
# print(sol.maxEnvelopes([[5,4],[6,5],[6,7],[2,3]]))
# print(sol.findLengthOfLCIS([1,3,5,4,2,3,4,5]))
# print(sol.uniquePaths(3, 7))
# print(sol.findNthDigit(1000))
# print(sol.validAbbr("word", "1o1d"))
# print(sol.addStrings("9", "9"))
# print(sol.findTargetSumWays([1, 0], 1))
