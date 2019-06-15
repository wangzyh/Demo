class Itcast(object):
    def __init__(self, subject1):
        self.subject1 = subject1
        self.subject2 = "cpp"

    # 属性访问时拦截器,打log
    def __getattribute__(self, obj):
        print("----1>%s" % obj)
        if obj == 'subject1':
            print('log subject1')
            return 'reditrct python'
        else: # 测试时注释掉这两行，将找不到subject2
            temp = object.__getattribute__(self, obj)
            print("----2>%s"%str(temp))
            return temp

    def show(self):
        print('this is Itcast')


s = Itcast("python")
print(s.subject1)
print(s.subject2)

s.show()
