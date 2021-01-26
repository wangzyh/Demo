# A sentence S is given, composed of words separated by spaces. Each word consis
# ts of lowercase and uppercase letters only. 
# 
#  We would like to convert the sentence to "Goat Latin" (a made-up language sim
# ilar to Pig Latin.) 
# 
#  The rules of Goat Latin are as follows: 
# 
#  
#  If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of t
# he word. 
#  For example, the word 'apple' becomes 'applema'. 
#  
#  If a word begins with a consonant (i.e. not a vowel), remove the first letter
#  and append it to the end, then add "ma". 
#  For example, the word "goat" becomes "oatgma". 
#  
#  Add one letter 'a' to the end of each word per its word index in the sentence
# , starting with 1. 
#  For example, the first word gets "a" added to the end, the second word gets "
# aa" added to the end and so on. 
#  
# 
#  Return the final sentence representing the conversion from S to Goat Latin. 
# 
#  
# 
#  Example 1: 
# 
#  
# Input: "I speak Goat Latin"
# Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
#  
# 
#  Example 2: 
# 
#  
# Input: "The quick brown fox jumped over the lazy dog"
# Output: "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetm
# aaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"
#  
# 
#  
# 
#  Notes: 
# 
#  
#  S contains only uppercase, lowercase and spaces. Exactly one space between ea
# ch word. 
#  1 <= S.length <= 150. 
#  
#  Related Topics String 
#  👍 473 👎 894

# region data
# 2021-01-26 10:46:22
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def toGoatLatin(self, S: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        res = []
        n = 1
        for i in S.split(' '):
            if i[0] in vowels:
                res.append(i + 'ma' + 'a' * n)
            else:
                res.append(i[1:] + i[0] + 'ma' + 'a' * n)
            n += 1
        return ' '.join(res)


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = "The quick brown fox jumped over the lazy dog"
    print(Solution().toGoatLatin(n))
