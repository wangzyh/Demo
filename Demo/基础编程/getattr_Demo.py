class Foo(object):
    def __init__(self):
        pass

    def __getattr__(self, item):
        print(item, end=" ")
        return self

    def __str__(self):
        return ""


print(Foo().think.different.itcast)
