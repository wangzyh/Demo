'''
def func(funcx):
    print('正在装载1')

    def func_in(*args, **kwargs):
        print('func_in')
        funcx(*args, **kwargs)
        print('func_in 2')
    print('正在装载2')
    return func_in

@func
def test1(a, b, c):
    print("----test-a=%d,b=%d,c=%d---"%(a,b,c))

test1(11,22,33)
'''

'''
# 带返回值
def func(funcx):
    print('正在装载1')

    def func_in():
        print('func_in')
        ret = funcx()  # 保存返回来的hahaha
        print('func_in 2')
        return ret  # 把hahaha返回到39行的调用

    print('正在装载2')
    return func_in


@func
def test1():
    print('test1------')
    return 'hahaha'


ret = test1()
print('test return value is %s' % ret)
'''


# 带参数的装饰器
def func_arg(arg):
    def func(funcx):
        def func_in():
            print('---%s---' % arg)
            funcx()

        return func_in

    return func


@func_arg('haha')
def test1():
    print('-------test1------')


test1()
