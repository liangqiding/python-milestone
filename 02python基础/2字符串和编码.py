# 字符串和编码

# 对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符：
print(ord('A'))
print(ord('中'))
print(chr(66))
print(chr(25991))
print('\n')

# Python对bytes类型的数据用带b前缀的单引号或双引号表示：
print(b'ABC')
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))
print('\n')

# 如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节：
msg =  b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore')
print('忽略错误的字节输出：',msg)
print('\n')

# 要计算str包含多少个字符，可以用len()函数：
print(len('ABC'))
print(len('好的'))
print(len(b'ABC'))
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
print(len('中文'.encode('utf-8')))
print('\n')

# 在Python中，采用的格式化方式和C语言是一致的，用%实现，举例如下：%d整数,%f浮点数,%s字符串,%x十六进制整数
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)