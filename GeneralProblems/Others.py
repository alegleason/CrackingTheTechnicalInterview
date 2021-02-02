# Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.
class Solution:
    def getSum(self, a, b):
        # We need the mask bc python types are not limited
        mask = 0xffffffff
        # Iterate until there is no carry
        while b != 0:
            # We do the actual sum by XORing
            tempSum = (a ^ b) & mask
            # To get the carrying bits, we & (since 1 & 1 = 1)
            b = a & b
            # a will hold "result" of the sum
            a = tempSum
            # b will hold the carrying bits
            b = (b << 1) & mask
        if (a >> 31) & 1:  # If a is negative in 32 bits sense
            return ~(a ^ mask)
        return a

sol = Solution()
print(sol.getSum(-1, 1))