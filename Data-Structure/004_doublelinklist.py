#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2021/02/19 22:36

@author: Tei Koten
"""


class Node(object):
    """定义节点"""
    def __init__(self, elem):
        self.elem = elem
        self.next = None
        self.prev = None


class DoubleLinkList(object):
    """singlelinklist"""

    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        """链表是否为空"""
        return self.__head is None

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
        node.next.prev = node

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
            node.prev = cur

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

if __name__=="__main__":

    node1 = Node(2)
    node2 = Node(5)
    node3 = Node(9)
    print(node1.prev)
    node1.next = node2.prev
    print(node1.next)





