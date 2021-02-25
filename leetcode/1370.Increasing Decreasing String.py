# Given a string s. You should re-order the string using the following algorithm
# : 
# 
#  
#  Pick the smallest character from s and append it to the result. 
#  Pick the smallest character from s which is greater than the last appended ch
# aracter to the result and append it. 
#  Repeat step 2 until you cannot pick more characters. 
#  Pick the largest character from s and append it to the result. 
#  Pick the largest character from s which is smaller than the last appended cha
# racter to the result and append it. 
#  Repeat step 5 until you cannot pick more characters. 
#  Repeat the steps from 1 to 6 until you pick all characters from s. 
#  
# 
#  In each step, If the smallest or the largest character appears more than once
#  you can choose any occurrence and append it to the result. 
# 
#  Return the result string after sorting s with this algorithm. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "aaaabbbbcccc"
# Output: "abccbaabccba"
# Explanation: After steps 1, 2 and 3 of the first iteration, result = "abc"
# After steps 4, 5 and 6 of the first iteration, result = "abccba"
# First iteration is done. Now s = "aabbcc" and we go back to step 1
# After steps 1, 2 and 3 of the second iteration, result = "abccbaabc"
# After steps 4, 5 and 6 of the second iteration, result = "abccbaabccba"
#  
# 
#  Example 2: 
# 
#  
# Input: s = "rat"
# Output: "art"
# Explanation: The word "rat" becomes "art" after re-ordering it with the mentio
# ned algorithm.
#  
# 
#  Example 3: 
# 
#  
# Input: s = "leetcode"
# Output: "cdelotee"
#  
# 
#  Example 4: 
# 
#  
# Input: s = "ggggggg"
# Output: "ggggggg"
#  
# 
#  Example 5: 
# 
#  
# Input: s = "spo"
# Output: "ops"
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 500 
#  s contains only lower-case English letters. 
#  
#  Related Topics String Sort 
#  👍 322 👎 335

# region data
# 2021-02-24 16:35:56
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
from collections import Counter


class Solution:
    def sortString(self, s: str) -> str:
        res = ''
        d = dict(Counter(s))
        first = max(d.values())
        d = sorted(d.items(), key=lambda x: ord(x[0]))
        d = list(map(list, d))
        n = 0
        for i in range(first):
            if n % 2 == 0:
                j = 0
                while j < len(d):
                    if not d:
                        break
                    res += d[j][0]
                    d[j][1] -= 1
                    if d[j][1] == 0:
                        d.pop(j)
                        j -= 1
                    j += 1
            else:
                k = len(d) - 1
                while k >= 0:
                    if not d:
                        break
                    res += d[k][0]
                    d[k][1] -= 1
                    if d[k][1] == 0:
                        d.pop(k)
                        # k -= 1
                    k -= 1
            n += 1
        return res


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = 'aaabbz'
    print(Solution().sortString(n))
