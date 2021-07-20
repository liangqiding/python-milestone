# 以Python内置的求绝对值的函数abs()为例，调用该函数用以下代码：
from functools import reduce
print('请绝对值：', abs(-10))

# 传入函数


def add(x, y, f):
    return f(x) + f(y)


print('传入函数：', add(-5, 6, abs))

# Python内建了map()和reduce()函数。


def f(x):
    return x * x


r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])

print('map：', list(r))

# 转str
r = list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))

print('转str:', r)


# 再看reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：


def add(x, y):
    return x + y


r = reduce(add, [1, 3, 5, 7, 9])

print('求和:', r)

# filter
def is_odd(n):
    return n % 2 == 1

r = list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))

print('过滤:', r)

def not_empty(s):
    return s and s.strip()

print(not_empty('s'))

# Python内置的sorted()函数就可以对list进行排序：
r = sorted([36, 5, -12, 9, -21], key=abs)
print('排序:', r)