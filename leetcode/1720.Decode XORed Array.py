# There is a hidden integer array arr that consists of n non-negative integers. 
# 
# 
#  It was encoded into another integer array encoded of length n - 1, such that 
# encoded[i] = arr[i] XOR arr[i + 1]. For example, if arr = [1,0,2,1], then encode
# d = [1,2,3]. 
# 
#  You are given the encoded array. You are also given an integer first, that is
#  the first element of arr, i.e. arr[0]. 
# 
#  Return the original array arr. It can be proved that the answer exists and is
#  unique. 
# 
#  
#  Example 1: 
# 
#  
# Input: encoded = [1,2,3], first = 1
# Output: [1,0,2,1]
# Explanation: If arr = [1,0,2,1], then first = 1 and encoded = [1 XOR 0, 0 XOR 
# 2, 2 XOR 1] = [1,2,3]
#  
# 
#  Example 2: 
# 
#  
# Input: encoded = [6,2,7,3], first = 4
# Output: [4,2,0,7,4]
#  
# 
#  
#  Constraints: 
# 
#  
#  2 <= n <= 104 
#  encoded.length == n - 1 
#  0 <= encoded[i] <= 105 
#  0 <= first <= 105 
#  
#  Related Topics Bit Manipulation 
#  👍 173 👎 30

# region time
# 2021-03-11 23:12:47
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        res = [first]
        for i in encoded:
            res.append(i ^ res[-1])
        return res


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    nencoded = [6, 2, 7, 3]
    first = 4
    print(Solution().decode(nencoded, first))
