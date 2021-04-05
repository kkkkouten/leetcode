#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2021/02/21 23:24

@author: Tei Koten
"""


class SortAlgorithm:
    """所有的排序算法"""

    def bubble_sort(self, alist):
        """冒泡排序"""
        # 最优时间复杂度 O(n)
        # 最坏时间复杂度 O(n**2)
        # 稳定性：稳定
        n = len(alist)
        for j in range(n - 1):
            count = 0  # 优化算法
            for i in range(n - 1 - j):
                if alist[i] > alist[i + 1]:
                    alist[i], alist[i + 1] = alist[i + 1], alist[i]
                    count += 1
            if 0 == count:
                # 遍历整个列表如果交换证明无序，count不为0
                # 如果无交换证明有序，count为 0
                # 因此此时最优复杂度为O(n)
                return alist
        # # Method.2
        # # 也可以写为
        # n = len(alist)
        # # 反向遍历的方法
        # for j in range(n-1,0,-1):
        #     for i in range(j):
        #         if alist[i] > alist[i + 1]:
        #             alist[i], alist[i + 1] = alist[i + 1], alist[i]
        return alist

    def select_sort(self, alist):
        """选择排序"""
        # 最优时间复杂度 O(n**2)
        # 最坏时间复杂度 O(n**2)
        # 稳定性：不稳定
        n = len(alist)
        for j in range(n - 1):
            min_index = j
            for i in range(j + 1, n):
                if alist[min_index] > alist[i]:
                    min_index = i
            # 交换两个位置的元素
            alist[j], alist[min_index] = alist[min_index], alist[j]
        return alist

    def insert_sort(self, alist):
        """插入算法"""
        # 最优时间复杂度 O(n)
        # 最坏时间复杂度 O(n**2)
        # 稳定性：稳定
        n = len(alist)
        for i in range(1,n):
            for j in range(i,0,-1):
                if alist[j] < alist[j-1]:
                    alist[j],alist[j-1] = alist[j-1], alist[j]
                else:
                    break
        return alist
        # # Method.2
        # # 用while 实现
        # n = len(alist)
        # for j in range(1,n):
        #     # i,j 代表内层循环起始值(反向循环)
        #     i = j
        #     # 执行从右边的无序序列中取出第一个元素。
        #     while i > 0:
        #         if alist[i] < alist[i-1]:
        #             alist[i],alist[i-1] = alist[i-1],alist[i]
        #             i -= 1
        #         else:
        #             break
        # return alist

    def shell_sort(self,alist):
        """希尔排序"""
        # 最优时间复杂度 O(n**1.3)
        # 最坏时间复杂度 O(n**2)  即gap=1是 变成 插入排序
        # 稳定性：不稳定
        n = len(alist)
        gap = n//2
        # gap变化到0之前，插入算法执行的次数
        while gap > 0:     # 希尔排序与插入算法的区别就是gap的步长
            for j in range(gap,n):
                # Q：为什么从gap-n
                # 将无序序列按照gap的索引在草稿纸上列出子序列，则可观察出原因。
                i = j
                while i > 0:
                    if alist[i] < alist[i-gap]:
                        alist[i], alist[i-1] = alist[i-1], alist[i]
                        i -= gap # 向子序列前一位移动
                    else:
                        break
            # 缩短gap步长
            gap //= 2
        return alist

    def quick_sort(self,alist):
        """快速排序"""
        # 最优时间复杂度 O(n**1.3)
        # 最坏时间复杂度 O(n**2)  即gap=1是 变成 插入排序
        # 稳定性：不稳定
        n = len(alist)
        mid = alist[0]
        low = 0
        high = n - 1
        while low < high:
            if alist[low] > mid or alist[high] < mid:
                alist[low], alist[high] = high,






if __name__ == "__main__":
    # 冒泡排序
    li = [53, 26, 93, 17, 77, 31, 44, 55, 20]
    Sort = SortAlgorithm()
    print(Sort.bubble_sort(li))

    # 选择排序
    li = [53, 26, 93, 17, 77, 31, 44, 55, 20]
    Sort = SortAlgorithm()
    print(Sort.select_sort(li))

    # 插入排序
    li = [53, 26, 93, 17, 77, 31, 44, 55, 20]
    Sort = SortAlgorithm()
    print(Sort.insert_sort(li))

    # 希尔排序
    li = [53, 26, 93, 17, 77, 31, 44, 55, 20]
    Sort = SortAlgorithm()
    print(Sort.shell_sort(li))

    # 快速排序
    li = [53, 26, 93, 17, 77, 31, 44, 55, 20]
    Sort = SortAlgorithm()
    print(Sort.quick_sort(li))



