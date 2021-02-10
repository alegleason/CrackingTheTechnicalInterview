class Solution:
    def generateParenthesis(self, n):
        # O(2^n) time and O(n*2) space complexity
        res = []

        # Inside fx so res has same scope
        def generateParenthesisHelper(left, right, curr, res):
            # Base case
            if not left and not right:
                res.append(curr)
                return
            # Recursion - Depth First
            temp = curr + "("
            if left > 0:
                generateParenthesisHelper(left - 1, right, temp, res)
            if right > left:
                curr += ")"
                generateParenthesisHelper(left, right - 1, curr, res)

        generateParenthesisHelper(n, n, "", res)
        return res


sol = Solution()
print(sol.generateParenthesis(3))
