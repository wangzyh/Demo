# Hercy wants to save money for his first car. He puts money in the Leetcode ban
# k every day. 
# 
#  He starts by putting in $1 on Monday, the first day. Every day from Tuesday t
# o Sunday, he will put in $1 more than the day before. On every subsequent Monday
# , he will put in $1 more than the previous Monday. 
# 
#  Given n, return the total amount of money he will have in the Leetcode bank a
# t the end of the nth day. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 4
# Output: 10
# Explanation: After the 4th day, the total is 1 + 2 + 3 + 4 = 10.
#  
# 
#  Example 2: 
# 
#  
# Input: n = 10
# Output: 37
# Explanation: After the 10th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2
#  + 3 + 4) = 37. Notice that on the 2nd Monday, Hercy only puts in $2.
#  
# 
#  Example 3: 
# 
#  
# Input: n = 20
# Output: 96
# Explanation: After the 20th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2
#  + 3 + 4 + 5 + 6 + 7 + 8) + (3 + 4 + 5 + 6 + 7 + 8) = 96.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 1000 
#  
#  Related Topics Math Greedy 
#  👍 90 👎 1

# region data
# 2021-01-18 11:54:54
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def totalMoney(self, n: int) -> int:
        return n // 7 * 28 + sum([n // 7 + 1 + i for i in range(n % 7)]) + (
            ((1 + n // 7 - 1) * (n // 7 - 1) // 2) if n >= 7 else 1 - 1) * 7


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = 30
    print(Solution().totalMoney(n))
