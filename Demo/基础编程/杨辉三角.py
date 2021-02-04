def yanghui():
    L = [1]
    while True:
        yield L
        L.append(0)
        L = [L[i - 1] + L[i] for i in range(len(L))]


n = 0
for t in yanghui():
    print(t)
    n = n + 1
    if n == 9:
        break

# from functools import reduce
#
#
# def f(x, y):
#     return x * 10 + y
#
#
# print(reduce(f, ([1, 2, 3, 4, 5])))
