# Given an integer num, return an array of the number of 1's in the binary repre
# sentation of every number in the range [0, num]. 
# 
#  
#  Example 1: 
# 
#  
# Input: num = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
#  
# 
#  Example 2: 
# 
#  
# Input: num = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= num <= 105 
#  
# 
#  
#  Follow up: 
# 
#  
#  It is very easy to come up with a solution with run time O(32n). Can you do i
# t in linear time O(n) and possibly in a single pass? 
#  Could you solve it in O(n) space complexity? 
#  Can you do it without using any built-in function (i.e., like __builtin_popco
# unt in C++)? 
#  
#  Related Topics Dynamic Programming Bit Manipulation 
#  👍 3715 👎 206

# region time
# 2021-03-28 22:36:40
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        # res = []
        # for i in range(num+1):
        #     res.append(bin(i).count('1'))
        # return res
        res = [0] * (num + 1)
        for i in range(num + 1):
            if i & 1:
                res[i] = res[i // 2] + 1
            else:
                res[i] = res[i // 2]
        return res


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = 10
    print(Solution().countBits(n))
