# 172. Factorial Trailing Zeroes
# 2020/5/13


def main(n):
    return int(n//5 + (n**0.5//5))


if __name__ == '__main__':
    n = 444
    a = main(n)
    print(a)
