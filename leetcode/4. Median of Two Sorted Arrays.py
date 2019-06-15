def main(nums1, nums2):
    nums = nums1 + nums2
    nums.sort()
    median = len(nums) % 2 and nums[int(len(nums)/2)] or (nums[int(len(nums)/2)-1] + nums[int(len(nums)/2)])/2
    return float(median)


if __name__ == '__main__':
    a = main(nums1 = [1, 3], nums2 = [2, 4])
    print(a)
