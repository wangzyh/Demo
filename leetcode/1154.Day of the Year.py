# Given a string date representing a Gregorian calendar date formatted as YYYY-M
# M-DD, return the day number of the year. 
# 
#  
#  Example 1: 
# 
#  
# Input: date = "2019-01-09"
# Output: 9
# Explanation: Given date is the 9th day of the year in 2019.
#  
# 
#  Example 2: 
# 
#  
# Input: date = "2019-02-10"
# Output: 41
#  
# 
#  Example 3: 
# 
#  
# Input: date = "2003-03-01"
# Output: 60
#  
# 
#  Example 4: 
# 
#  
# Input: date = "2004-03-01"
# Output: 61
#  
# 
#  
#  Constraints: 
# 
#  
#  date.length == 10 
#  date[4] == date[7] == '-', and all other date[i]'s are digits 
#  date represents a calendar date between Jan 1st, 1900 and Dec 31, 2019. 
#  Related Topics Math 
#  👍 132 👎 193

# region time
# 2021-01-07 22:56:40
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def dayOfYear(self, date: str) -> int:
        year, month, day = date.split('-')
        leap_year = 29 if int(year) % 4 == 0 and int(year) % 100 != 0 or (int(year) % 400 == 0) else 28
        dic = {1: 31, 2: leap_year, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31,
               11: 30, 12: 30}
        day = int(day)
        for i in range(1, int(month)):
            day += dic[i]
        return day


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    # n = "2003-03-01"
    # n = "1900-03-25"
    n = "2004-03-01"
    print(Solution().dayOfYear(n))
