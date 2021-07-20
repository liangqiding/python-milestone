# 使用dict和set
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])
# 放入
d['Adam'] = 67

# 判断key存在
print('Thomas' in d)

# get 获取 避免报错
print(d.get('Thomas'))

# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。

s = set([1, 2, 3])
