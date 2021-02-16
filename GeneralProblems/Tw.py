from collections import deque


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
    # print(maxEvents([1, 3, 3, 5, 7], [2, 2, 1, 2, 1]))  # 4


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
    print(left)
    print(right)
    # Calculate the results in the form of res = sum(A[i] * f(i))
    res = 0
    for i in range(n):
        res += left[i] * right[i] * A[i]
    return res


# 739. Daily Temperatures LeetCode
def dailyTemperatures(T):
    # O(n) time and space complexity
    n = len(T)
    result = [0] * n
    stack = deque()
    for i in range(n-1, -1, -1):
        # Pop the stack until we find a greater element than us
        while stack and T[stack[-1]] <= T[i]:
            stack.pop()
            # The result on the previous index is the distance between it and current
        result[i] = 0 if len(stack) == 0 else stack[-1] - i
        stack.append(i)

    return result


print(dailyTemperatures([73,74,75,71,69,72,76,73]))

# for i in range(n):
#     count = 1
#     while stack and stack[-1][0] > A[i]:
#         count += stack.pop()[1]
#     left[i] = count
#     stack.append([A[i], count])
# stack.clear()
# for i in range(n - 1, -1, -1):
#     count = 1
#     while stack and stack[-1][0] >= A[i]:
#         count += stack.pop()[1]
#     right[i] = count
#     stack.append([A[i], count])
# res = 0
# # Calculate the results in the form of res = sum(A[i] * f(i))
# for i in range(n):
#     res += A[i] * left[i] * right[i]
# return res % mod
