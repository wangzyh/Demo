# 1.
# def sing(class_):
#     instances = {}
#
#     def getinstance(*args, **kwargs):
#         if class_ not in instances:
#             instances[class_] = class_(*args, **kwargs)
#         return instances[class_]
#
#     return getinstance()
#
#
# @sing
# class MyClass(object):
#     pass

# 2.
# class Sing(object):
#     instances = None
#     def __new__(cls, *args, **kwargs):
#         if not isinstance(cls.instances, cls):
#             cls.instances = object.__new__(cls)
#         return cls.instances
#
# class MyClass(Sing):
#     pass

# 3.
class Sing(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Sing, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class MyClasss(object, metaclass=Sing):
    pass
