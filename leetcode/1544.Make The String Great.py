# Given a string s of lower and upper case English letters. 
# 
#  A good string is a string which doesn't have two adjacent characters s[i] and
#  s[i + 1] where: 
# 
#  
#  0 <= i <= s.length - 2 
#  s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case
#  or vice-versa. 
#  
# 
#  To make the string good, you can choose two adjacent characters that make the
#  string bad and remove them. You can keep doing this until the string becomes go
# od. 
# 
#  Return the string after making it good. The answer is guaranteed to be unique
#  under the given constraints. 
# 
#  Notice that an empty string is also good. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "leEeetcode"
# Output: "leetcode"
# Explanation: In the first step, either you choose i = 1 or i = 2, both will re
# sult "leEeetcode" to be reduced to "leetcode".
#  
# 
#  Example 2: 
# 
#  
# Input: s = "abBAcC"
# Output: ""
# Explanation: We have many possible scenarios, and all lead to the same answer.
#  For example:
# "abBAcC" --> "aAcC" --> "cC" --> ""
# "abBAcC" --> "abBA" --> "aA" --> ""
#  
# 
#  Example 3: 
# 
#  
# Input: s = "s"
# Output: "s"
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 100 
#  s contains only lower and upper case English letters. 
#  Related Topics String Stack 
#  👍 353 👎 36

# region data
# 2021-02-25 14:55:54
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def makeGood(self, s: str) -> str:
        # n = 0
        # ls = list(s)
        # if not s:
        #     return ''
        # while n <= len(ls) - 2:
        #     if ls[n].islower() and (ls[n].upper() == ls[n + 1]):
        #         ls.pop(n)
        #         ls.pop(n)
        #     if n >= len(ls) - 1:
        #         break
        #     if ls[n].isupper() and (ls[n].lower() == ls[n + 1]):
        #         ls.pop(n)
        #         ls.pop(n)
        #     n += 1
        # if ''.join(ls) == s:
        #     return ''.join(ls)
        # return self.makeGood(''.join(ls))
        if not s:
            return ''
        stack = [s[0]]
        for i in s[1:]:
            if not stack:
                stack.append(i)
                continue
            if i.islower() and stack[-1] == i.upper():
                stack.pop(-1)
                continue
            elif i.isupper() and stack[-1] == i.lower():
                stack.pop(-1)
                continue
            stack.append(i)
        return ''.join(stack)


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = "aaaabaabBAABAAddD"
    print(Solution().makeGood(n))
