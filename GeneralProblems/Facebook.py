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

    # Implement pow(x, n), which calculates x raised to the power n (i.e. xn).
    def myPow(self, x, n):
        # Lets use the idea that x^5 is the same as x^2 * x^2 * x^1 and save 50% of the time
        # O(logn) time and O(n) space complexity (call stack)
        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n < 0:
            # Convert to fraction and positive, which is equivalent
            x = 1/x
            n *= -1
        result = self.myPow(x, n//2)
        result *= result
        if n % 2 == 1:
            result *= x
        return result


sol = Solution()
print(sol.generateParenthesis(3))
print(sol.combinationSum([2, 3, 6, 7], 7))
print(sol.myPow(2.0, 10))
print(sol.myPow(2.1, 3))
print(sol.myPow(2.0, -2))
