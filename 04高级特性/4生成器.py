# 生成器：generator

# 要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：
L = [x * x for x in range(10)]
print('list:', L)
g = (x * x for x in range(10))
print('generator:', g)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print('\n')

# 斐波拉契数列演示yield


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

g = fib(6)

while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
         print('Generator return value:', e.value)
         break
