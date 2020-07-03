# 201. Bitwise AND of Numbers Range
# 2020/6/1


def main(m: int, n: int):
    result = 1
    for i in range(m, n+1):
        result = i & result
    return result


if __name__ == '__main__':
    m = 5
    n = 7
    a = main(m, n)
    print(a)

