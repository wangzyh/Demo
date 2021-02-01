# You are given an array of strings words and a string chars. 
# 
#  A string is good if it can be formed by characters from chars (each character
#  can only be used once). 
# 
#  Return the sum of lengths of all good strings in words. 
# 
#  
# 
#  Example 1: 
# 
#  
# Input: words = ["cat","bt","hat","tree"], chars = "atach"
# Output: 6
# Explanation: 
# The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
# 
#  
# 
#  Example 2: 
# 
#  
# Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
# Output: 10
# Explanation: 
# The strings that can be formed are "hello" and "world" so the answer is 5 + 5 
# = 10.
#  
# 
#  
# 
#  Note: 
# 
#  
#  1 <= words.length <= 1000 
#  1 <= words[i].length, chars.length <= 100 
#  All strings contain lowercase English letters only. 
#  Related Topics Array Hash Table 
#  👍 527 👎 88

# region data
# 2021-01-25 10:53:31
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countCharacters(self, words, chars: str) -> int:
        res = 0
        from collections import Counter
        d = dict(Counter(chars))
        for i in words:
            n = 0
            d_i = dict(Counter(i))
            for j in d_i:
                if j not in d or (d_i[j] > d[j]):
                    n = 0
                    break
                else:
                    n += d_i[j]
            res += n
        return res


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    words = ["hello", "world", "leetcode"]
    chars = "welldonehoneyr"
    print(Solution().countCharacters(words, chars))
