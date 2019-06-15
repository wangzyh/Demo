def main(s):
    # if s == s[::-1]:
    #     return s
    # slen = len(s)
    # li = ""
    # ls = list(s)
    # distance = 0
    #
    # if ls.count(ls[0]) < 2:
    #     # return self.longestPalindrome(s[1:])
    #     return main(s[1:])
    #
    # for i in range(slen):
    #     for j in range(slen, i, -1):
    #         if j - i < distance:
    #             break
    #         if s[i:j][::-1] == s[i:j] and len(s[i:j]) > len(li):
    #             li = s[i:j]
    #             distance = j - i
    #             break
    #
    # return li
    longest = ""
    i = 0
    while i < len(s):
        l = i
        r = i
        while r + 1 < len(s) and s[r] == s[r + 1]:
            r = r + 1
        i = r + 1

        while l >= 0 and r < len(s) and s[l] == s[r]:
            l = l - 1
            r = r + 1

        ans = s[l + 1:r]
        if len(longest) < len(ans):
            longest = ans
    return longest


if __name__ == '__main__':
    a = main("babad")
    print(a)
