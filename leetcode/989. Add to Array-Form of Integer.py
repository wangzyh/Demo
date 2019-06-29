def main(A, K):
    count = int(str(A).replace(',', '').replace('[', '').replace(']', '').replace(' ', ''))
    return list(map(int, str(count + K)))


if __name__ == '__main__':
    a = main(A = [1,2,0,0], K = 34)
    print(a)
