# 
# A self-dividing number is a number that is divisible by every digit it contain
# s.
#  
# For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0,
#  and 128 % 8 == 0.
#  
# Also, a self-dividing number is not allowed to contain the digit zero.
#  
# Given a lower and upper number bound, output a list of every possible self div
# iding number, including the bounds if possible.
#  
#  Example 1: 
#  
# Input: 
# left = 1, right = 22
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
#  
#  
# 
#  Note:
#  The boundaries of each input argument are 1 <= left <= right <= 10000. 
#  Related Topics Math 
#  👍 788 👎 305

# region time
# 2021-01-18 23:58:58
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def selfDividingNumbers(self, left: int, right: int):
        res = []
        for i in range(left, right + 1):
            if '0' in str(i):
                continue
            n = [i if i % int(str(i)[j]) == 0 else 0 for j in range(len(str(i)))]
            if 0 not in n:
                res.append(n[0])
        return res


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    left = 1234
    right = 4512
    print(Solution().selfDividingNumbers(left, right))
