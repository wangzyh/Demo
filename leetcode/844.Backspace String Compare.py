# Given two strings S and T, return if they are equal when both are typed into e
# mpty text editors. # means a backspace character. 
# 
#  Note that after backspacing an empty text, the text will continue empty. 
# 
#  
#  Example 1: 
# 
#  
# Input: S = "ab#c", T = "ad#c"
# Output: true
# Explanation: Both S and T become "ac".
#  
# 
#  
#  Example 2: 
# 
#  
# Input: S = "ab##", T = "c#d#"
# Output: true
# Explanation: Both S and T become "".
#  
# 
#  
#  Example 3: 
# 
#  
# Input: S = "a##c", T = "#a#c"
# Output: true
# Explanation: Both S and T become "c".
#  
# 
#  
#  Example 4: 
# 
#  
# Input: S = "a#c", T = "b"
# Output: false
# Explanation: S becomes "c" while T becomes "b".
#  
# 
#  Note: 
# 
#  
#  1 <= S.length <= 200 
#  1 <= T.length <= 200 
#  S and T only contain lowercase letters and '#' characters. 
#  
# 
#  Follow up: 
# 
#  
#  Can you solve it in O(N) time and O(1) space? 
#  
#  
#  
#  
#  
#  Related Topics Two Pointers Stack 
#  👍 2184 👎 104

# region time
# 2021-01-17 23:39:09
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        # s, t = [], []
        # for i in S:
        #     if i == '#' and s:
        #         s.pop(-1)
        #     elif i != '#':
        #         s.append(i)
        # for i in T:
        #     if i == '#' and t:
        #         t.pop(-1)
        #     elif i != '#':
        #         t.append(i)
        # return s == t
        s = list(S)
        t = list(T)



# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    S = "y#fo##f"
    T = "y#f#o##f"
    print(Solution().backspaceCompare(S, T))
