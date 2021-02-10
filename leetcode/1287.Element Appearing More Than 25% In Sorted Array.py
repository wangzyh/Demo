# Given an integer array sorted in non-decreasing order, there is exactly one in
# teger in the array that occurs more than 25% of the time. 
# 
#  Return that integer. 
# 
#  
#  Example 1: 
#  Input: arr = [1,2,2,6,6,6,6,7,10]
# Output: 6
#  
#  
#  Constraints: 
# 
#  
#  1 <= arr.length <= 10^4 
#  0 <= arr[i] <= 10^5 
#  Related Topics Array 
#  👍 404 👎 28

# region time
# 2021-02-09 20:54:53
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        from collections import Counter
        d = dict(Counter(arr))
        for k, v in d.items():
            if v > len(arr) / 4:
                return k


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = [1, 2, 2, 6, 6, 6, 6, 7, 10]
    print(Solution().findSpecialInteger(n))
