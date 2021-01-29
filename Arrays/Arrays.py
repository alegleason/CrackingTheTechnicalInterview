import sys
from collections import deque


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

    # 498. Diagonal Traverse - Medium
    def findDiagonalOrder(self, matrix):
        diagonalOrder = []
        if not matrix:
            return diagonalOrder

        N, M = len(matrix[0]), len(matrix)
        D = M + N - 1
        goingUp = True
        for d in range(D):
            row = 0 if d < N else d - N + 1
            col = d if d < N else N - 1
            tempQueue = deque()
            while row < M and col >= 0:
                tempQueue.appendleft(matrix[row][col]) if goingUp else tempQueue.append(matrix[row][col])
                row += 1
                col -= 1
            diagonalOrder.extend(list(tempQueue))
            goingUp = not goingUp

        return diagonalOrder


sol = Solution()
# print(sol.pivotIndex([1,7,3,6,5,6]))
# print(sol.dominantIndex([0,0,3,2]))
print(sol.findDiagonalOrder([ [ 1, 2, 3], [ 4, 5, 6 ], [ 7, 8, 9 ] ]))
