import sys


class Solution:
    # Find Pivot Index - Introduction to Array
    def pivotIndex(self, nums):
        # O(n) time complexity and O(1) space complexity where n is the length of nums
        S = sum(nums)
        leftSum = 0

        for i, num in enumerate(nums):
            # Accumulate left sum, calculate right sum at each iteration
            if leftSum == (S - num - leftSum):
                return i
            leftSum += num

        return -1

    # Largest Number At Least Twice of Others - Introduction to Array
    def dominantIndex(self, nums):
        # O(n) time complexity and O(1) space complexity where n is the length of nums
        maxNum = sys.maxsize * -1
        secMaxNum = sys.maxsize * -1
        maxNumIdx = -1

        for i, num in enumerate(nums):
            if num > maxNum:
                secMaxNum = maxNum
                maxNum = num
                maxNumIdx = i
            if maxNum > num > secMaxNum:
                secMaxNum = num
        # If the max number is greater or equal than the second max number divided by 2,
        # it means that it is valid for the whole array, otherwise, invalid
        if maxNum >= secMaxNum * 2:
            return maxNumIdx
        return -1


sol = Solution()
# print(sol.pivotIndex([1,7,3,6,5,6]))
# print(sol.dominantIndex([0,0,3,2]))
