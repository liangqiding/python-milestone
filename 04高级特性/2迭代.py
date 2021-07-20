# 迭代

d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
  print(key)

# 判断是否可迭代
from collections.abc import Iterable
print('判断是否可迭代:',isinstance(d, Iterable) )

# Python内置的enumerate函数可以把一个list变成索引-元素对
for i, value in enumerate(['A', 'B', 'C']):
   print(i, value)

