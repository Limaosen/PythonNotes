#!/usr/bin/python
# -*- coding: utf-8 -*-
'''多个构造函数还没学完'''
class Student(object):  # python3的类class(object)括号中的object可以不用写
    '''
    java的this是隐式的，它就叫this。
    python的self是显式的，以形参的身份出现，你写成this，itself也没问题。
    '''

    def __init__(self, name, score):#
        self.name = name#不像java一样 变量还得写成全局那样别的地方才能调用，print_score直接就可以用
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))
Bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
Bart.print_score()
lisa.print_score()
lisa2 = Student("adasf")
lisa2.print_score()
print(Bart.score)#直接打印student得属性值
Bart2 = Student('Bart Simpson3', 593)
Bart2.age = 1.08 #和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同
print('aaaa:',Bart2.age)
print('aaaa2:',Bart2.print_score())
"""
class Student:
    def init(self,name,score):
        self.name = name
        self.score= score
    def print_score(self):
        print('%s:%s' % (self.name,self.score))
实例化和调用：
>>> std1 = Student()
>>> std1.init('Ian',96)
>>> std1.print_score()
Ian:96

这种写法的init就是一个普通的赋值方法，不能叫做实例化。没实例化student之前还不能调用（那当然），而且实例化之后可以多次调用。

而__init__ 是实例化方法（构造方法），在实例化student的时候自动调用，之后就不再调用（对这个已经实例化的对象来说）。
"""

