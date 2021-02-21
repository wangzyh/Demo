# Given a date, return the corresponding day of the week for that date. 
# 
#  The input is given as three integers representing the day, month and year res
# pectively. 
# 
#  Return the answer as one of the following values {"Sunday", "Monday", "Tuesda
# y", "Wednesday", "Thursday", "Friday", "Saturday"}. 
# 
#  
#  Example 1: 
# 
#  
# Input: day = 31, month = 8, year = 2019
# Output: "Saturday"
#  
# 
#  Example 2: 
# 
#  
# Input: day = 18, month = 7, year = 1999
# Output: "Sunday"
#  
# 
#  Example 3: 
# 
#  
# Input: day = 15, month = 8, year = 1993
# Output: "Sunday"
#  
# 
#  
#  Constraints: 
# 
#  
#  The given dates are valid dates between the years 1971 and 2100. 
#  
#  Related Topics Array 
#  👍 152 👎 1385

# region time
# 2021-02-21 14:16:02
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        from datetime import date
        d = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        # year_one, year_two = int(str(year)[:2]), int(str(year)[2:])
        # d = ['Sunday', "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        # if month == 1 or month == 2:
        #     return d[(year_two - 1 + (year_two - 1) // 4 + year_one // 4 - 2 * year_one + 26 * (
        #             month + 12 + 1) // 10 + day - 1) % 7]
        # return d[(year_two + year_two // 4 + year_one // 4 - 2 * year_one + 26 * (month + 1) // 10 + day - 1) % 7]
        day = date(year, month, day).weekday()
        return d[day]


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    day = 6
    month = 3
    year = 1995
    print(Solution().dayOfTheWeek(day, month, year))
