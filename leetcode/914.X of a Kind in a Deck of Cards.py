# In a deck of cards, each card has an integer written on it. 
# 
#  Return true if and only if you can choose X >= 2 such that it is possible to 
# split the entire deck into 1 or more groups of cards, where: 
# 
#  
#  Each group has exactly X cards. 
#  All the cards in each group have the same integer. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: deck = [1,2,3,4,4,3,2,1]
# Output: true
# Explanation: Possible partition [1,1],[2,2],[3,3],[4,4].
#  
# 
#  Example 2: 
# 
#  
# Input: deck = [1,1,1,2,2,2,3,3]
# Output: false´
# Explanation: No possible partition.
#  
# 
#  Example 3: 
# 
#  
# Input: deck = [1]
# Output: false
# Explanation: No possible partition.
#  
# 
#  Example 4: 
# 
#  
# Input: deck = [1,1]
# Output: true
# Explanation: Possible partition [1,1].
#  
# 
#  Example 5: 
# 
#  
# Input: deck = [1,1,2,2,2,2]
# Output: true
# Explanation: Possible partition [1,1],[2,2],[2,2].
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= deck.length <= 10^4 
#  0 <= deck[i] < 10^4 
#  
#  Related Topics Array Math 
#  👍 712 👎 177

# region data
# 2021-01-07 14:57:25
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def hasGroupsSizeX(self, deck) -> bool:
        from math import gcd
        from functools import reduce

        from collections import Counter
        dic = dict(Counter(deck))
        return True if reduce(gcd, dic.values()) >= 2 else False


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    # n = [1, 2, 3, 4, 4, 3, 2, 2, 2, 1]
    n = [1]
    # n = [1, 1, 1, 1, 2, 2, 2, 2, 2, 2]
    print(Solution().hasGroupsSizeX(n))
