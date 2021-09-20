"""
  main.py
  1486D - Max Median


  Created by Alejandro Gleason on 09/18/21.
  Copyright © 2021 Alejandro Gleason. All rights reserved.
"""

if __name__ == '__main__':
    n, k = map(int, input().split())  # n is  length of array and k is the min length of the contiguous sub array
    a = [int(i) for i in input().split()]  # array given
    left = 1
    right = n + 1 # 1 ≤ left ≤ right ≤ n
    while right - left > 1:  # while there are still elements to look at in binary search
        mid = left + (right - left) // 2  # possible median, since (1 ≤ a𝑖 ≤ n)

        b = [-1] * n  # create an array that marks whether the element is greater or lesser than the mid
        for i in range(n):
            if a[i] >= mid:
                b[i] = 1

        # calculate if the sum up until that point can be greater than 0, which means that mid can be the max median
        for i in range(1, len(b)):
            b[i] += b[i - 1]

        ans = False  # flag to search for the res element
        if b[k - 1] > 0:  # if the element at position k is greater than 0, that means mid is a potential median
            ans = True

        my_min = 0
        for i in range(k, len(b)):  # check all possible options that have k as min length
            my_min = min(my_min, b[i - k])
            if b[i] - my_min > 0:
                ans = True

        # binary search
        if ans:
            left = mid
        else:
            right = mid
    # return left
    print(left)
