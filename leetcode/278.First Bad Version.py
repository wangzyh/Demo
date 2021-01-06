# You are a product manager and currently leading a team to develop a new produc
# t. Unfortunately, the latest version of your product fails the quality check. Si
# nce each version is developed based on the previous version, all the versions af
# ter a bad version are also bad. 
# 
#  Suppose you have n versions [1, 2, ..., n] and you want to find out the first
#  bad one, which causes all the following ones to be bad. 
# 
#  You are given an API bool isBadVersion(version) which returns whether version
#  is bad. Implement a function to find the first bad version. You should minimize
#  the number of calls to the API. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 5, bad = 4
# Output: 4
# Explanation:
# call isBadVersion(3) -> false
# call isBadVersion(5) -> true
# call isBadVersion(4) -> true
# Then 4 is the first bad version.
#  
# 
#  Example 2: 
# 
#  
# Input: n = 1, bad = 1
# Output: 1
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= bad <= n <= 231 - 1 
#  
#  Related Topics Binary Search 
#  👍 1858 👎 774

# region time
# 2021-01-04 19:31:23
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

def isBadVersion(num):
    return bad <= num


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # bads = []
        # num = n // 2 if n // 2 != 0 else 1
        # while num and num <= n:
        #     print(1111)
        #     if isBadVersion(num):
        #         bads.append(num)
        #         if num // 2 != 0:
        #             num //= 2
        #         else:
        #             return num
        #     else:
        #         if num + 1 in bads:
        #             return num + 1
        #         pick = bads[-1] if bads else n
        #         num += ((pick - num) // 2) if (pick - num) // 2 != 0 else 1
        l = 1
        r = n
        while l <= r:
            mid = (l + r) // 2
            if isBadVersion(mid) == False:
                l = mid + 1
            else:
                r = mid - 1
        return l

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = 400
    bad = 5
    print(Solution().firstBadVersion(n))
