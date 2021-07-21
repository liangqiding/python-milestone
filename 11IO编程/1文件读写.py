# 标示符'r'表示读，这样，我们就成功地打开了一个文件。
file = 'test.txt'

try:
    f = open(file, 'r', encoding="utf-8")
    print(f.read())
finally:
    if f:
        f.close()
print('\n')

# 简写形式 with表达式其实是try-finally的
with open(file, 'r', encoding="utf-8") as f:
    print(f.read())
print('\n')

# 按大小读取
with open(file, 'r', encoding="utf-8") as f:
    print(f.read(10))
print('\n')

# 读取一行
with open(file, 'r', encoding="utf-8") as f:
    print(f.readline())
print('\n')

# 读取成list
with open(file, 'r', encoding="utf-8") as f:
    print(f.readlines())
print('\n')

# 二进制文件
with open(file, 'rb') as f:
    print(f.read())
print('\n')

# 写文件
msg = '1. 第一行\n2. 第二行\n3. 第三行\n4. 第四行'
with open(file, 'w',encoding="utf-8") as f:
    f.write(msg)