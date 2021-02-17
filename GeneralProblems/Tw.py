from collections import deque
import enum
import sys


# Given an array of arrival times and duration, determine the max number of events
def maxEvents(arrival, duration):
    # O(nlogn) time and O(n) space
    for i in range(len(duration)):
        # Replace duration x end time
        duration[i] += arrival[i]
    # Create new array in form [startTime, endTime]
    times = []
    for i in range(len(duration)):
        times.append([arrival[i], duration[i]])
    # Sort by end time
    times.sort(key=lambda x: x[1])
    # Greedy approach
    count = 1
    et = times[0][1]
    for i in range(1, len(times)):
        # If next start time <= than our current end time, add the event
        if times[i][0] >= et:
            et = times[i][1]
            count += 1
    return count
    # print(maxEvents([1, 3, 3, 5, 7], [2, 2, 1, 2, 1]))  -> 4


# 907. Sum of Subarray Minimums LeetCode
def sumSubarrayMins(A):
    # O(n) time and space complexity
    n, mod = len(A), 10 ** 9 + 7
    # declare left and right holders
    left, right = [0] * n, [0] * n
    # stacks for monotonous increase stack
    stack = deque()
    # Calculate for each position [i] all elements that are lesser to the left
    for i in range(n):
        count = 1
        while stack and stack[-1][0] > A[i]:
            count += stack.pop()[1]
        left[i] = count
        stack.append([A[i], count])
    stack.clear()
    # Do the same for the right part
    for i in range(n - 1, -1, -1):
        count = 1
        while stack and stack[-1][0] >= A[i]:
            count += stack.pop()[1]
        right[i] = count
        stack.append([A[i], count])
    # Calculate the results in the form of res = sum(A[i] * f(i))
    res = 0
    for i in range(n):
        res += left[i] * right[i] * A[i]
    return res % mod
    # print(sumSubarrayMins([3,1,2,4]))# -> 17


# 739. Daily Temperatures LeetCode
def dailyTemperatures(T):
    # O(n) time and space complexity
    n = len(T)
    result = [0] * n
    stack = deque()
    for i in range(n - 1, -1, -1):
        # Pop the stack until we find a greater element than us
        while stack and T[stack[-1]] <= T[i]:
            stack.pop()
            # The result on the previous index is the distance between it and current
        result[i] = 0 if len(stack) == 0 else stack[-1] - i
        stack.append(i)

    return result
    # print(dailyTemperatures([73,74,75,71,69,72,76,73])) -> [1, 1, 4, 2, 1, 1, 0, 0]


# Given an array of prices, determine the discount for each price, which is, the next number lesser or equal than it
def minDiscount(D):
    n = len(D)
    # Next Less Elements Indexes help calculate discount
    discounts = D.copy()
    stack = deque()
    notChanged = set()
    for i in range(n):
        while stack and D[i] <= D[stack[-1]]:
            x = stack.pop()
            # Update all previous indexes that had not found a lesser element
            discounts[x] = D[x] - D[i]
            # Get elements without discount
            notChanged.remove(x)
        stack.append(i)
        notChanged.add(i)

    return sum(discounts), notChanged
    # print(minDiscount([5, 4, 5, 1, 3, 3, 8, 2]))  # -> totalDisc = 18, elemNoDisc = 3, 7


class Cell(enum.Enum):
    Unknown = 1
    Impossible = 2
    Possible = 3


# 55. Jump Game LeetCode
def canJump(nums):
    # O(n^2) time and O(n) space
    n = len(nums)
    # Initialize DP structure
    dp = [Cell.Unknown] * n
    # Mark last cell as possible (itself)
    dp[n - 1] = Cell.Possible
    return canJumpRecursive(0, dp, nums)
    # print(canJump([2, 3, 1, 1])) -> True


def canJumpRecursive(start, dp, nums):
    # Base case
    if dp[start] != Cell.Unknown:
        return True if dp[start] == Cell.Possible else False

    # Recursive calls
    maxSteps = min(len(nums) - 1, nums[start] + start)
    for i in range(start + 1, maxSteps + 1):
        if canJumpRecursive(i, dp, nums):
            dp[start] = Cell.Possible
            return True

    dp[start] = Cell.Impossible
    return False


# 45. Jump Game II LeetCode
def canJumpII(nums):
    # O(n) time and O(1) space complexity
    if not nums or len(nums) == 1:
        return 0
    # BFS similarity
    furthest = nums[0]
    curr_end = nums[0]
    jumps = 1
    n = len(nums)
    # Greedy approach
    for i in range(1, n):
        if i == n - 1:
            return jumps
        if i + nums[i] > furthest:
            furthest = i + nums[i]
        # We have finished processing the level
        if i == curr_end:
            jumps += 1
            curr_end = furthest
    return jumps


print(canJumpII([1,2,3]))
