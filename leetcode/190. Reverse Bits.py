# 190. Reverse Bits
# 2020/7/4


def main(n):
    b = bin(n)[:1:-1]
    return int(b + (32-len(b))*'0', 2)


if __name__ == '__main__':
    a = main(11111111111111111111111111111101)
    print(a)

