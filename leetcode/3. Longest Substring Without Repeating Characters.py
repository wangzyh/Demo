def main(s):
    res = ''
    max_size = 0
    list_s = list(s)
    for i in list_s:
        if i in res:
            res = res[res.index(i)+1:] + i
            if len(res) > max_size:
                max_size = len(res)
            continue
        res += i
        if len(res) > max_size:
            max_size = len(res)
    return max_size


if __name__ == '__main__':
    a = main("nfpdmpi")
    print(a)
