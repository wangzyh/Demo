def main(digits):
    num = 0
    for i in range(len(digits)):
        num += digits[i]*10**(len(digits)-i-1)
    num += 1
    print(num)
    return [int(x) for x in str(num)]


if __name__ == '__main__':
    a = main([1, 2, 3])
    print(a)