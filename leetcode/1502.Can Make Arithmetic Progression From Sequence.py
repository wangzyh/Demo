# Given an array of numbers arr. A sequence of numbers is called an arithmetic p
# rogression if the difference between any two consecutive elements is the same. 
# 
#  Return true if the array can be rearranged to form an arithmetic progression,
#  otherwise, return false. 
# 
#  
#  Example 1: 
# 
#  
# Input: arr = [3,5,1]
# Output: true
# Explanation: We can reorder the elements as [1,3,5] or [5,3,1] with difference
# s 2 and -2 respectively, between each consecutive elements.
#  
# 
#  Example 2: 
# 
#  
# Input: arr = [1,2,4]
# Output: false
# Explanation: There is no way to reorder the elements to obtain an arithmetic p
# rogression.
#  
# 
#  
#  Constraints: 
# 
#  
#  2 <= arr.length <= 1000 
#  -10^6 <= arr[i] <= 10^6 
#  
#  Related Topics Array Sort 
#  👍 264 👎 22

# region data
# 2021-01-25 12:24:01
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canMakeArithmeticProgression(self, arr) -> bool:
        arr = sorted(arr)
        a = [arr[i] - arr[i - 1] for i in range(1, len(arr))]
        return len(set(a)) == 1


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = [4, 2, 3]
    print(Solution().canMakeArithmeticProgression(n))
