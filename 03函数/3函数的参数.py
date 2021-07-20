# 默认参数
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(power(5))
print(power(5,3))
print('\n')

# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
person("lqd",18,msg='普通写法', job='Engineer')
# 简化写法
extra = {'msg': '简化写法', 'job': 'Engineer'}
person('Jack', 24, **extra)
print('\n')

# 对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。至于到底传入了哪些，就需要在函数内部通过kw检查。
def person2(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('关键字参数：name:', name, 'age:', age, 'other:', kw)

extra = {'msg': '简化写法', 'job': 'Engineer'}
person2('Jack', 24, **extra)
print('\n')

# 可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print('可变参数',calc(1, 2, 3))
print('\n')