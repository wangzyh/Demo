nums = [1, 3, 4, 5, 6, 1, 4]


# 递归 时间复杂度O(2**n)
def rec_opt(n, i):
    if i == 0:
        return n[0]
    elif i == 1:
        return max(n[0], n[1])
    else:
        a = rec_opt(n, i - 2) + n[i]
        b = rec_opt(n, i - 1)
        return max(a, b)


print(rec_opt(nums, len(nums) - 1))


def dp_opt(n):
    dp = [0 for _ in range(len(n))]
    dp[0] = n[0]
    dp[1] = max(n[0], n[1])
    for i in range(2, len(n)):
        a = dp[i - 2] + n[i]
        b = dp[i - 1]
        dp[i] = max(a, b)
    return dp[-1]


print(dp_opt(nums))
