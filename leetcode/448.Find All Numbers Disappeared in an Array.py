# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elemen
# ts appear twice and others appear once. 
# 
#  Find all the elements of [1, n] inclusive that do not appear in this array. 
# 
#  Could you do it without extra space and in O(n) runtime? You may assume the r
# eturned list does not count as extra space. 
# 
#  Example:
#  
# Input:
# [4,3,2,7,8,2,3,1]
# 
# Output:
# [5,6]
#  
#  Related Topics Array 
#  👍 2896 👎 248


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findDisappearedNumbers(self, nums):
        lens = len(nums)
        m = [x for x in range(1, lens+1)]
        return list(set(m)-set(nums))


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    n = [2,2]
    print(Solution().findDisappearedNumbers(n))
