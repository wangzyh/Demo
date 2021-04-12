# Given a string array words, return the maximum value of length(word[i]) * leng
# th(word[j]) where the two words do not share common letters. If no such two word
# s exist, return 0. 
# 
#  
#  Example 1: 
# 
#  
# Input: words = ["abcw","baz","foo","bar","xtfn","abcdef"]
# Output: 16
# Explanation: The two words can be "abcw", "xtfn".
#  
# 
#  Example 2: 
# 
#  
# Input: words = ["a","ab","abc","d","cd","bcd","abcd"]
# Output: 4
# Explanation: The two words can be "ab", "cd".
#  
# 
#  Example 3: 
# 
#  
# Input: words = ["a","aa","aaa","aaaa"]
# Output: 0
# Explanation: No such pair of words.
#  
# 
#  
#  Constraints: 
# 
#  
#  2 <= words.length <= 1000 
#  1 <= words[i].length <= 1000 
#  words[i] consists only of lowercase English letters. 
#  
#  Related Topics Bit Manipulation 
#  👍 1014 👎 79

# region time
# 2021-04-11 17:52:32
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        max_len = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                s = set(words[i]) & set(words[j])
                m = len(words[i]) * len(words[j])
                if not s and m > max_len:
                    max_len = len(words[i]) * len(words[j])
        return max_len

        # d = {}
        # for w in words:
        #     mask = 0
        #     for c in set(w):
        #         mask |= (1 << (ord(c) - ord('a')))
        #     d[mask] = max(d.get(mask, 0), len(w))
        # return max([d[x] * d[y] for x in d for y in d if not x & y] or [0])


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
    print(Solution().maxProduct(n))
