# 首先，我们尝试把一个对象序列化并写入文件：
import pickle
d = dict(name='Bob', age=20, score=88)
serialization = pickle.dumps(d)
print('序列化',serialization)