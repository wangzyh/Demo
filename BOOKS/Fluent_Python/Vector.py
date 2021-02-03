from math import hypot


class Vector:
    # Vector 的构造函数接受字符串。而且，对于使用字符串构造的Vector，这6个特殊方法中，只有__abs__和__bool__会报错。

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector {self.x}, {self.y}'

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        # return bool(abs(self))
        return bool(self.x or self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.x + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    # def __str__(self):
    #     return 'This is a Vector'


v1 = Vector(2, 4)
v2 = Vector(2, 1)
print(v1 + v2)
# abs 是一个内置函数，如果输入是整数或者浮点数，它返回的是输入值的绝对值；如果输入是复数（complex number），那么返回这个复数的模
v = Vector(3, 4)
print(abs(v))
# 利用 * 运算符来实现向量的标量乘法（即向量与数的乘法，得到的结果向量的方向与原向量一致 ，模变大）：
print(v * 3)
print(abs(v * 3))
print(v1)
# 当交换两个操作数的位置时，就会调用反向运算符（b * a 而不是 a * b）。增量赋值运算符则是一种把中缀运算符变成赋值运算的捷径（a = a * b 就变成了 a *= b）
