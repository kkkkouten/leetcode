#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2021/04/05 23:38

@author: Tei Koten
"""


# Queue 队列 (First In First Out, FIFO)
# 特点：只允许在一端进行插入操作，而在另一端进行删除操作的线性表


# 队列的操作
# Queue() 创建一个新的空栈
# enqueue(item) 添加一个新的元素item到队列中
# dequeue() 从队列头部删除一个元素
# is_empty() 判断队列是否为空
# size() 返回队列的元素个数

class Queue(object):
    """队列"""

    def __init__(self):
        """顺序表构建容器"""
        self.__list = list()

    def enqueue(self, item):
        """添加一个新的元素item到队列中"""
        self.__list.append(item)

    def dequeue(self):
        """从队列头部删除一个元素"""
        return self.__list.pop(0)

    def is_empty(self):
        """判断队列是否为空"""
        return not self.__list

    def size(self):
        """返回队列的元素个数"""
        return len(self.__list)


if __name__ == "__main__":

    s = Queue()
    s.enqueue(1)
    s.enqueue(2)
    s.enqueue(3)
    s.enqueue(4)
    print(s.dequeue())
    print(s.dequeue())
    print(s.dequeue())
    print(s.dequeue())

