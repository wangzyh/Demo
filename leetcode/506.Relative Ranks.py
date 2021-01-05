# 
# Given scores of N athletes, find their relative ranks and the people with the 
# top three highest scores, who will be awarded medals: "Gold Medal", "Silver Meda
# l" and "Bronze Medal". 
# 
#  Example 1: 
#  
# Input: [5, 4, 3, 2, 1]
# Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
# Explanation: The first three athletes got the top three highest scores, so the
# y got "Gold Medal", "Silver Medal" and "Bronze Medal". For the left two athletes
# , you just need to output their relative ranks according to their scores.
#  
#  
# 
#  Note: 
#  
#  N is a positive integer and won't exceed 10,000. 
#  All the scores of athletes are guaranteed to be unique. 
#  
#  
#  👍 302 👎 598

# region data
# 2021-01-05 10:38:31
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findRelativeRanks(self, nums):
        top = ("Gold Medal", "Silver Medal", "Bronze Medal")
        res = ['' for _ in range(len(nums))]
        sort_nums = sorted(list(enumerate(nums)), key=lambda x: x[1], reverse=True)
        lens = len(sort_nums)
        for i in range(lens):
            if i < 3:
                res[sort_nums[i][0]] = top[i]
            else:
                res[sort_nums[i][0]] = str(i+1)
        return res


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = [1, 4, 9, 5, 6, 7, 8, 3, 3]
    # ["9","6","Gold Medal","5","4","Bronze Medal","Silver Medal","7","8"]
    print(Solution().findRelativeRanks(n))
