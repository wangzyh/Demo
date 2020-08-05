# Write a function that takes a string as input and reverse only the vowels of a
#  string. 
# 
#  Example 1: 
# 
#  
# Input: "hello"
# Output: "holle"
#  
# 
#  
#  Example 2: 
# 
#  
# Input: "leetcode"
# Output: "leotcede" 
#  
# 
#  Note: 
# The vowels does not include the letter "y". 
# 
#  
#  Related Topics Two Pointers String 
#  👍 698 👎 1154

# region time
# 2020-08-03 21:57:44
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverseVowels(self, s: str) -> str:
        defoult = 'aeiouAEIOU'
        s = list(s)
        setp = 0
        for i in range(len(s)):
            if s[i] in defoult:
                for j in range(len(s) - setp - 1, i, -1):
                    setp += 1
                    if s[j] in defoult:
                        s[i], s[j] = s[j], s[i]
                        break
        return ''.join(s)


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    # n = "aea"
    # n = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccccccccccccccccccccccccccccccccccccccccccccccccccccccddddddddddddddddddddddddddddddddddddddddddddddddddddddddddeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeegggggggggggggggggggggggggggggggggggggggggggg"
    n = 'Aa'
    print(Solution().reverseVowels(n))
