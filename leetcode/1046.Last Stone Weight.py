# We have a collection of stones, each stone has a positive integer weight. 
# 
#  Each turn, we choose the two heaviest stones and smash them together. Suppose
#  the stones have weights x and y with x <= y. The result of this smash is: 
# 
#  
#  If x == y, both stones are totally destroyed; 
#  If x != y, the stone of weight x is totally destroyed, and the stone of weigh
# t y has new weight y-x. 
#  
# 
#  At the end, there is at most 1 stone left. Return the weight of this stone (o
# r 0 if there are no stones left.) 
# 
#  
# 
#  Example 1: 
# 
#  
# Input: [2,7,4,1,8,1]
# Output: 1
# Explanation: 
# We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
# we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
# we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
# we combine 1 and 1 to get 0 so the array converts to [1] then that's the value
#  of last stone. 
# 
#  
# 
#  Note: 
# 
#  
#  1 <= stones.length <= 30 
#  1 <= stones[i] <= 1000 
#  
#  Related Topics Heap Greedy 
#  👍 1258 👎 35

# region data
# 2021-03-16 15:30:53
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort(reverse=True)
        if len(stones) < 3:
            return stones[0] if len(stones) == 1 else stones[0] - stones[1]
        stones.append(stones.pop(0) - stones.pop(0))
        return self.lastStoneWeight(stones)


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = [2, 7, 4, 1, 8, 1]
    print(Solution().lastStoneWeight(n))
