# 20. Valid Parentheses
# 2020/5/12


def main(s):
    # my
    # dic_s = {'(': 1, ')': -1, '{': 2, '}': -2, '[': 4, ']': -4}
    # l = []
    # if not s:
    #     return True
    # if (len(s) % 2 != 0) or (dic_s[s[0]] < 0):
    #     return False
    # for i in s:
    #     if dic_s[i] > 0:
    #         l.append(dic_s[i])
    #     else:
    #         if dic_s[i] + l[-1] == 0:
    #             l.pop(-1)
    #         else:
    #             return False
    # if sum(l) != 0:
    #     return False
    # return True

    #
    mapping = {'(': ')',
               '[': ']',
               '{': '}'}

    l = []
    for i in s:
        if i in mapping:
            l.append(i)
        else:
            if not l:
                return False
            if i != mapping[l[-1]]:
                return False
            l.pop(-1)

    return not l


if __name__ == '__main__':
    s = "]"
    a = main(s)
    print(a)
