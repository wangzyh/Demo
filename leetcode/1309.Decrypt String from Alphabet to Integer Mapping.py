# Given a string s formed by digits ('0' - '9') and '#' . We want to map s to En
# glish lowercase characters as follows: 
# 
#  
#  Characters ('a' to 'i') are represented by ('1' to '9') respectively. 
#  Characters ('j' to 'z') are represented by ('10#' to '26#') respectively. 
#  
# 
#  Return the string formed after mapping. 
# 
#  It's guaranteed that a unique mapping will always exist. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "10#11#12"
# Output: "jkab"
# Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".
#  
# 
#  Example 2: 
# 
#  
# Input: s = "1326#"
# Output: "acz"
#  
# 
#  Example 3: 
# 
#  
# Input: s = "25#"
# Output: "y"
#  
# 
#  Example 4: 
# 
#  
# Input: s = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"
# Output: "abcdefghijklmnopqrstuvwxyz"
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 1000 
#  s[i] only contains digits letters ('0'-'9') and '#' letter. 
#  s will be valid string such that mapping is always possible. 
#  
#  Related Topics String 
#  👍 511 👎 50

# region data
# 2021-03-12 11:06:22
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def freqAlphabets(self, s: str) -> str:
        d = {'1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e', '6': 'f', '7': 'g', '8': 'h', '9': 'i', '10': 'j',
             '11': 'k', '12': 'l', '13': 'm', '14': 'n', '15': 'o', '16': 'p', '17': 'q', '18': 'r', '19': 's',
             '20': 't', '21': 'u', '22': 'v', '23': 'w', '24': 'x', '25': 'y', '26': 'z'}
        res = ''
        ll = s.split('#')
        for i in ll[:-1]:
            if not i:
                continue
            for j in i[:-2]:
                res += d[j]
            res += d[i[-2:]]
        for i in ll[-1]:
            for j in i:
                res += d[j]

        return res


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = "1326#"
    print(Solution().freqAlphabets(n))
