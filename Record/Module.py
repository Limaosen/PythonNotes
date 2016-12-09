#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
'''
1、Python中，一个.py文件就称之为一个模块（Module）
    举个例子，一个abc.py的文件就是一个名字叫abc的模块
    （1）自己创建模块时要注意命名，不能和Python自带的模块名称冲突。例如，系统自带了sys模块
2、包（Package）（为了避免模块名冲突），按目录来组织模块的方法
    （1）只要顶层的包名不与别人冲突，那所有模块都不会与别人冲突，abc.py模块的名字就变成了mycompany.abc
    （2）每一个包目录下面都会有一个__init__.py的文件，这个文件是必须存在的，否则，Python就把这个目录当成普通目录，而不是一个包。
        __init__.py可以是空文件，也可以有Python代码，因为__init__.py本身就是一个模块，而它的模块名就是mycompany
3、import
    （1）import后面直接跟模块名，如果是系统自带的模块，不管在哪里都可以直接输入import +...
    （2）如果你要调用你自己写的模块
        A：需要将该模块放置于你的工作目录下
        B:  import sys
            sys.path.append('存放模块的路径') #告诉python解释器，我写得那个文件在哪里，然后你后面就可以调用你写的模块了
3、查询内置函数 https://docs.python.org/3/library/functions.html
4、萌13131313 关于__init__.py 的解释（http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014318447437605e90206e261744c08630a836851f5183000）
'''
import os
