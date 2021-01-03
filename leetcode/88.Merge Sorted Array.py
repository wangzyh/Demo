# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one
#  sorted array. 
# 
#  Note: 
# 
#  
#  The number of elements initialized in nums1 and nums2 are m and n respectivel
# y. 
#  You may assume that nums1 has enough space (size that is equal to m + n) to h
# old additional elements from nums2. 
#  
# 
#  Example: 
# 
#  
# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
# 
# Output: [1,2,2,3,5,6]
#  
# 
#  
#  Constraints: 
# 
#  
#  -10^9 <= nums1[i], nums2[i] <= 10^9 
#  nums1.length == m + n 
#  nums2.length == n 
#  
#  Related Topics Array Two Pointers 
#  👍 3041 👎 4746

# region data
# 2020-12-31 12:20:53
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(len(nums1)-m):
            nums1.pop(-1)
        nums1 += nums2
        nums1.sort()
    # leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    print(Solution().merge(nums1, m, nums2, n))
