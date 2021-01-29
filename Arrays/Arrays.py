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

    # Return true if all chars on the string are unique otherwise false
    def isUnique(self, string):
        # We could argue it is both O(1) in time and space bc 128 is the limit
        chars = [False for _ in range(128)]
        for char in string:
            if chars[ord(char)]:
                return False
            chars[ord(char)] = True
        return True

    # Return true if all chars on the string are unique otherwise false
    def isUniqueImproved(self, string):
        # Improve space complexity by using bitwise operation to check if the bit in that position has been turned on
        chars = 0
        for char in string:
            # If the bit has been turned on...
            if chars & 1 << ord(char) > 0:
                return False
            # Mark the bit as visited with an or operation
            chars |= (1 << ord(char))
        return True

    # Return true if one string is a permutation of the other
    def isPermutation(self, s1, s2):
        # O(m+n) time complexity, O(128) space
        if len(s1) != len(s2):
            return False
        # We assume is ASCII string, case sensitive and white spaces matter
        charCount = [0] * 128
        for char in s1:
            charCount[ord(char)] += 1
        for char in s2:
            charCount[ord(char)] -= 1
            # Check for discrepancies
            if charCount[ord(char)] < 0:
                return False
        return True

    # Given a string with white spaces, return it with them substituted by %20
    def URLify(self, string, realLength):
        # O(n) time complexity, O(1) space complexity
        if not string:
            return
        spaceCount = 0
        for i in range(realLength):
            if string[i] == ' ':
                spaceCount += 1
        totalLength = realLength + spaceCount*2
        while realLength:
            if string[realLength - 1] != ' ':
                string[totalLength - 1] = string[realLength - 1]
                totalLength -= 1
            else:
                string[totalLength - 1] = '0'
                string[totalLength - 2] = '2'
                string[totalLength - 3] = '%'
                totalLength -= 3
            realLength -= 1
        return ''.join(string)




sol = Solution()
# print(sol.pivotIndex([1,7,3,6,5,6]))
# print(sol.dominantIndex([0,0,3,2]))
# print(sol.findDiagonalOrder([ [ 1, 2, 3], [ 4, 5, 6 ], [ 7, 8, 9 ] ]))
# print(sol.isUnique("abcdefghijklmnopqrstuvwxyzg"))
# print(sol.isPermutation("abc", "bca"))
# print(sol.URLify(['M', 'r', ' ', 'J', 'o', 'e', ' ', 'B', 'l', 'a', 'n', 't', 'o', 'n', ' ', ' ', ' ', ' '], 14))
