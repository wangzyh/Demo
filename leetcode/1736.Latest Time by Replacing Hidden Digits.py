# You are given a string time in the form of hh:mm, where some of the digits in 
# the string are hidden (represented by ?). 
# 
#  The valid times are those inclusively between 00:00 and 23:59. 
# 
#  Return the latest valid time you can get from time by replacing the hidden di
# gits. 
# 
#  
#  Example 1: 
# 
#  
# Input: time = "2?:?0"
# Output: "23:50"
# Explanation: The latest hour beginning with the digit '2' is 23 and the latest
#  minute ending with the digit '0' is 50.
#  
# 
#  Example 2: 
# 
#  
# Input: time = "0?:3?"
# Output: "09:39"
#  
# 
#  Example 3: 
# 
#  
# Input: time = "1?:22"
# Output: "19:22"
#  
# 
#  
#  Constraints: 
# 
#  
#  time is in the format hh:mm. 
#  It is guaranteed that you can produce a valid time from the given string. 
#  
#  Related Topics String Greedy 
#  👍 47 👎 26

# region data
# 2021-01-26 16:43:36
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maximumTime(self, time: str) -> str:
        res = ['', '', ':', '', '']
        h, m = time.split(':')

        if h[0] == '?':
            res[0] = '2' if h[1] == '?' or int(h[1]) < 4 else '1'
            res[1] = h[1] if h[1] != '?' else '3'
        else:
            res[0] = h[0]
        if h[1] == '?':
            if int(res[0]) < 2:
                res[1] = '9'
            else:
                res[1] = '3'
        else:
            res[1] = h[1]

        res[3] = '5' if m[0] == '?' else m[0]
        res[4] = '9' if m[1] == '?' else m[1]

        return ''.join(res)


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = "00:01"
    print(Solution().maximumTime(n))
