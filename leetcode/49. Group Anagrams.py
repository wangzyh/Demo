def main(strs):
    ans = {}
    for ss in strs:
        s = str(sorted(ss))
        if s in ans:
            ans[s].append(ss)
        else:
            ans[s] = [ss]
    return list(ans.values())


if __name__ == '__main__':
    a = main(["eat", "tea", "tan", "ate", "nat", "bat"])
    print(a)