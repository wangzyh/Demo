# The Hamming distance between two integers is the number of positions at which 
# the corresponding bits are different. 
# 
#  Given two integers x and y, calculate the Hamming distance. 
# 
#  Note: 
# 0 ≤ x, y < 231.
#  
# 
#  Example:
#  
# Input: x = 1, y = 4
# 
# Output: 2
# 
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑
# 
# The above arrows point to positions where the corresponding bits are different
# .
#  
#  Related Topics Bit Manipulation 
#  👍 1883 👎 162

# region data
# 2020-08-17 11:05:16
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')
        
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    x = 1
    y = 4
    print(Solution().hammingDistance(x, y))