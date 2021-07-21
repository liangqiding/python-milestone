# 转int
int('12345')
# 16转10
int('12345', 16)

# functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2：
import functools
int2 = functools.partial(int, base=2)
int2('1000000')
int2('1010101')
max2 = functools.partial(max, 10)
max2(5, 6, 7)
