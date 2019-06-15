def main(nums):
    result = []
    if not nums and len(nums) <= 3:
        return result

    for i in nums[1:]:

        res = - (nums[0] + i)

        if res in nums[1:] and sorted([nums[0], i, res]) not in result:
            result.append(sorted([nums[0], i, res]))
            nums[1:].remove(i)
            nums[1:].remove(res)

    main(nums[1:])

    return result


if __name__ == '__main__':
    a = main([-1, 0, 1, 2, -1, -4])
    print(a)
