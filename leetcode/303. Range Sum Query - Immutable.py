# 303. Range Sum Query - Immutable
# 2020/7/7


class NumArray:

    def __init__(self, nums):
        self._sum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self._sum[i + 1] = self._sum[i] + nums[i]

    def sumRange(self, i: int, j: int) -> int:
        return self._sum[j+1] - self._sum[i]


if __name__ == '__main__':
    nums = [-2, 0, 3, -5, 2, -1]
    a = NumArray(nums)
    print(a.sumRange(0, 2))
    print(a.sumRange(2, 5))
    print(a.sumRange(0, 5))

