# Given an integer array arr, return true if there are three consecutive odd num
# bers in the array. Otherwise, return false.
#  
#  Example 1: 
# 
#  
# Input: arr = [2,6,4,1]
# Output: false
# Explanation: There are no three consecutive odds.
#  
# 
#  Example 2: 
# 
#  
# Input: arr = [1,2,34,3,4,5,7,23,12]
# Output: true
# Explanation: [5,7,23] are three consecutive odds.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= arr.length <= 1000 
#  1 <= arr[i] <= 1000 
#  
#  Related Topics Array 
#  👍 187 👎 33

# region time
# 2021-03-08 20:16:45
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        # if len(arr) < 3:
        #     return False
        # arr = [i % 2 for i in arr]
        # arr = [[arr[i], arr[i + 1], arr[i + 2]] for i in range(len(arr) - 2)]
        # return [1, 1, 1] in arr
        counter = 0

        for i in arr:
            if i % 2 != 0:
                counter += 1
            else:
                counter = 0

            if counter == 3:
                return True

        return False


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = [1, 5, 23]
    print(Solution().threeConsecutiveOdds(n))
