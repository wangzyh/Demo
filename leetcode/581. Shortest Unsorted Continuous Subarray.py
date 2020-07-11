# 581. Shortest Unsorted Continuous Subarray
# 2020/7/11


def main(nums):
    s_nums = sorted(nums)
    start = 0
    end = -1

    for i in range(len(nums)):
        if nums[i] != s_nums[i]:
            start = i
            for j in range(len(nums)-1, i, -1):
                if nums[j] != s_nums[j]:
                    end = j
                    break
            break
    return end-start+1


if __name__ == '__main__':
    a = main([2, 6, 4, 8, 10, 9, 15])
    # c = main([1,2,3,4])
    # b = main([2, 3, 43, 54, 2, 3, 4, 5, 6, 2, 2, 1, 2, 4, 4, 5, 26, 5, 5])
    print(a)
    # print(b)
    # print(c)