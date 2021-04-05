#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2021/04/05 22:53

@author: Tei Koten
"""


# stack 栈 （Last In First Out, LIFO）
# 定义：是一种容器，可以存入数据元素，访问元素，删除元素
# 特点：只允许在容器的Top端进行加入数据(push)和输出数据(pop)
# 优点：没有了位置概念，保证任何时候可以访问、删除的元素都是此铅最后存入的那个元素
#      确认了一种默认的访问顺序

# 栈的操作
# Stack() 创建一个新的空栈
# push(item) 添加一个新的元素item到栈顶
# pop() 弹出栈顶元素
# peak() 返回栈顶元素
# is_empty() 判断栈是否为空
# size() 返回栈的元素个数


class Stack(object):
    """栈"""
    def __init__(self):
        self.__list = list()

    def push(self, item):
        """添加一个新的元素item到栈顶"""
        # 栈顶可以是list的顶端也可以是尾端
        # 但接下来的方法需要一致
        # 如果使用顺序表储存元素 选择 尾端，因为顺序表的时间复杂度为O(1)
        # 如果使用单链表储存元素 选择 首端，因为顺单链表的时间复杂度为O(1)
        self.__list.append(item)       # 尾端
        # self.__list.insert(0, item)  # 首段

    def pop(self):
        """弹出栈顶元素"""
        return self.__list.pop()

    def peak(self):
        """返回栈顶元素"""
        if self.__list:
            return self.__list[-1]
        return None

    def is_empty(self):
        """判断栈是否为空"""
        # return self.__list ==[]
        # 与下边是一样的意思
        return not self.__list

    def size(self):
        """返回栈的元素个数"""
        return len(self.__list)

if __name__=="__main__":

    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())



