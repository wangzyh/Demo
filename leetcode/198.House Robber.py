# You are a professional robber planning to rob houses along a street. Each hous
# e has a certain amount of money stashed, the only constraint stopping you from r
# obbing each of them is that adjacent houses have security system connected and i
# t will automatically contact the police if two adjacent houses were broken into 
# on the same night. 
# 
#  Given a list of non-negative integers representing the amount of money of eac
# h house, determine the maximum amount of money you can rob tonight without alert
# ing the police. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
#              Total amount you can rob = 1 + 3 = 4.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 
# (money = 1).
#              Total amount you can rob = 2 + 9 + 1 = 12.
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= nums.length <= 100 
#  0 <= nums[i] <= 400 
#  
#  Related Topics Dynamic Programming 
#  👍 4924 👎 151

# region time
# 2020-07-29 22:34:55
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def rob(self, nums) -> int:
        if len(nums) <= 1:
            return 0 if nums == [] else nums[1]
        first = nums[0]
        two = nums[1]
        lens = len(nums)
        temp_f = 0
        temp_t = 0

        for i in range(2, lens, 1):
            for j in range(i + 2, lens, 1):
                if i + 1 >= lens:
                    temp_f = nums[i]
                elif i + 2 >= lens:
                    temp_f += nums[i]
                    temp_t += nums[i+1]
                elif i + 3 >= lens:
                    temp_f += (nums[i] + nums[i+2])
                    temp_t += nums[i + 1]
                elif i + 4 >= lens:
                    temp_f += (nums[i] + nums[i+2])
                    temp_t += (nums[i +1] + nums[i+3])
                if temp_f > temp_t:

                if nums[i] + nums[i+2] > (nums[i +1] + nums[i+3]):
                    temp_f = temp_f + nums[i] + nums[i+2]
                else:
                    temp_f = temp_f + nums[i +1] + nums[i+3]
                elif i +2
                temp_f += nums[i]
        print(temp_f)



# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    # n = [2,7,9,3,1]
    n = [2, 3, 4, 32, 36, 34, 5, 15, 24, 5]
    # 2, 32, 34, 24
    # 3, 32, 34, 24
    print(Solution().rob(n))
