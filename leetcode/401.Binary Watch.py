# A binary watch has 4 LEDs on the top which represent the hours (0-11), and the
#  6 LEDs on the bottom represent the minutes (0-59). 
#  Each LED represents a zero or one, with the least significant bit on the righ
# t. 
# 
#  For example, the above binary watch reads "3:25". 
# 
#  Given a non-negative integer n which represents the number of LEDs that are c
# urrently on, return all possible times the watch could represent. 
# 
#  Example:
#  Input: n = 1 Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04",
#  "0:08", "0:16", "0:32"] 
#  
# 
#  Note: 
#  
#  The order of output does not matter. 
#  The hour must not contain a leading zero, for example "01:00" is not valid, i
# t should be "1:00". 
#  The minute must be consist of two digits and may contain a leading zero, for 
# example "10:2" is not valid, it should be "10:02". 
#  
#  Related Topics Backtracking Bit Manipulation 
#  👍 569 👎 975


# leetcode submit region begin(Prohibit modification and deletion)
from itertools import combinations


class Solution:
    def readBinaryWatch(self, num: int):
        res = []
        a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        b_time = ['0' for _ in range(len(a))]
        times = list(combinations(a, num))
        for t in times:
            for i in t:
                b_time[i] = '1'
            b_hours = int(''.join(b_time[:4]), 2)
            b_min = int(''.join(b_time[4:]), 2)

            if b_hours >= 12 or (b_min >= 60):
                b_time = ['0' for _ in range(len(a))]
                continue
            time = f'{b_hours}:{b_min if len(str(b_min)) > 1 else "0" + str(b_min)}'
            res.append(time)
            b_time = ['0' for _ in range(len(a))]

        return res


# ["0:03","0:05","0:06","0:09","0:10","0:12","0:17","0:18","0:20","0:24","0:33","0:34","0:36","0:40","0:48","1:01","1:02","1:04","1:08","1:16","1:32","2:01","2:02","2:04","2:08","2:16","2:32","3:00","4:01","4:02","4:04","4:08","4:16","4:32","5:00","6:00","8:01","8:02","8:04","8:08","8:16","8:32","9:00","10:00"]
# ["12:00","10:00","9:00","8:32","8:16","8:08","8:04","8:02","8:01","6:00","5:00","4:32","4:16","4:08","4:04","4:02","4:01","3:00","2:32","2:16","2:08","2:04","2:02","2:01","1:32","1:16","1:08","1:04","1:02","1:01","0:48","0:40","0:36","0:34","0:33","0:24","0:20","0:18","0:17","0:12","0:10","0:09","0:06","0:05","0:03"]
# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    n = 4
    print(Solution().readBinaryWatch(n))
