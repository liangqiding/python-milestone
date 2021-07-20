# 使用list和tuple

# Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
print(len(classmates))
print(classmates[0])
# 取倒数
print(classmates[-1])
print(classmates[-2])
classmates.insert(1, 'Jack')
# 要删除list末尾的元素，用pop()方法：
classmates.pop()
# 要删除指定位置的元素，用pop(i)方法
classmates.pop(1)

# tuple 元组tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改，比如同样是列出同学的名字：
tuple = ('Michael', 'Bob', 'Tracy')


