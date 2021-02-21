# Given an integer n. Each number from 1 to n is grouped according to the sum of
#  its digits. 
# 
#  Return how many groups have the largest size. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 13
# Output: 4
# Explanation: There are 9 groups in total, they are grouped according sum of it
# s digits of numbers from 1 to 13:
# [1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9]. There are 4 groups wi
# th largest size.
#  
# 
#  Example 2: 
# 
#  
# Input: n = 2
# Output: 2
# Explanation: There are 2 groups [1], [2] of size 1.
#  
# 
#  Example 3: 
# 
#  
# Input: n = 15
# Output: 6
#  
# 
#  Example 4: 
# 
#  
# Input: n = 24
# Output: 5
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 10^4 
#  
#  Related Topics Array 
#  👍 163 👎 417

# region time
# 2021-02-20 22:53:42
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countLargestGroup(self, n: int) -> int:
        res = []
        for i in range(1, n + 1):
            c = i
            sum = 0
            while i != 0:
                sum += i % 10
                i //= 10
            if len(res) < sum:
                res.insert(sum - 1, [c, ])
                continue
            res[sum - 1].append(c)
        res.sort(key=lambda x: len(x), reverse=True)

        max_len = 1
        for i in res[1:]:
            if len(i) < len(res[0]):
                break
            max_len += 1
        return max_len


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = 24
    print(Solution().countLargestGroup(n))
