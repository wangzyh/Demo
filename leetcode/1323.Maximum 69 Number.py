# Given a positive integer num consisting only of digits 6 and 9. 
# 
#  Return the maximum number you can get by changing at most one digit (6 become
# s 9, and 9 becomes 6). 
# 
#  
#  Example 1: 
# 
#  
# Input: num = 9669
# Output: 9969
# Explanation: 
# Changing the first digit results in 6669.
# Changing the second digit results in 9969.
# Changing the third digit results in 9699.
# Changing the fourth digit results in 9666. 
# The maximum number is 9969.
#  
# 
#  Example 2: 
# 
#  
# Input: num = 9996
# Output: 9999
# Explanation: Changing the last digit 6 to 9 results in the maximum number. 
# 
#  Example 3: 
# 
#  
# Input: num = 9999
# Output: 9999
# Explanation: It is better not to apply any change. 
# 
#  
#  Constraints: 
# 
#  
#  1 <= num <= 10^4 
#  num's digits are 6 or 9. 
#  Related Topics Math 
#  👍 485 👎 80

# region time
# 2021-01-24 02:00:21
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maximum69Number(self, num: int) -> int:
        n = list(str(num))
        if '6' in n:
            n[n.index('6')] = '9'
            return int(''.join(n))

        return num


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = 9669
    print(Solution().maximum69Number(n))
