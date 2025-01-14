[TOC]

# LeetCode

### 

[面试题 01.01. 判定字符是否唯一](https://leetcode.cn/problems/is-unique-lcci/)

[面试题 01.02. 判定是否互为字符重排](https://leetcode.cn/problems/check-permutation-lcci/)

[面试题 01.06. 字符串压缩](https://leetcode.cn/problems/compress-string-lcci/)

Solution1: 排序

```python
class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        if len(s1) < len(s2): return False
        if sorted(s1) != sorted(s2):return False
        return True
```

Solution2: 哈希表

```python
class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        if len(s1) < len(s2): return False
        map = dict();
        for c1 in s1:
            if c1 not in map:
                map[c1] = 1
            else:
                map[c1] = map[c1] + 1
        for c2 in s2:
            if c2 not in map:
                map[c2] = 1
            else:
                map[c2] = map[c2] - 1
        for val in map.values():
            if val != 0:
                return False
        return True;
```

[面试题 01.04. 回文排列](https://leetcode.cn/problems/palindrome-permutation-lcci/)

### 回文串的结构

一个回文串的特性是它在正反两个方向读起来都是一样的。例如，"racecar" 和 "abba" 都是回文串。

1. **偶数长度的回文串**：所有字符的出现次数必须是偶数。例如，"abba" 由两个 'a' 和两个 'b' 组成。
2. **奇数长度的回文串**：只有一个字符可以出现奇数次，其余字符必须出现偶数次。例如，"racecar" 由两个 'r'，两个 'a'，两个 'c'，和一个 'e' 组成。

```python
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        if not s:
            return False
        map = dict()
        for i in s:
            if i in map:
                map[i] += 1
            else:
                map[i] = 1 
        return sum(1 for count in map.values() if count %2 == 1) <= 1

```





## 链表

###  单项链表

-  [剑指 Offer II 024. 反转链表](https://leetcode.cn/problems/UHnkqh/)

  > 利用三个指针遍历链表。
  >
  > 1. 储存`curr.next`为`next`
  > 2. 改变`curr`指向`prev`
  > 3. 移动`prev`至`curr`并移动`curr`至`next`。

- [876. 链表的中间结点](https://leetcode.cn/problems/middle-of-the-linked-list/)

  > 利用快慢指针两个指针，`fast` `slow`。
  >
  > 1. 循环条件为`fast`和`fast.next`都不为`null`
  >
  > 2. `fast`每次移动两次，`slow`每次移动一次。
  >
  > `fast` 到达链表的末尾时，`slow` 必然位于中间。（可以简单画图证明）

- [剑指 Offer 18. 删除链表的节点](https://leetcode.cn/problems/shan-chu-lian-biao-de-jie-dian-lcof/)





## 树

- [144. 二叉树的前序遍历](https://leetcode.cn/problems/binary-tree-preorder-traversal/)

  > 前序遍历等于深度优先搜索。也就是说会沿着一条路径不断往下搜索直到不能再继续未知，然后在折返至最初的分岔点，开始搜索下一条候补路径。
  >
  > 方法1: 递归
  >
  > 	1. 递归的描述

- [145. 二叉树的后序遍历](https://leetcode.cn/problems/binary-tree-postorder-traversal/)

  > 





一个优秀的工程师不应该只是根据业务逻辑写出业务代码，应该从整体的架构，工作效率等来考虑如何完成业务逻辑比如 cloud的建立。如果发现错误也可以从底层分析。如同建筑师，不应该只考虑房子如何建造好，应该考虑建好房子的基础上如何和周围环境等融合。

> 一个优秀的工程师不仅仅是根据业务逻辑编写代码，还应该从整体架构和工作效率的角度考虑如何完成业务逻辑。例如，云平台的建立。如果发现错误，工程师还应能够从底层进行分析。就像建筑师一样，不仅要考虑房子的建造质量，还要考虑在确保房子建好的基础上，如何与周围环境等融合。





#### 摩尔投票法

摩尔投票法的原理是基于一个简单的观察：在一个数组中，如果一个元素的出现次数超过数组长度的一半，那么它一定是剩余元素中出现次数最多的那个。以下是详细的解释和创建这个算法的过程。

##### 原理

1. **消除配对**：每次选择两个不同的元素，它们彼此互相抵消，直到最后剩下的元素就是出现次数最多的那个元素（如果存在的话）。
2. **候选人选择阶段**：通过不断抵消不同的元素，找到一个可能的多数元素。
3. **验证阶段**：确定这个候选元素是否确实是多数元素。

##### 创建算法的过程

###### 1. 消除配对的思想

我们从数组的第一个元素开始，使用一个计数器来记录当前候选元素的计数。如果当前元素与候选元素相同，增加计数；否则，减少计数。当计数器为零时，选择下一个元素作为新的候选元素。这个过程不断重复，直到遍历完数组。最终剩下的候选元素就是可能的多数元素。

###### 2. 验证阶段

由于候选人选择阶段可能会出现错误的候选人（在某些特殊情况下），我们需要再次遍历数组来确认这个候选元素是否真的出现次数超过一半。

https://leetcode.cn/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof/solutions/138691/mian-shi-ti-39-shu-zu-zhong-chu-xian-ci-shu-chao-3/





