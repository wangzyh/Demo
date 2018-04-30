# -*- Coding:utf-8 -*-


def upper_attr(future_class_name, future_class_parents, future_class_attr):

    # 遍历属性字典，把不是__开头的属性名字变为大写
    newattr = {}
    for name, value in future_class_attr.items():
        if not name.startswith("__"):
            newattr[name.upper()] = value

    # 调用type来创建一个类
    return type(future_class_name, future_class_parents, newattr)


class Foo(object, metaclass=upper_attr):
    bar = 'bip'


print(hasattr(Foo, 'bar'))
print(hasattr(Foo, 'BAR'))