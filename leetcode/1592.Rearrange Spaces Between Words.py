# You are given a string text of words that are placed among some number of spac
# es. Each word consists of one or more lowercase English letters and are separate
# d by at least one space. It's guaranteed that text contains at least one word. 
# 
#  Rearrange the spaces so that there is an equal number of spaces between every
#  pair of adjacent words and that number is maximized. If you cannot redistribute
#  all the spaces equally, place the extra spaces at the end, meaning the returned
#  string should be the same length as text. 
# 
#  Return the string after rearranging the spaces. 
# 
#  
#  Example 1: 
# 
#  
# Input: text = "  this   is  a sentence "
# Output: "this   is   a   sentence"
# Explanation: There are a total of 9 spaces and 4 words. We can evenly divide t
# he 9 spaces between the words: 9 / (4-1) = 3 spaces.
#  
# 
#  Example 2: 
# 
#  
# Input: text = " practice   makes   perfect"
# Output: "practice   makes   perfect "
# Explanation: There are a total of 7 spaces and 3 words. 7 / (3-1) = 3 spaces p
# lus 1 extra space. We place this extra space at the end of the string.
#  
# 
#  Example 3: 
# 
#  
# Input: text = "hello   world"
# Output: "hello   world"
#  
# 
#  Example 4: 
# 
#  
# Input: text = "  walks  udp package   into  bar a"
# Output: "walks  udp  package  into  bar  a "
#  
# 
#  Example 5: 
# 
#  
# Input: text = "a"
# Output: "a"
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= text.length <= 100 
#  text consists of lowercase English letters and ' '. 
#  text contains at least one word. 
#  
#  Related Topics String 
#  👍 115 👎 122

# region time
# 2021-02-21 19:06:05
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reorderSpaces(self, text: str) -> str:
        space = text.count(' ')
        data = [i for i in text.split() if i != '']
        if space == 0:
            return data[0]
        if len(data) == 1:
            return data[0] + ' ' * space
        return (' ' * (space // (len(data) - 1))).join(data) + ' ' * (space % (len(data) - 1))


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = "  hello"
    print(Solution().reorderSpaces(n))
