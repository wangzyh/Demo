#
# Given n pairs of parentheses, write a function to generate all combinations of
#  well-formed parentheses.
#
#
#
# For example, given n = 3, a solution set is:
#
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]
#  Related Topics String Backtracking
#  👍 5266 👎 270


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def generateParenthesis(self, n: int):
        left, right = '(', ')'
        res = []
        lens = n * 2
        l = ''
        for i in range(lens - 1):
            l += left
            for j in range(1, lens):
                res.append(i) 
        return res


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = 3
    a = Solution().generateParenthesis(n)
    print(a)
