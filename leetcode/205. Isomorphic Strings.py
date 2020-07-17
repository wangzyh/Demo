# 205. Isomorphic Strings
# 2020/7/11


def main(s, t):
    if s == t:
        return True
    if not s or not t or len(s) != len(t):
        return False
    d = {}
    for i in range(len(s)):
        if s[i] in d:
            if d[s[i]] != t[i]:
                return False
        elif t[i] in d.values():
            return False
        d.setdefault(s[i], t[i])
    return True


if __name__ == '__main__':
    s = ""
    t = ""
    a = main(s, t)
    print(a)

