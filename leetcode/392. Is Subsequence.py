"""
Given a string s and a string t, check if s is subsequence of t.
You may assume that there is only lower case English letters in both s and t. t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).
A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
s = "abc", t = "ahbgdc"

Return true.

Example 2:
s = "axc", t = "ahbgdc"

Return false.
"""


def main(s, t):
    # my
    # if len(t) < len(s):
    #     return False
    # t_l = list(t)
    # for i in s[::-1]:
    #     while True:
    #         if not t_l or (len(t_l) < len(s)):
    #             return False
    #         if i == t_l[-1]:
    #             t_l.pop(-1)
    #             break
    #         t_l.pop(-1)
    # return True
    for i in s:
        try:
            index_i = t.index(i)
            t = t[index_i+1:]
        except:
            return False
    return True



a = set()
if __name__ == '__main__':
    a = main("fdsfsdafffff", "fadsfsdffsadfdsf")
    print(a)
