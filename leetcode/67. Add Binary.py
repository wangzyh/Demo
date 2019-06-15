def main(a, b):
    count = int(a, 2) + int(b, 2)

    return bin(count)[2:]

if __name__ == '__main__':
    a = main(a = "1010", b = "1011")
    print(a)