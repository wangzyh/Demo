# 
# You are given two arrays (without duplicates) nums1 and nums2 where nums1’s el
# ements are subset of nums2. Find all the next greater numbers for nums1's elemen
# ts in the corresponding places of nums2. 
#  
# 
#  
# The Next Greater Number of a number x in nums1 is the first greater number to 
# its right in nums2. If it does not exist, output -1 for this number.
#  
# 
#  Example 1: 
#  
# Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
# Output: [-1,3,-1]
# Explanation:
#     For number 4 in the first array, you cannot find the next greater number f
# or it in the second array, so output -1.
#     For number 1 in the first array, the next greater number for it in the sec
# ond array is 3.
#     For number 2 in the first array, there is no next greater number for it in
#  the second array, so output -1.
#  
#  
# 
#  Example 2: 
#  
# Input: nums1 = [2,4], nums2 = [1,2,3,4].
# Output: [3,-1]
# Explanation:
#     For number 2 in the first array, the next greater number for it in the sec
# ond array is 3.
#     For number 4 in the first array, there is no next greater number for it in
#  the second array, so output -1.
#  
#  
# 
# 
#  Note: 
#  
#  All elements in nums1 and nums2 are unique. 
#  The length of both nums1 and nums2 would not exceed 1000. 
#  
#  Related Topics Stack 
#  👍 2091 👎 2592

# region data
# 2021-01-04 16:44:30
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def nextGreaterElement(self, nums1, nums2):
        # res = []
        # point = 0
        # for i in nums1:
        #     if nums2.index(i) + 1 < len(nums2):
        #         for j in nums2[nums2.index(i)+1:]:
        #             if j > i:
        #                 res.append(j)
        #                 point = 1
        #                 break
        #         if point:
        #             point = 0
        #             continue
        #         res.append(-1)
        #
        #     else:
        #         res.append(-1)
        # return res
        d1 = {}
        ans = []
        stack = []

        for num in nums2:
            while stack and num > stack[-1]:
                d1[stack.pop()] = num
            stack.append(num)

        for num in nums1:
            ans.append(d1.get(num, -1))

        return ans
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    nums1 = [4,6,2]
    nums2 = [5,6,3,4,7]
    print(Solution().nextGreaterElement(nums1, nums2))