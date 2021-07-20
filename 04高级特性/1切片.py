# 取一个list或tuple的部分元素是非常常见的操作。比如，一个list如下：
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print('取前三个:', L[0:3])
print('第1-3个:', L[1:3])
print('倒数第2个开始:', L[-2:])

# 自定义去除空格函数

def trim(s):
    flag = 0
    if s[:1] == ' ':
        flag = 1
        s = s[1:]
    if s[-1:] == ' ':
        flag = 1
        s = s[:-1]
    if flag == 1:
       return trim(s)
    else:
        return s
print('自定义去除空格函数:',trim('  f   '))
