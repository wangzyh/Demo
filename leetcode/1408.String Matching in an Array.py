# Given an array of string words. Return all strings in words which is substring
#  of another word in any order. 
# 
#  String words[i] is substring of words[j], if can be obtained removing some ch
# aracters to left and/or right side of words[j]. 
# 
#  
#  Example 1: 
# 
#  
# Input: words = ["mass","as","hero","superhero"]
# Output: ["as","hero"]
# Explanation: "as" is substring of "mass" and "hero" is substring of "superhero
# ".
# ["hero","as"] is also a valid answer.
#  
# 
#  Example 2: 
# 
#  
# Input: words = ["leetcode","et","code"]
# Output: ["et","code"]
# Explanation: "et", "code" are substring of "leetcode".
#  
# 
#  Example 3: 
# 
#  
# Input: words = ["blue","green","bu"]
# Output: []
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= words.length <= 100 
#  1 <= words[i].length <= 30 
#  words[i] contains only lowercase English letters. 
#  It's guaranteed that words[i] will be unique. 
#  Related Topics String 
#  👍 259 👎 55

# region data
# 2021-01-26 12:03:09
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def stringMatching(self, words):
        res = []
        words = sorted(words, key=lambda x: len(x))
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                if words[i] in words[j]:
                    res.append(words[i])
                    break
        return res


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = ["leetcoder", "leetcode", "od", "hamlet", "am"]
    print(Solution().stringMatching(n))
