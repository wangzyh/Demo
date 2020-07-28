# The count-and-say sequence is the sequence of integers with the first five ter
# ms as following: 
# 
#  
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
#  
# 
#  1 is read off as "one 1" or 11. 
# 11 is read off as "two 1s" or 21. 
# 21 is read off as "one 2, then one 1" or 1211. 
# 
#  Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-s
# ay sequence. You can do so recursively, in other words from the previous member 
# read off the digits, counting the number of digits in groups of the same digit. 
# 
# 
#  Note: Each term of the sequence of integers will be represented as a string. 
# 
# 
#  
# 
#  Example 1: 
# 
#  
# Input: 1
# Output: "1"
# Explanation: This is the base case.
#  
# 
#  Example 2: 
# 
#  
# Input: 4
# Output: "1211"
# Explanation: For n = 3 the term was "21" in which we have two groups "2" and "
# 1", "2" can be read as "12" which means frequency = 1 and value = 2, the same wa
# y "1" is read as "11", so the answer is the concatenation of "12" and "11" which
#  is "1211".
#  
#  Related Topics String 
#  👍 1341 👎 9807

# region time
# 2020-07-26 17:14:06
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        elif n == 2:
            return "11"
        a = "11"
        for j in range(n - 2):
            ans = ""
            ctr = 1
            for i in range(len(a)):
                if i != len(a) - 1 and a[i] == a[i + 1]:
                    ctr += 1
                elif i == len(a) - 1:
                    ans = ans + str(ctr) + a[i]
                    ctr = 1
                else:
                    ans = ans + str(ctr) + a[i]
                    ctr = 1
            a = ans
        return ans
        
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = 10
    print(Solution().countAndSay(n))
