#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2021/04/05 23:53

@author: Tei Koten
"""


# 双端队列 (deque, double-ended-queue)
# 定义：是一种具有队列和栈的性质的数据结构
# 特点：1.双端队列中的元素可以从两端弹出，其限定插入和删除操作在表的两端进行。
# 特点：2.双端队列可以在队列任意一端入队和出队。

# 操作
# Deque()           创建一个空的双端队列
# add_front(item)   从队头加入一个item元素
# add_rear(item)    从队尾加入一个item元素
# remove_front()    从队头删除一个item元素
# remove_rear()     从队尾删除一个item元素
# is_empty()        判断双端队列是否为空
# size()            返回队列的大小

class Deque(object):

    def __init__(self):
        self.__list = list()

    def add_front(self, item):
        """从队头加入一个item元素"""
        self.__list.insert(0, item)

    def add_rear(self, item):
        """从队尾加入一个item元素"""
        self.__list.append(item)

    def pop_front(self):
        """从队头删除一个item元素"""
        return self.__list.pop(0)

    def pop_rear(self):
        """从队尾删除一个item元素"""
        return self.__list.pop()

    def is_empty(self):
        """判断双端队列是否为空"""
        return not self.__list

    def size(self):
        """返回队列的大小"""
        return len(self.__list)

if __name__ == "__main__":

    s = Deque()
    s.add_front(1)
    s.add_front(2)
    s.add_rear(3)
    s.add_rear(4)
    print(s.pop_front())
    print(s.pop_rear())
    print(s.is_empty())
    print(s.size())
