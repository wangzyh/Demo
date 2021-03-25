# region 1. 数字隔一个选一个，使结果最大 [1, 3, 4, 5, 6, 1, 4]
nums = [1, 3, 4, 5, 6, 1, 4]


# 最佳方案 递归 时间复杂度O(2**n)
def rec_opt(n, i):
    if i == 0:
        return n[0]
    elif i == 1:
        return max(n[0], n[1])
    else:
        a = rec_opt(n, i - 2) + n[i]
        b = rec_opt(n, i - 1)
        return max(a, b)


# 非递归
def dp_opt(n):
    dp = [0 for _ in range(len(n))]
    dp[0] = n[0]
    dp[1] = max(n[0], n[1])
    for i in range(2, len(n)):
        a = dp[i - 2] + n[i]
        b = dp[i - 1]
        dp[i] = max(a, b)
    return dp[-1]


# endregion

# region 2. 存在路径使和等于结果 [1, 3, 4, 5, 6, 1, 4] add = 13
# 递归
def rec_subset(nums, s):
    if s == 0:
        return True
    elif len(nums) == 1:
        return nums[0] == s
    elif nums[-1] > s:
        return rec_subset(nums[:-1], s)
    else:
        return bool(rec_subset(nums[:-1], s - nums[-1]) or rec_subset(nums[:-1], s))


def dp_subset(nums, s):
    dp = [[0 for _ in range(s)] for i in range(len(nums))]
    for i in dp:
        i[0] = True
    for i in range(s):
        dp[0][i] = False
    dp[0][nums[0]] = True
    for i in range(1, len(nums)):
        for ss in range(1, s):
            if nums[i] > ss:
                dp[i][ss] = dp[i - 1][ss]
            else:
                dp[i][ss] = dp[i - 1][ss - nums[i]] or dp[i - 1][ss]
    return dp[-1][-1]


# endregion

if __name__ == '__main__':
    # print(rec_opt(nums, len(nums) - 1))
    # print(dp_opt(nums))
    nums = [1, 3, 4, 5, 6, 1, 4]
    s = 9
    print(dp_subset(nums, s))
