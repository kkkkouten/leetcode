#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2021/02/18 14:45

@author: Tei Koten
"""


## 单链表的实现

class Node(object):
    """Node"""

    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleLinkList(object):
    """单向链表"""

    def __init__(self, node=None):
        """链表节点"""
        self.__head = node

    def is_empty(self):
        """链表是否为空"""
        return self.__head == None

    def length(self):
        """"""
        # cur游标用来移动遍历节点
        cur = self.__head
        # 计数器
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        cur = self.__head
        while cur != None:
            print(cur.elem, end=" ")
            cur = cur.next

    def add(self, item):
        """链表头部添加元素"""
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        """链表尾部添加元素"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        """"""
        if pos <= 0:
            self.add(item)
        elif pos > self.length() - 1:
            self.append(item)
        else:
            node = Node(item)
            pre = self.__head
            count = 0
            while count < (pos - 1):
                count += 1
                pre = pre.next
            # 当循环结束时，pre指向pos-1
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        """删除链表结点"""
        cur = self.__head
        pre = None
        while cur != None:
            if cur.elem == item:
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def search(self, item):
        """搜索链表结点"""
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False


if __name__ == "__main__":
    singlelinklist = SingleLinkList()

    singlelinklist.append(1)
    singlelinklist.append(23)
    singlelinklist.append(13)
    singlelinklist.append(11)
    singlelinklist.append(45)
    singlelinklist.add(8)
    singlelinklist.insert(3, 3)
    # 此时 列表为  8 1 23 3 13 11 45
    singlelinklist.search(23)  # 查找的是第一个与目标相同的元素
    singlelinklist.remove(1)

    print(singlelinklist.length())
    print(singlelinklist.travel())

