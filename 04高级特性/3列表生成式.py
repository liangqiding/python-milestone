# 列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。

# 举个例子，要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用list(range(1, 11))：
print('生成1-10：',list(range(1, 11)))

# 带if
arr = [x * x for x in range(1, 11) if x % 2 == 0]
print('带if:',arr)

# 2层
arr = [m + n for m in 'ABC' for n in 'XYZ']
print('2层:',arr)

# 导入os模块，模块的概念后面讲到
import os 
arr = [d for d in os.listdir('.')] # os.listdir可以列出文件和目录
print('目录结构：',arr)

# for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value：
d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k, v in d.items():
    print(k, '=', v)

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s for s in L1 if s!=None and s!=18 ]
print(L2)

