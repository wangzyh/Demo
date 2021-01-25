# Write a program to count the number of days between two dates. 
# 
#  The two dates are given as strings, their format is YYYY-MM-DD as shown in th
# e examples. 
# 
#  
#  Example 1: 
#  Input: date1 = "2019-06-29", date2 = "2019-06-30"
# Output: 1
#  Example 2: 
#  Input: date1 = "2020-01-15", date2 = "2019-12-31"
# Output: 15
#  
#  
#  Constraints: 
# 
#  
#  The given dates are valid dates between the years 1971 and 2100. 
#  
#  👍 84 👎 478

# region data
# 2021-01-25 14:50:28
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        years = [1704, 1708, 1712, 1716, 1720, 1724, 1728, 1732, 1736, 1740, 1744, 1748, 1752, 1756, 1760, 1764, 1768,
                 1772, 1776, 1780, 1784, 1788, 1792, 1796, 1804, 1808, 1812, 1816, 1820, 1824, 1828, 1832, 1836, 1840,
                 1844, 1848, 1852, 1856, 1860, 1864, 1868, 1872, 1876, 1880, 1884, 1888, 1892, 1896, 1904, 1908, 1912,
                 1916, 1920, 1924, 1928, 1932, 1936, 1940, 1944, 1948, 1952, 1956, 1960, 1964, 1968, 1972, 1976, 1980,
                 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020, 2024, 2028, 2032, 2036, 2040, 2044, 2048,
                 2052, 2056, 2060, 2064, 2068, 2072, 2076, 2080, 2084, 2088, 2092, 2096]

        def dayOfYear(date: str):
            year, month, day = [int(i) for i in date.split('-')]
            leap_year = 29 if year in years else 28
            dic = {1: 31, 2: leap_year, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31,
                   11: 30, 12: 30}
            day = day
            for i in range(1, month):
                day += dic[i]
            return day, year

        d1 = dayOfYear(date1)
        d2 = dayOfYear(date2)
        y = 0
        if d1[1] > d2[1]:
            for i in range(d2[1], d1[1]):
                if i in years:
                    y += 1
            return d1[0] + (d1[1] - d2[1]) * 365 - d2[0] + y
        else:
            for i in range(d1[1], d2[1]):
                if i in years:
                    y += 1
            return abs(d2[0] + (d2[1] - d1[1]) * 365 - d1[0]) + y


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    date1 = "1971-06-29"
    date2 = "2010-09-23"
    print(Solution().daysBetweenDates(date1, date2))
