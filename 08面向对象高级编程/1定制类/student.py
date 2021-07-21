class Student(object):
    # 用tuple定义允许绑定的属性名称
    __slots__ = ('name', 'age', 'pt')

    def set_pt(self, pt):
        self.pt = pt
    # 可以直接实例()调用

    def __call__(self):
        print('My name is %s.' % self.name)

    # 注意，只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找。
    def __getattr__(self, attr):
        if attr == 'age':
            return 25
        raise AttributeError(
            '\'Student\' object has no attribute \'%s\'' % attr)


s = Student()
s.name = 'Michael'
print(s.name)
# 配置方法


def printMsg(x):
    print(x)


# 动态绑定方法
s.set_pt(printMsg)

s.pt(111)

# 直接实例()调用
s()

# 调用没有的属性
print('调用没有的属性:',s.age)
