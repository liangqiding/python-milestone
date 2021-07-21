# 首先，我们尝试把一个对象序列化并写入文件：
import json
import pickle

d = dict(name='Bob', age=20, score=88)
# pickle.dumps()方法把任意对象序列化成一个bytes
serialization = pickle.dumps(d)
print('序列化', serialization)

# pickle.loads()方法反序列化出对象
obj = pickle.loads(serialization)

print('反序列化', obj)


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob', 20, 88)

def student2dict(std):
        return {
            'name': std.name,
            'age': std.age,
            'score': std.score
        }

print('序列化对象：',json.dumps(student2dict(s)))
