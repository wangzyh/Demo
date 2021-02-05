# region 列表生成式 推导式
# 1.
x = 'ABC'
dummy = [ord(x) for x in x]
print(x)
print(dummy)
"""
生成式有作用域，类似函数
表达式内部的变量和赋值只在局部起作用，表达式的上下文里的同名变量还可以被正常引用，局部变量并不会影响到它们
x
>>> 'ABC'
dummy
>>> [65, 66, 67]
"""

# 2. 列表推导 与 map/filter 组合 比较
symbols = '$¢£¥€¤'
beyond_ascii1 = [ord(s) for s in symbols if ord(s) > 127]
print(beyond_ascii1)

beyond_ascii2 = list(filter(lambda x: x > 127, map(ord, symbols)))
print(beyond_ascii2)

# 3. 生成器表达式
beyond_ascii3 = tuple(ord(symbol) for symbol in symbols)
print(beyond_ascii3)
import array

beyond_ascii4 = array.array('I', (ord(symbol) for symbol in symbols))
print(beyond_ascii4)
# endregion


# region 元组
# 把元组用作记录
lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '311958555'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
for passport in sorted(traveler_ids):
    print('%s/%s' % passport)

for country, _ in traveler_ids:
    print(country)
# ----------------------------------------------------------------------------------------------------------------------
# 元组拆包可以应用到任何可迭代对象上，唯一的硬性要求是，被可迭代对象中的元素数量必须要跟接受这些元素的元组的空档数一致。
# 除非我们用 * 来表示忽略多余的元素，在“用 * 来处理多余的元素”一节里，我会讲到它的具体用法。Python 爱好者们很
# 喜欢用元组拆包这个说法，但是可迭代元素拆包这个表达也慢慢流行了起来，比如“PEP 3132—Extended Iterable
# Unpacking”（https://www.python.org/dev/peps/pep-3132/）的标题就是这么用的

# 元组拆包
latitude, longitude = lax_coordinates
print(latitude)
print(longitude)

latitude, longitude = longitude, latitude

# 还可以用 * 运算符把一个可迭代对象拆开作为函数的参数
print(divmod(20, 8))
""">>>(2, 4)"""
t = (20, 8)
print(divmod(*t))
""">>>(2, 4)"""
quotient, remainder = divmod(*t)
"""quotient = 2, remainder = 4"""

import os

_, filename = os.path.split(os.getcwd())
print(filename)

# 用*处理剩下的元素, * 前缀只能用在一个变量名前面，但是这个变量可以出现在赋值表达式的任意位置
a, b, *rest = range(5)
print(a, b, rest)
a, b, *rest = range(3)
print(a, b, rest)
a, b, *rest = range(2)
print(a, b, rest)

a, *body, c, d = range(5)
print(a, body, c, d)

# 嵌套元组拆包

metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]
print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
for name, cc, pop, (latitude, longitude) in metro_areas:
    if longitude <= 0:
        print(fmt.format(name, latitude, longitude))

# ----------------------------------------------------------------------------------------------------------------------
# 具名元组
from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
print(tokyo)
print(tokyo.population)
print(tokyo.coordinates)
print(tokyo[1])

# 专有属性
print('专有属性 _fields:', City._fields)
LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
delhi = City._make(delhi_data)
print('专有属性 _asdict:', delhi._asdict())

for key, value in delhi._asdict().items():
    print(f'{key}:{value}')

# ----------------------------------------------------------------------------------------------------------------------
# 切片
l = [10, 20, 30, 40, 50, 60]
print(l[:2])  # 在下标2的地方分割
# [10, 20]
print(l[2:])
# [30, 40, 50, 60]
print(l[:3])  # 在下标3的地方分割
# [10, 20, 30]
print(l[3:])
# [40, 50, 60]

# 对对象进行切片
invoice = """
    0     6                       40            52      55      
    1909 Pimoroni PiBrella        $17.50        3       $52.50
    1489 6mm Tactile Switch x20   $4.95         2       $9.90
    1510 Panavise Jr. - PV-201    $28.00        1       $28.00
    1601 PiTFT Mini Kit 320x240   $34.95        1       $34.95
    """
SKU = slice(0, 6)
DESCRIPTION = slice(6, 40)
UNIT_PRICE = slice(40, 52)
QUANTITY = slice(52, 55)
ITEM_TOTAL = slice(55, None)
line_items = invoice.split('\n')[2:]
for item in line_items:
    print(item[UNIT_PRICE], item[DESCRIPTION])

# 多维切片和省略
# 逗号分开的多个索引或者是切片，外部库NumPy 里就用到了这个特性，二维的 numpy.ndarray 就可以用 a[i,j] 这种形式来获取，抑或是用 a[m:n, k:l] 的方式来得到二维切片

# 给切片赋值
l = list(range(10))
print(l)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
l[2:5] = [20, 30]
print(l)
# [0, 1, 20, 30, 5, 6, 7, 8, 9]
del l[5:7]
print(l)
# [0, 1, 20, 30, 5, 8, 9]
l[3::2] = [11, 22]
print(l)
# [0, 1, 20, 11, 5, 22, 9]
l[2:5] = 100  # ➊
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# TypeError: can only assign an iterable
l[2:5] = [100]
print(l)
# [0, 1, 100, 22, 9]
# 如果赋值的对象是一个切片，那么赋值语句的右侧必须是个可迭代对象。即便只有单独一个值，也要把它转换成可迭代的序列

# endregion
