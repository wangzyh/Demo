# 119. Pascal's Triangle II
# 2020/7/6


def main(rowIndex):
    ret = [1]
    while True:
        yield ret
        for i in range(1, len(ret)):
            ret[i] = pre[i] + pre[i - 1]
        ret.append(1)
        pre = ret[:]


if __name__ == '__main__':
    a = main(3)
    print(a)

