#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2021/03/10 19:28

@author: Tei Koten
"""

# binary search
# 条件：递增数组
# 时间复杂度：O(logN)
# 1D array 查找第一个，查找最后一个，与某个数最近
# 2D array 查找某个数时候在其中

def findFirstPosition(nums, target):
    """查找第一个等于目标值的索引"""
    if len(nums) == 0:
        return -1
    start, end = 0, len(nums) - 1
    while (start + 1 < end):
        mid = start + (end - start) // 2
        # first == end
        if (nums[mid] >= target):
            end = mid
        else:
            start = mid
    # 因此查找第一个是否等于所以最后的判断条件位end 和 start
    # 是否等于目标值
    if nums[start] == target:
        return start
    if nums[end] == target:
        return end
    return -1



def findLastPosition(nums, target):
    """查找最后一个等于目标的索引"""
    if len(nums) == 0:
        return -1
    start, end = 0, len(nums) - 1
    while start + 1 < end:
        mid = start + (end - start) // 2
        # last == start
        if nums[mid] <= target:
            start = mid
        else:
            end = mid
    # 因此查找最后一个是否等于所以最后的判断条件位end 和 start
    # 是否等于目标值
    if nums[end] == target:
        return end
    if nums[start] == target:
        return start
    return -1


def sqrt(x):
    """计算x的平方根"""
    # 思想：找到某个数k其 k**2 <= target
    # 也就是说某个整数 k**2 最接近 x
    # 转换成 查找最后一个与target相同的数的索引 的解题思想
    start, end = 0, x
    while start + 1 < end:
        # 这一步与 start + (end - start)//2 是一样的
        mid = start + (end - start) // 2
        if mid * mid >= x:
            end = mid
        else:
            start = mid
    if start * start == x:
        return start
    if end * end == x:
        return end
    # 因为last 是 start 所以返回 start
    return start


def searchMatrix(matrix, target):
    # 判断 [] 和 [[]] 这两种特殊情况
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return False
    # 一般情况
    m, n = len(matrix), len(matrix[0])
    l = m * n
    start, end = 0, l - 1
    while start + 1 < end:
        mid = start + (end - start) // 2
        # 一维数组书的二维坐标形式。
        x, y = mid // n, mid % n
        if matrix[x][y] == target:
            return True
        elif matrix[x][y] < target:
            start = mid
        else:
            end = mid
    if matrix[start // n][start % n] == target:
        return True
    if matrix[end // n][end % n] == target:
        return True
    return False




def searchInsertPosition(nums,target):
    """搜索插入位置"""
    # 按照原始数组的顺序，返回target的插入位置
    # 其思想为找到第一个数字大于等于目标值
    if len(nums) == 0:
        return len(nums)
    start, end = 0, len(nums)-1
    while start + 1 < end:
        mid = start + (end - start) // 2
        # first == end
        if nums[mid] >= target:
            end = mid
        else:
            start = mid
    # 其思想为找到第一个数字大于等于目标值
    if nums[start]  >= target:
        return start
    if nums[end] >= target:
        return end
    # 因为如果超出数组的最大值则返回数组的最后一位
    # 其实只要比数组长度大用insert都可以插入最后一位
    return len(nums)


def countOfSmallerNumber(A, queries):
    """"""
    def searchLastPosition(A, target):
        if len(A) == 0 or target == None:
            return len(A)
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if A[mid] >= target:
                end = mid
            else:
                start = mid
        if A[start] >= target:
            return start
        if A[end] >= target:
            return end
        return end
    res = []
    A.sort()
    for target in queries:
        ind = searchLastPosition(A, target)
        res.append(ind)
    return res

def searchRange(A, target):
    # write your code here
    if len(A) == 0:
        return [-1, -1]
    # 首先寻找First
    start, end = 0, len(A) - 1
    while start + 1 < end:
        mid = (end + start) // 2
        if A[mid] >= target:
            end = mid
        else:
            start = mid
    # 此时的判断顺序很重要
    # 第一次寻找的first所以先判断start
    # 因为有可能A全为一样的
    if A[start] == target:
        first = start
    elif A[end] == target:
        first = end
    else:
        first = -1
    # 寻找Last
    start, end = 0, len(A) - 1
    while start + 1 < end:
        mid = (end + start) // 2
        if A[mid] <= target:
            start = mid
        else:
            end = mid
    # 第二次寻找last，所以先判断end
    if A[end] == target:
        last = end
    elif A[start] == target:
        last = start
    else:
        last = -1
    return [first, last]



if __name__ == "__main__":
    #
    nums = [5, 7, 8, 9, 10, 10, 10, 10, 14, 19]

    # 457.经典二分法
    print(findFirstPosition(nums, 10))

    # 经典二分法
    print(findLastPosition(nums,10))

    # 141.对x开根
    print(sqrt(12))

    # 28.搜索二维数组
    print(searchMatrix([[3]], 3))

    # 60.搜索插入位置
    searchInsertPosition(nums,43)

    # 248.统计比给定整数小的数的个数
    A = [55,81,56,91,35,92,10,53,27,94,64,45,19,44,52,19,79,12,16,90,97,33,73,2,20,68,19,7,17,62,45,48,62,26,85,4,63,67,56,16]
    A.sort()
    queries = [10,43,2,17,28,75,75,12]
    countOfSmallerNumber(A, queries)

    # 61.搜索区间
    searchRange(A,19)



