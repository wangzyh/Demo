# 写程序实现一个函数PrintN，使得传入的一个正整数为N的参数后，能顺序打印从1到N的全部正整数
import time
import sys


def print_n_1(n):
    for i in range(n):
        print(f'{i}\n')


def print_n_2(n):
    if n:
        print_n_2(n - 1)
        print(f'{n}\n')


if __name__ == '__main__':
    n = 999
    start_time_1 = time.time()
    print_n_1(n)
    end_time_1 = time.time() - start_time_1

    start_time_2 = time.time()
    print_n_2(n)
    end_time_2 = time.time() - start_time_2

    print(f'first print time:{end_time_1}')
    print(f'first print time:{end_time_2}')
