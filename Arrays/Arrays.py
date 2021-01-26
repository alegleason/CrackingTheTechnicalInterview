class Solution:
    def pivotIndex(self, nums):
        # O(n) time complexity and O(1) space complexity
        S = sum(nums)
        leftSum = 0

        for i, num in enumerate(nums):
            # Accumulate left sum, calculate right sum at each iteration
            if leftSum == (S - num - leftSum):
                return i
            leftSum += num

        return -1


sol = Solution()
# print(sol.pivotIndex([1,7,3,6,5,6]))
