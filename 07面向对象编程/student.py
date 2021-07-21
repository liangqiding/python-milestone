#!/usr/bin/python3


from teacher import Teacher


class Student(Teacher):
     # 类属性
    msg = 'Student'
    # 以__(2)开头，就变成了一个私有变量（private）

    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.__value = '私有变量123'

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_value(self):
        return self.__value
