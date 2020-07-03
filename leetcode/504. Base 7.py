# 504. Base 7
# 2020/5/13


def main(num):
    representation = ''
    c = ''
    if num < 0:
        c = '-'
        num *= -1
    while 1:
        quotient = num // 7
        remainder = num % 7
        representation += str(remainder)

        if quotient == 0:
            break
        num = quotient

    return c+representation[::-1]


if __name__ == '__main__':
    num = -7
    a = main(num)
    print(a)

