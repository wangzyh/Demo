# You are given a string s of even length. Split this string into two halves of 
# equal lengths, and let a be the first half and b be the second half. 
# 
#  Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 
# 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowerca
# se letters. 
# 
#  Return true if a and b are alike. Otherwise, return false. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "book"
# Output: true
# Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore
# , they are alike.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "textbook"
# Output: false
# Explanation: a = "text" and b = "book". a has 1 vowel whereas b has 2. Therefo
# re, they are not alike.
# Notice that the vowel o is counted twice.
#  
# 
#  Example 3: 
# 
#  
# Input: s = "MerryChristmas"
# Output: false
#  
# 
#  Example 4: 
# 
#  
# Input: s = "AbCdEfGh"
# Output: true
#  
# 
#  
#  Constraints: 
# 
#  
#  2 <= s.length <= 1000 
#  s.length is even. 
#  s consists of uppercase and lowercase letters. 
#  
#  Related Topics String 
#  👍 102 👎 5

# region time
# 2021-01-23 16:17:30
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        from collections import Counter
        left, right = dict(Counter(s[:len(s) // 2])), dict(Counter(s[len(s) // 2:]))
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        return sum([left.get(i, 0) for i in vowels]) == sum([right.get(i, 0) for i in vowels])

    # leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = "teetbook"
    print(Solution().halvesAreAlike(n))
