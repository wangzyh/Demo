# Given a string S, return the "reversed" string where all characters that are n
# ot a letter stay in the same place, and all letters reverse their positions. 
# 
#  
# 
#  
#  
#  
#  
#  
#  
#  
#  
# 
#  
#  Example 1: 
# 
#  
# Input: "ab-cd"
# Output: "dc-ba"
#  
# 
#  
#  Example 2: 
# 
#  
# Input: "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"
#  
# 
#  
#  Example 3: 
# 
#  
# Input: "Test1ng-Leet=code-Q!"
# Output: "Qedo1ct-eeLg=ntse-T!"
#  
# 
#  
# 
#  
#  Note: 
# 
#  
#  S.length <= 100 
#  33 <= S[i].ASCIIcode <= 122 
#  S doesn't contain \ or " 
#  
#  
#  
#  
#  Related Topics String 
#  👍 723 👎 40

# region data
# 2021-01-21 15:49:07
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        if not S:
            return S
        indexs = [[i, S[i]] for i, j in enumerate(S) if ord(j) < 65 or (91 <= ord(j) <= 96)]
        S = list(S)[::-1]
        for i in indexs:
            S.remove(i[1])
        for i in indexs:
            S.insert(i[0], i[1])
        return ''.join(S)


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    # n = "Test1ng-Leet=code-Q!"
    n = ""
    print(Solution().reverseOnlyLetters(n))
