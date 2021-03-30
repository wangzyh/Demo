# 快排 时间复杂度：O(nlog₂n) 空间复杂度：O(nlog₂n) 稳定性：不稳定
def quick_sort(nums):
    if not nums:
        return []
    else:
        node = nums[0]
        ll = quick_sort([i for i in nums[1:] if i < node])
        rl = quick_sort([i for i in nums[1:] if i >= node])
        return ll + [node] + rl


# 冒泡排序 时间复杂度：O(n²) 空间复杂度：O(1) 稳定性：稳定
def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums




if __name__ == '__main__':
    nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(quick_sort(nums))
