# 537. Complex Number Multiplication
# 2020/7/15


def main(nums):
    n_list = [nums[0]]
    lens = len(n_list)
    for i in nums[1:]:
        if i > n_list[-1] + 1:
            lens = max(lens, len(n_list))
            n_list = [i]
        else:
            n_list.append(i)
    return lens


if __name__ == '__main__':
    a = main([1, 3, 2, 2, 5, 2, 3, 7])
    print(a)
