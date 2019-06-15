def creatNum():
    a, b = 0, 1
    for i in range(5):
        yield b
        a, b = b, a + b


i = creatNum()

for num in i:
    print(num)
# 注意
#  next(a） 等价于 a.__next__()
