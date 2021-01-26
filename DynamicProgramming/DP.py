# Problem: Find the sum of the first N numbers.
# Objective function: f(i) is the sum of the first i elements.
# Recurrence relation: f(n) = f(n-1) + n
def summatory(n):
    # We add the one so we can consider the 0
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i - 1] + i
    return dp.pop()


summatory(3)


# Problem: In how many different ways can we climb the stair, we can either climb one or two steps at a time.
# Objective function: f(i) is the number of ways to reach to a stair.
# Recurrence relation: f(n) = f(n-1) + f(n-2)
# Both O(n) time and space complexity
def climb_stairs1(n):
    # Add one because of the zero
    # return helper_cs1(0, n, dp)
    # Second option: iterative way
    a = 1
    b = 1
    for i in range(2, n + 1):
        # c = a + b
        c = a + b
        a = b
        b = c
    return c


def helper_cs1(curr, n, dp):
    if curr > n:
        return 0
    if dp[curr]:
        return dp[curr]
    if curr == n:
        if not dp[curr]:
            dp[curr] = 1
        else:
            dp[curr] += 1
        return 1
    return helper_cs1(curr + 1, n, dp) + helper_cs1(curr + 2, n, dp)


climb_stairs1(3)


# Same problem, but with the possibility of climbing 3 stairs
def climb_stairs3(n):
    a = 1
    b = 1
    c = 2
    for i in range(3, n + 1):
        # d = a + b + c
        d = a + b + c
        a = b
        b = c
        c = d
    return d


climb_stairs3(4)


# Problem: In how many different ways can we climb the stair, k determines how many steps can we take.
# Objective function: f(i) is the number of ways to reach to a stair, in k ways.
# Base cases:
# Recurrence relation: f(n) = f(n-1) + f(n-2) + ... + f(n-k)
# Order of execution: Bottom-up
# Where to look for the answer? f(n)
# Time complexity O(nk), space complexity O(k)
def climb_stairs_k(n, k):
    dp = [0] * k
    dp[0] = 1
    for i in range(1, n + 1):
        # Apply the recurrence relation
        for j in range(1, k):
            if i - j < 0:
                continue
            dp[i % k] += dp[(i - j) % k]
    return dp[n % k]


climb_stairs_k(4, 3)


# Problem: In how many different ways can we climb the stair.
# K determines how many steps can we take. We cant step on red steps.
# Objective function: f(i) is the number of ways to reach to a stair, in k ways.
# Base cases:
# Recurrence relation: f(n) = f(n-1) + f(n-2) + ... + f(n-k)
# Order of execution: Bottom-up
# Where to look for the answer? f(n)
# Time complexity O(nk), space complexity O(k)

def climb_stairs_k_red(n, k, red_steps):
    dp = [0] * k
    dp[0] = 1
    for i in range(1, n + 1):
        # Apply the recurrence relation
        for j in range(1, k):
            if i - j < 0:
                # continue ignores next statements
                continue
            # Check if current step is in non-valid steps
            if i - 1 in red_steps:
                dp[i % k] = 0
            else:
                dp[i % k] += dp[(i - j) % k]
    return dp[n % k]


# print(climb_stairs_k_red(7, 3, [1, 3, 4]))

# Problem: Paid stair case, extension of k steps, but we add prices
# to each step, so let's compute the min price to get to the top.
# UPDATE: We want to return the path if followed, which should be the cheapes.
# 1. Objective function: f(i) -> min cost to the ith step
# 2. Base cases: f(0) = 0, f(1) = 3, f(2) = 2
# 3. Recurrence relation: F(n) = P(n) + min(F(n - 1), F(n - 2))
# 4. Order of execution: Bottom-up
# 5. Where to look for the answer?: F(n)
# Time complexity O(n), space complexity O(k)

def paid_stairs(n, p):
    # every time we step on a new step, we need to save where we came from
    from_path = [0] * (n + 1)
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = p[1]
    for i in range(2, n+1):
        dp[i] = min(dp[i - 1], dp[i - 2]) + p[i]
        if dp[i - 1] < dp[i - 2]:
            from_path[i] = i - 1
        else:
            from_path[i] = i - 2

    ordered_path = []
    curr = n
    # reconstruct the path
    while curr > 0:
        ordered_path.append(curr)
        curr = from_path[curr]
    ordered_path.append(0)

    return my_reverse(ordered_path)

def my_reverse(my_list):
    i = 0
    j = len(my_list) - 1
    while i < j:
        aux = my_list[i]
        my_list[i] = my_list[j]
        my_list[j] = aux
        i += 1
        j -= 1
    return my_list

print(paid_stairs(8, [0, 3, 2, 4, 6, 1, 1, 5, 3]))