# Given a positive integer, check whether it has alternating bits: namely, if tw
# o adjacent bits will always have different values. 
# 
#  Example 1: 
#  
# Input: 5
# Output: True
# Explanation:
# The binary representation of 5 is: 101
#  
#  
# 
#  Example 2: 
#  
# Input: 7
# Output: False
# Explanation:
# The binary representation of 7 is: 111.
#  
#  
# 
#  Example 3: 
#  
# Input: 11
# Output: False
# Explanation:
# The binary representation of 11 is: 1011.
#  
#  
# 
#  Example 4: 
#  
# Input: 10
# Output: True
# Explanation:
# The binary representation of 10 is: 1010.
#  
#  Related Topics Bit Manipulation 
#  👍 453 👎 78

# region time
# 2020-07-28 23:56:34
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        # s = str(bin(n)).split('b')[1]
        # x = 0
        # for i in s:
        #     if not x:
        #         x = int(i)+1
        #         continue
        #     if x == int(i)+1:
        #         return False
        #     if x != int(i)+1:
        #         x = int(i)+1
        # return True
        n = bin(n)[2:]
        for i in range(1, len(n)):
            if n[i - 1] == n[i]:
                return False
        return True


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = 42
    print(Solution().hasAlternatingBits(n))
