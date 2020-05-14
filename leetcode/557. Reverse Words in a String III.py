def reverseWords(s):
    res = ''
    list_s = s.split(' ')
    for i in list_s:
        res += f'{i[::-1]} '
    return res.rstrip()

if __name__ == '__main__':
    s = "Let's take LeetCode contest"
    res = reverseWords(s)
    print(res)