# class Cat(object):
#     age = '10'
#
#     def __init__(self):
#         self.age = 9
#
#     # 静态方法 staticmethod
#     @staticmethod
#     def print_age(age):
#         print(f"Cat's age is {age}")
#
#     # 类方法 classmethod
#     @classmethod
#     def get_age1(cls, age):
#         print(cls.age)
#         print(age)
#
#     # 成员方法 method
#     def get_age2(self, age):
#         print(self.age)
#         print(age)
#
#
# cat = Cat()
# print(cat.print_age(1))
# print(cat.get_age1(9))
# print(cat.get_age2(2))

res = []


def fun(data) -> list:
    if isinstance(data, list):
        for i in range(len(data)):
            # res.append([f'{i}'] * len(data[i]) if data[i] else 0)
            if data[i] == None:
                continue
            for j in range(len(data[i])):
                res.append(f'{i}')
            # [res.append([f'{i}']) for _ in range(len(data[i]) if data[i] else 0)]
                fun(data[i])
    elif isinstance(data, dict):
        for i in range(len(data)):
            if res:
                res.append(list(data.keys())[i])
            else:
                res.append(list(data.keys())[i])
            fun(data[list(data.keys())[i]])
    # elif data == None:
    # res.pop(-1)
    # return []
    elif isinstance(data, str):
        res[-1] = (res[-1], data)
        return res


data = [
    {
        "general": {
            "icon": "这个字段为必填项"
        },
        "roles": [
            None,
            {
                "name": "这个字段不能为空",
                "label": "这个字段不能为空"
            }
        ],
        "settings": "这个字段为必填项"
    }
]
fun(data)
print(res)
