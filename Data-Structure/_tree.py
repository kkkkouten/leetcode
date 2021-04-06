#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2021/04/06 11:38

@author: Tei Koten
"""


## Tree 树
# 是一种抽象数据类型，用来莫扭具有树状结构性质的数据集合。
# 性质1：每个节点含有0个或多个子节点。
# 性质2：没有父节点的节点成为根节点
# 性质3：每一个非根节点有且只有一个父节点
# 性质4：除了根节点外，每个子节点可以分为多个不相交的子数

## 数的种类
# -- 无序树
# -- 有序树
#    -- 二叉树：每个节点最多含两个子树的树称为二叉树
#       -- 完全二叉树: 除了底层之外，其余各层的节点的度都为2
#          满二叉树:所有层的节点的度都为2
#       -- 平衡二叉树（AVL树）：当且仅当任何节点的两颗子树的高度差不大于1的二叉树
#       -- 排序二叉树（二叉查找树, Binary Search Tree）：任意根节点的左子树小于根节点，
#                   右子树大于根节点
#    -- 霍夫曼树：
#    -- B树：

## 树的储存与表示
# 1 顺序储存
#  遍历速度有一定优势，但所占空间比较大。
# 2 链式储存
#  常用的储存方式。

# 这次只关注二叉树
# 二叉树的性质
# 性质1：在二叉树的第i层上最多有2^(i-1)个节点(i>0)
# 性质2：深度为k的二叉树最多有2^k-1个节点(k>0)
# 性质3：对于任意一棵二叉树，如果其叶节点树为N0，而度树为2的节点总数为N2，则 N0 = N2 + 1
# 性质4：具有n个节点的完全二叉树的深度必为 log2(n+1)   --> 待定
# 性质5：对完全二叉树，若从上至下，从左至右，则编号为i的节点，其左孩子编号必为2i，
#       其右孩子编号必为2i + 1，其双亲的编号必为 i/2 （i=1时为根，除外）

class Node(object):
    def __init__(self, item):
        self.elem = item
        self.lchild = None  # 左子节点
        self.rchild = None  # 右子节点


class Tree(object):
    """二叉树"""

    def __init__(self):
        self.root = None

    def add(self, item):
        """添加元素"""
        node = Node(item)
        # root为空的操作
        if self.root is None:
            self.root = node
            return
        # root不为空的操作
        queue = [self.root]
        while queue:
            # 取出队头元素
            cur_node = queue.pop(0)
            # 遍历左节点如果为空则添加元素
            # 否则添加至队列
            if cur_node.lchild is None:
                cur_node.lchild = node
                return
            else:
                queue.append(cur_node.lchild)
            # 遍历右节点如果为空则添加元素
            # 否则添加至队列
            if cur_node.rchild is None:
                cur_node.rchild = node
                return
            else:
                queue.append(cur_node.rchild)

    def breadth_travel(self):
        """广度优先遍历"""
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem, end=" ")
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)

    def preorder(self, node):
        """先序遍历"""
        # 根 左 右
        # 利用了递归的方法,
        # 也就是方法里边套方法
        if node is None:
            return
        print(node.elem, end=" ")
        self.preorder(node.lchild)
        self.preorder(node.rchild)

    def inorder(self, node):
        """中序遍历"""
        # 左 根 右
        if node is None:
            return
        self.inorder(node.lchild)
        print(node.elem, end=" ")
        self.inorder(node.rchild)

    def postorder(self, node):
        """中序遍历"""
        # 左 根 右
        if node is None:
            return
        self.postorder(node.lchild)
        self.postorder(node.rchild)
        print(node.elem, end=" ")


if __name__ == "__main__":
    tree = Tree()
    tree.add(0)  # 添加tree的root  tree.root
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    tree.breadth_travel()
    print(" --> 层次遍历")
    tree.preorder(tree.root)
    print(" --> 前序遍历")
    tree.inorder(tree.root)
    print(" --> 中序遍历")
    tree.postorder(tree.root)
    print(" --> 后续遍历")
