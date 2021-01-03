# Given a string containing digits from 2-9 inclusive, return all possible lette
# r combinations that the number could represent. Return the answer in any order. 
# 
# 
#  A mapping of digit to letters (just like on the telephone buttons) is given b
# elow. Note that 1 does not map to any letters. 
# 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
#  
# 
#  Example 2: 
# 
#  
# Input: digits = ""
# Output: []
#  
# 
#  Example 3: 
# 
#  
# Input: digits = "2"
# Output: ["a","b","c"]
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= digits.length <= 4 
#  digits[i] is a digit in the range ['2', '9']. 
#  Related Topics String Backtracking Depth-first Search Recursion 
#  👍 5004 👎 471

# region time
# 2020-12-29 21:26:55
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def letterCombinations(self, digits: str):
        if not digits:
            return []
        d = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if len(digits) == 1:
            return list(d[digits[0]])
        res = list(d[digits[0]])
        l = [d[i] for i in list(digits[1:])]
        for i in l:
            res = [(x + y) for x in res for y in i]
        return res


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    # n = '23'
    # n = '2'
    n = '23'
    print(Solution().letterCombinations(n))
