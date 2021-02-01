# We have two special characters. The first character can be represented by one 
# bit 0. The second character can be represented by two bits (10 or 11). 
# 
#  Now given a string represented by several bits. Return whether the last chara
# cter must be a one-bit character or not. The given string will always end with a
#  zero. 
# 
#  Example 1: 
#  
# Input: 
# bits = [1, 0, 0]
# Output: True
# Explanation: 
# The only way to decode it is two-bit character and one-bit character. So the l
# ast character is one-bit character.
#  
#  
# 
#  Example 2: 
#  
# Input: 
# bits = [1, 1, 1, 0]
# Output: False
# Explanation: 
# The only way to decode it is two-bit character and two-bit character. So the l
# ast character is NOT one-bit character.
#  
#  
# 
#  Note:
#  1 <= len(bits) <= 1000. 
#  bits[i] is always 0 or 1. 
#  Related Topics Array 
#  👍 518 👎 1294

# region data
# 2021-01-21 10:58:03
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isOneBitCharacter(self, bits) -> bool:
        n = 0
        while len(bits):
            if len(bits) == 1:
                return True
            if len(bits) == 2 and bits[0] == 0:
                return True
            if bits[n] == 1:
                bits.pop(0)
                bits.pop(0)
            else:
                bits.pop(0)
        return len(bits) == 1


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    # n = [0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0]
    n = [0, 0]
    print(Solution().isOneBitCharacter(n))
