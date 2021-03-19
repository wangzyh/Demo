# Given a string paragraph and a string array of the banned words banned, return
#  the most frequent word that is not banned. It is guaranteed there is at least o
# ne word that is not banned, and that the answer is unique. 
# 
#  The words in paragraph are case-insensitive and the answer should be returned
#  in lowercase. 
# 
#  
#  Example 1: 
# 
#  
# Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", 
# banned = ["hit"]
# Output: "ball"
# Explanation: 
# "hit" occurs 3 times, but it is a banned word.
# "ball" occurs twice (and no other word does), so it is the most frequent non-b
# anned word in the paragraph. 
# Note that words in the paragraph are not case sensitive,
# that punctuation is ignored (even if adjacent to words, such as "ball,"), 
# and that "hit" isn't the answer even though it occurs more because it is banne
# d.
#  
# 
#  Example 2: 
# 
#  
# Input: paragraph = "a.", banned = []
# Output: "a"
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= paragraph.length <= 1000 
#  paragraph consists of English letters, space ' ', or one of the symbols: "!?'
# ,;.". 
#  0 <= banned.length <= 100 
#  1 <= banned[i].length <= 10 
#  banned[i] consists of only lowercase English letters. 
#  
#  Related Topics String 
#  👍 925 👎 2048

# region data
# 2021-03-19 16:20:22
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
from collections import Counter


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        for i in "!?',;.":
            paragraph = paragraph.replace(i, ' ')
        d = dict(Counter(paragraph.split(' ')))
        s = [i[0] for i in sorted(d.items(), key=lambda x: x[1], reverse=True)]
        for i in s:
            if i not in banned and i != '':
                return i


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = "a, a, a, a, b,b,b,c, c"
    banned = ["a"]
    print(Solution().mostCommonWord(n, banned))
