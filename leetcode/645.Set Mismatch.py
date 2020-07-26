# 
# The set S originally contains numbers from 1 to n. But unfortunately, due to t
# he data error, one of the numbers in the set got duplicated to another number in
#  the set, which results in repetition of one number and loss of another number. 
# 
#  
# 
#  
# Given an array nums representing the data status of this set after the error. 
# Your task is to firstly find the number occurs twice and then find the number th
# at is missing. Return them in the form of an array.
#  
# 
# 
#  Example 1: 
#  
# Input: nums = [1,2,2,4]
# Output: [2,3]
#  
#  
# 
#  Note: 
#  
#  The given array size will in the range [2, 10000]. 
#  The given array's numbers won't have any order. 
#  
#  Related Topics Hash Table Math 
#  👍 666 👎 302

# 2020-07-25 00:18:41

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findErrorNums(self, nums):
        from collections import Counter
        d = dict(Counter(nums))
        key = [key for key, value in d.items() if value==2]
        lens = len(nums)
        m = set(range(1, lens+1))
        res = list(m - set(nums))

        return key+res

        
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = [1,1]
    print(Solution().findErrorNums(n))
