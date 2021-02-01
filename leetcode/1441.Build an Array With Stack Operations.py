# Given an array target and an integer n. In each iteration, you will read a num
# ber from list = {1,2,3..., n}. 
# 
#  Build the target array using the following operations: 
# 
#  
#  Push: Read a new element from the beginning list, and push it in the array. 
#  Pop: delete the last element of the array. 
#  If the target array is already built, stop reading more elements. 
#  
# 
#  Return the operations to build the target array. You are guaranteed that the 
# answer is unique. 
# 
#  
#  Example 1: 
# 
#  
# Input: target = [1,3], n = 3
# Output: ["Push","Push","Pop","Push"]
# Explanation: 
# Read number 1 and automatically push in the array -> [1]
# Read number 2 and automatically push in the array then Pop it -> [1]
# Read number 3 and automatically push in the array -> [1,3]
#  
# 
#  Example 2: 
# 
#  
# Input: target = [1,2,3], n = 3
# Output: ["Push","Push","Push"]
#  
# 
#  Example 3: 
# 
#  
# Input: target = [1,2], n = 4
# Output: ["Push","Push"]
# Explanation: You only need to read the first 2 numbers and stop.
#  
# 
#  Example 4: 
# 
#  
# Input: target = [2,3,4], n = 4
# Output: ["Push","Pop","Push","Push","Push"]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= target.length <= 100 
#  1 <= target[i] <= n 
#  1 <= n <= 100 
#  target is strictly increasing. 
#  
#  Related Topics Stack 
#  👍 226 👎 376

# region data
# 2021-01-26 14:52:51
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def buildArray(self, target, n: int):
        res = ['Push'] * target[-1]
        diff = sorted(set([i for i in range(1, target[-1] + 1)]) - set(target))
        n = 0
        for i in diff:
            res.insert(i + n, 'Pop')
            n += 1
        return res


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    target = [1, 2, 4, 5, 6, 9, 10, 11, 13, 14, 15, 16]
    n = 16
    print(Solution().buildArray(target, n))
