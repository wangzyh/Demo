# 628. Maximum Product of Three Numbers
# 2020/7/17


def main(nums):
    res = 1

    nums.sort()
    for i in range(-1, -4, -1):
        res *= nums[i]

    return res


if __name__ == '__main__':
    nums = [-4, -3, -2, -1, 60]
    a = main(nums)
    print(a)
