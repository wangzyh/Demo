def main(s, t):
    return list(set(t).difference(set(s)))[0]

a = set()
if __name__ == '__main__':
    a = main(s="abcd", t="abcde")
    print(a)
