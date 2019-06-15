def main(nums, k):
    k = len(nums) - k
    head = nums[:k]
    for x in head:
        nums.remove(x)
        nums.append(x)


if __name__ == '__main__':
    a = main([1, 2, 3, 4, 5, 6, 7], k=3)
    print(a)
