#!/usr/bin/python3
# Filename: test.py

# 导入模块
from student import Student

# 现在可以调用模块里包含的函数了
s = Student('公共变量111', 59)
s.print_score()
print('访问公共变量：', s.name)
print('访问私有变量：', s.get_value())
print('访问类属性：', s.msg)
homework = s.get_homework()
print("多态继承：", homework)

print('获取对象信息：',type(s))

print('获取对象所有方法：',dir(s))

