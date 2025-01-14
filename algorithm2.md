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



## 位运算（bitwise operations，ビット演算）

位运算是一种直接操作二进制位的计算机编程技术。通过对数据的二进制表示的各个位进行操作来执行特定的数学运算或逻辑操作。这些操作通常在底层硬件级别上执行，因此能够高效地处理大量数据，特别是在需要高性能和低资源消耗的场景下非常有用

#### 常见的位运算操作包括：

1. **按位与 (AND)**：对应位都为1时，结果才为1。

   示例：`5 & 3` 的二进制运算是 `0101 & 0011`，结果是 `0001`，即1。

2. **按位或 (OR)**：只要有一个对应位为1，结果就为1。

   示例：`5 | 3` 的二进制运算是 `0101 | 0011`，结果是 `0111`，即7。

3. **按位异或 (XOR)**：对应位不同，结果为1；相同则为0。

   示例：`5 ^ 3` 的二进制运算是 `0101 ^ 0011`，结果是 `0110`，即6。

4. **按位取反 (NOT)**：每个位取反，即0变1，1变0。

   示例：`~5` 的二进制运算是 `~0101`，结果是 `1010`，在Python中按位取反会取反所有位，包括符号位，因此结果是负数。

5. **左移 (Left Shift)**：将二进制位向左移动，右侧补0。

   示例：`5 << 1` 的二进制运算是 `0101 << 1`，结果是 `1010`，即10。

6. **右移 (Right Shift)**：将二进制位向右移动，左侧补0或补符号位（算术右移）。

   示例：`5 >> 1` 的二进制运算是 `0101 >> 1`，结果是 `0010`，即2。

#### 应用场景：

- **位掩码**：通过位运算可以快速设置或检查数据的特定位状态，如在权限控制中使用。
- **优化算法**：某些算法利用位运算来提高效率，例如位图算法。
- **嵌入式系统**：在资源受限的嵌入式设备中，位运算常用于节省内存和提高速度。
- **密码学**：一些加密算法使用位运算来进行数据处理和转换。







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

### 定义

树（Tree）是一种**非线性**的数据结构，由**节点（nodes）**和**边（edges）**组成。它具有以下特点：

- **节点**：每个元素称为一个节点。一个节点包含数据和指向子节点的指针。
- **根节点（Root Node）**：树中的顶层节点称为根节点，树从根节点开始。
- **边（Edges）**：连接两个节点的线条称为边。每条边都将一个父节点连接到其子节点。
- **子节点（Child Node）**：与某个节点相连的节点称为该节点的子节点。
- **父节点（Parent Node）**：具有子节点的节点称为父节点。
- **叶节点（Leaf Node）**：没有子节点的节点称为叶节点或终端节点。
- **深度（Depth）**：从根节点到某一节点的边的数量称为该节点的深度。
- **高度（Height）**：从某个节点到叶节点的最长路径称为该节点的高度。
- **路径（Path）**：从一个节点到另一个节点经过的节点序列称为路径。

### 常见种类：

- **二叉树（Binary Tree）**：每个节点最多有两个子节点。
- **平衡二叉树（Balanced Binary Tree）**：左右子树的高度差不超过1的二叉树。
- **二叉搜索树（Binary Search Tree, BST）**：左子树的所有节点值小于根节点值，右子树的所有节点值大于根节点值。
- **完全二叉树（Complete Binary Tree）**：除最后一层外，每一层的节点都是满的，最后一层的节点从左到右依次排列。
- **满二叉树（Full Binary Tree）**：每个节点要么有0个子节点，要么有2个子节点。
- **平衡树（Balanced Tree）**：子树的高度差不会太大，常见如红黑树、AVL树等。

树在计算机科学中广泛应用于表示层次结构、文件系统、HTML DOM等。

-----

### 二叉树的实现

```python
class TreeNode:
    def __init__(self, value):
        self.value = value  # 节点的值
        self.left = None    # 左子节点
        self.right = None   # 右子节点

# 创建一个树
root = TreeNode(1)           # 创建根节点
root.left = TreeNode(2)      # 创建左子节点
root.right = TreeNode(3)     # 创建右子节点
root.left.left = TreeNode(4) # 创建左子节点的左子节点
root.left.right = TreeNode(5)# 创建左子节点的右子节点
```

### 二叉树的遍历方式

1. **前序遍历（Pre-order Traversal）**: 根 -> 左 -> 右
2. **中序遍历（In-order Traversal）**: 左 -> 根 -> 右
3. **后序遍历（Post-order Traversal）**: 左 -> 右 -> 根
4. **层次遍历（Level-order Traversal）**: 按层从上到下，从左到右遍历节点。



```
        a
       / \
      b   c
     / \   \
    d   e   f
   /
  g
 / 
h
```



#### 前序遍历实现

前序遍历的顺序是：**根 -> 左子树 -> 右子树**

```python
def pre_order(node):
    if node:
        print(node.value)    # 访问根节点
        pre_order(node.left) # 递归访问左子树
        pre_order(node.right)# 递归访问右子树

# 调用前序遍历
pre_order(root)
# a, b, d, g, h, e, c, f
```

#### 中序遍历实现

中序遍历的顺序是：**左子树 -> 根 -> 右子树**

```python
def in_order(node):
    if node:
        in_order(node.left)  # 递归访问左子树
        print(node.value)    # 访问根节点
        in_order(node.right) # 递归访问右子树

# 调用中序遍历
in_order(root)
# h, g, d, b, e, a, c, f
```

#### 后序遍历实现

后序遍历的顺序是：**左子树 -> 右子树 -> 根**

```python
def post_order(node):
    if node:
        post_order(node.left)  # 递归访问左子树
        post_order(node.right) # 递归访问右子树
        print(node.value)      # 访问根节点

# 调用后序遍历
post_order(root)
# h, g, d, e, b, f, c, a
```

#### 层次遍历实现

层次遍历的顺序是按层逐级从左到右访问：层次遍历（Level Order Traversal）可以被视为广度优先搜索（Breadth-First Search，BFS）

```python
from collections import deque

def level_order(node):
    if not node:
        return
    queue = deque([node])  # 用队列实现广度优先搜索
    while queue:
        current = queue.popleft()  # 访问当前节点
        print(current.value)
        if current.left:           # 如果有左子节点，加入队列
            queue.append(current.left)
        if current.right:          # 如果有右子节点，加入队列
            queue.append(current.right)

# 调用层次遍历
level_order(root)
# a, b, c, d, e, f, g, h
```











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





