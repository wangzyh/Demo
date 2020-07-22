# 628. Maximum Product of Three Numbers
# 2020/7/17


def main(nums):
    nums.sort()
    top = nums[0] * nums[1]
    end = nums[-2]*nums[-3]
    if top > end:
        return top*nums[-1]
    return nums[-1]*end


if __name__ == '__main__':
    nums = [-4, -3, -2, -1, 60]
    a = main(nums)
    print(a)
