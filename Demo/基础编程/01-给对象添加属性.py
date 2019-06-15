class Person(object):
    def __init__(self, newName, newAge):
        self.name = newName
        self.age = newAge


laowang = Person('laowang', 19)
print(laowang.name)
print(laowang.age)
laowang.addr = 'henan'
print(laowang.addr)

laozhao = Person('老赵', 100)
# laozhao.addr('hebei')

Person.num = 100
print(laowang.num)
print(laozhao.num)
