import os

print('\n操作系统类型',os.name)


# print('操作系统详细信息（win不可用）',os.uname())

print('\n环境变量',os.environ)

print('\n单个环境变量',os.environ.get('PATH'))

# 操作文件和目录

print('\n查看当前目录的绝对路径：',os.path.abspath('.'))

# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
thisPath = os.path.abspath('.').strip()
newPath = os.path.join(thisPath, 'testdir')
# 然后创建一个目录:
os.mkdir(newPath)
# 删掉一个目录:
os.rmdir(newPath)


