import sys
from collections import deque
import math


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
        totalLength = realLength + spaceCount * 2
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

    # Given a string, check if it is a permutation of a palindrome
    def palindromePermutation(self, string):
        string = string.lower()
        bitVector = 0
        # Setting the vector's bits on and off
        for char in string:
            if char.isalpha():
                mask = 1 << ord(char)
                # Toggling the bits
                if bitVector & mask == 0:
                    # Turn it on
                    bitVector |= mask
                else:
                    # Turn it back off
                    bitVector &= ~mask
        return ((bitVector - 1) & bitVector) == 0 or bitVector == 0

    # Check if two strings are one or zero editions away (insert, remove, replace)
    def oneAway(self, s1, s2):
        lenS1 = len(s1)
        lenS2 = len(s2)
        # O(n) time and O(1) space complexity
        if lenS1 == lenS2:
            # Check for replacements or equality
            differenceFound = False
            for i in range(lenS1):
                if s1[i] != s2[i]:
                    if differenceFound:
                        return False
                    differenceFound = True
            return True
        elif abs(lenS1 - lenS2) == 1:
            # Check for insertions or deletions
            differenceFound = False
            idxS1, idxS2 = 0, 0
            while idxS1 < lenS1 and idxS2 < lenS2:
                if s1[idxS1] != s2[idxS2]:
                    if differenceFound:
                        return False
                    differenceFound = True
                    if lenS1 > lenS2:
                        idxS1 += 1
                    else:
                        idxS2 += 1
                idxS1 += 1
                idxS2 += 1
            return True
        else:
            return False

    # Implement a method to perform string compression as aabcccccaa -> a2b1c5a3
    def stringCompression(self, string):
        # We could add a first traverse that checks if there will not be need for a string builder, though it adds time
        retStr = []
        compressionFlag = False
        # O(n) both time and space complexity
        i = 0
        while i < len(string):
            if i + 1 < len(string) and string[i] == string[i + 1]:
                compressionFlag = True
                tempCount = 1
                tempChar = string[i]
                while i + 1 < len(string) and string[i] == string[i + 1]:
                    i += 1
                    tempCount += 1
                # Concat uses n2 time, that is why we use a list
                retStr.append(tempChar)
                retStr.append(str(tempCount))
            else:
                retStr.append(string[i])
                retStr.append("1")
            i += 1
        return ''.join(retStr) if compressionFlag else string

    # Given a NxN matrix, rotate it 90 degrees in place
    def rotateMatrix(self, mat):
        # O(n2) time and O(1) space complexity
        if not mat or (len(mat) != len(mat[0])):
            return False
        N = len(mat)
        for level in range(math.ceil(N / 2)):
            first = level
            last = N - 1 - level
            for i in range(first, last):
                offset = i - first
                top = mat[first][i]
                # left -> top
                mat[first][i] = mat[last - offset][first]
                # bottom -> left
                mat[last - offset][first] = mat[last][last - offset]
                # right -> bottom
                mat[last][last - offset] = mat[i][last]
                # top -> right
                mat[i][last] = top
        return mat

    # Given a matrix, put the row and col to 0 if an element is equal to 0
    def zeroMatrix(self, mat):
        # O(n2) time and O(1) space complexity
        # We will use the first position in each row and col as markers
        firstRowZero = False
        firstColZero = False
        # Search if first row has zeroes
        for col in range(len(mat[0])):
            if mat[0][col] == 0:
                firstRowZero = True
                break
        # Search if first col has zeroes
        for row in range(len(mat)):
            if mat[row][0] == 0:
                firstColZero = True
                break

        for row in range(1, len(mat)):
            for col in range(1, len(mat[0])):
                if mat[row][col] == 0:
                    mat[0][col] = 0
                    mat[row][0] = 0

        # Now we can fill rows and cols
        for row in range(1, len(mat)):
            if mat[row][0] == 0:
                self.setRowZeroes(mat, row)

        for col in range(1, len(mat[0])):
            if mat[0][col] == 0:
                self.setColZeroes(mat, col)

        if firstRowZero:
            self.setRowZeroes(mat, 0)

        if firstColZero:
            self.setColZeroes(mat, 0)

        return mat

    def setRowZeroes(self, mat, row):
        for col in range(len(mat[0])):
            mat[row][col] = 0

    def setColZeroes(self, mat, col):
        for row in range(1, len(mat)):
            mat[row][col] = 0

    def stringRotation(self, s1, s2):
        # s1 is rotated, s2 is original
        s1 = s1 + s1
        return True if s2 in s1 else False



sol = Solution()
# print(sol.pivotIndex([1,7,3,6,5,6]))
# print(sol.dominantIndex([0,0,3,2]))
# print(sol.findDiagonalOrder([ [ 1, 2, 3], [ 4, 5, 6 ], [ 7, 8, 9 ] ]))
# print(sol.isUnique("abcdefghijklmnopqrstuvwxyzg"))
# print(sol.isPermutation("abc", "bca"))
# print(sol.URLify(['M', 'r', ' ', 'J', 'o', 'e', ' ', 'B', 'l', 'a', 'n', 't', 'o', 'n', ' ', ' ', ' ', ' '], 14))
# print(sol.palindromePermutation("Tact Coa"))
# print(sol.oneAway("pale", "bake"))
# print(sol.stringCompression("aabcccccaaa"))
# print(sol.rotateMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
# print(sol.zeroMatrix([[0, 2, 3], [4, 0, 6], [7, 8, 9]]))
print(sol.stringRotation("erbottlewat", "waterbottle"))