# 写程序计算给多项式{Data/1.3.png}，在给定点x=1.1处的值
import time


def f1(n, a, x):
    p = a[n]
    for i in range(n):
        p += a[i] * pow(x, i)
    return p


def f2(n, a, x):
    p = a[n]
    for i in range(n, 0, -1):
        p = a[i - 1] + x * p
    return p


if __name__ == '__main__':
    max_n = 1000
    a = [i / 1 for i in range(max_n)]
    x = 1.1
    start_time_1 = time.time()
    for i in range(max_n):
        f1(max_n - 1, a, x)
    end_time_1 = time.time() - start_time_1

    start_time_2 = time.time()
    for i in range(max_n):
        f2(max_n - 1, a, x)
    end_time_2 = time.time() - start_time_2

    print(f'first print time:{end_time_1/max_n}')
    print(f'first print time:{end_time_2/max_n}')
