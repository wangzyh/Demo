# Given the array candies and the integer extraCandies, where candies[i] represe
# nts the number of candies that the ith kid has. 
# 
#  For each kid check if there is a way to distribute extraCandies among the kid
# s such that he or she can have the greatest number of candies among them. Notice
#  that multiple kids can have the greatest number of candies. 
# 
#  
#  Example 1: 
# 
#  
# Input: candies = [2,3,5,1,3], extraCandies = 3
# Output: [true,true,true,false,true] 
# Explanation: 
# Kid 1 has 2 candies and if he or she receives all extra candies (3) will have 
# 5 candies --- the greatest number of candies among the kids. 
# Kid 2 has 3 candies and if he or she receives at least 2 extra candies will ha
# ve the greatest number of candies among the kids. 
# Kid 3 has 5 candies and this is already the greatest number of candies among t
# he kids. 
# Kid 4 has 1 candy and even if he or she receives all extra candies will only h
# ave 4 candies. 
# Kid 5 has 3 candies and if he or she receives at least 2 extra candies will ha
# ve the greatest number of candies among the kids. 
#  
# 
#  Example 2: 
# 
#  
# Input: candies = [4,2,1,1,2], extraCandies = 1
# Output: [true,false,false,false,false] 
# Explanation: There is only 1 extra candy, therefore only kid 1 will have the g
# reatest number of candies among the kids regardless of who takes the extra candy
# .
#  
# 
#  Example 3: 
# 
#  
# Input: candies = [12,1,12], extraCandies = 10
# Output: [true,false,true]
#  
# 
#  
#  Constraints: 
# 
#  
#  2 <= candies.length <= 100 
#  1 <= candies[i] <= 100 
#  1 <= extraCandies <= 50 
#  Related Topics Array 
#  👍 277 👎 72

# region data
# 2020-07-29 14:07:25
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def kidsWithCandies(self, candies, extraCandies: int):
        gr = max(candies)
        return [x+extraCandies >= gr for x in candies]
        
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    candies = [2, 3, 5, 1, 3]
    extraCandies = 3
    print(Solution().kidsWithCandies(candies, extraCandies))
