# 26. Remove Duplicates from Sorted Array
# 2020/7/5


def main(nums):
    """
        from collections import Counter
        num = dict(Counter(nums))
        for i in num:
            if num[i] > 1:
                for j in range(num[i]-1):
                    nums.remove(i)

        return len(nums)
    """
    n = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[n] = nums[i]
            n += 1
    nums = nums[:n]
    return n


if __name__ == '__main__':
    a = main(nums=[1, 2, 3, 3, 3, 3, 4, 4, 4, 5, 6, 7, 7, 7, 12])
    print(a)
