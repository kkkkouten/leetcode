# Leetcode

## [88.合并两个有序数组](https://leetcode.cn/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150)

### 方法二：双指针

将两个数组看作队列，每次从两个数组头部取出比较小的数字放到结果中。

#### 复杂度分析

时间复杂度: O(m+n)。指针移动单调递增，最多移动 m+n 次，因此时间复杂度为 O(m+n)。

空间复杂度: O(m+n)。需要建立长度为 m+n 的中间数组 sorted。


```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        sorted = []
        p1, p2 = 0, 0
        while p1 < m or p2 < n:
            if p1 == m:
                sorted.append(nums2[p2])
                p2 += 1
            elif p2 == n:
                sorted.append(nums1[p1])
                p1 += 1
            elif nums1[p1] < nums2[p2]:
                sorted.append(nums1[p1])
                p1 += 1
            else:
                sorted.append(nums2[p2])     
                p2 += 1
        nums1[:] = sorted   
        
```



## [169.多数元素](https://leetcode.cn/problems/majority-element/description/?envType=study-plan-v2&envId=top-interview-150)

### 方法一：哈希表

#### 思路

出现次数最多的元素大于 n/2 次，所以可以用哈希表来快速统计每个元素出现的次数。

#### 算法

使用哈希映射（HashMap）来存储每个元素以及出现的次数。对于哈希映射中的每个键值对，键表示一个元素，值表示该元素出现的次数。用一个循环遍历数组 nums 并将数组中的每个元素加入哈希映射中。在这之后，我们遍历哈希映射中的所有键值对，返回值最大的键。我们同样也可以在遍历数组 nums 时候使用打擂台的方法，维护最大的值，这样省去了最后对哈希映射的遍历。

#### 复杂度分析

时间复杂度：O(n)，其中 n 是数组 nums 的长度。我们遍历数组 nums 一次，对于 nums 中的每一个元素，将其插入哈希表都只需要常数时间。如果在遍历时没有维护最大值，在遍历结束后还需要对哈希表进行遍历，因为哈希表中占用的空间为 O(n)（可参考下文的空间复杂度分析），那么遍历的时间不会超过 O(n)。因此总时间复杂度为 O(n)。

空间复杂度：O(n)。哈希表最多包含 `n-n/2` 个键值对，所以占用的空间为 O(n)。这是因为任意一个长度为 n 的数组最多只能包含 n 个不同的值，但题中保证 nums 一定有一个众数，会占用（最少） `n/2+1` 个数字。因此最多有 `n−(n/2+1)` 个不同的其他数字，所以最多有`n−n/2`个不同的元素。

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        map = {}
        for num in nums:
            if num in map.keys():
                map[num] += 1
            else:
                map[num] = 1
        
        for key,value in map.items():
            if value > len(nums) / 2:
                return key
```

### 方法二：排序

#### 思路

如果将数组 nums 中的所有元素按照单调递增或单调递减的顺序排序，那么下标为n/2 的元素（下标从 0 开始）一定是众数。

#### 算法

对于这种算法，我们先将 nums 数组排序，然后返回上文所说的下标对应的元素。下面的图中解释了为什么这种策略是有效的。在下图中，第一个例子是 n 为奇数的情况，第二个例子是 n 为偶数的情况。

#### 复杂度分析

时间复杂度：O(nlogn)。将数组排序的时间复杂度为 O(nlogn)。

空间复杂度：O(logn)。如果使用语言自带的排序算法，需要使用 O(logn) 的栈空间。如果自己编写堆排序，则只需要使用 O(1) 的额外空间。



## [189.轮转数组](https://leetcode.cn/problems/rotate-array/description/?envType=study-plan-v2&envId=top-interview-150)

### 方法三：数组翻转

该方法基于如下的事实：当我们将数组的元素向右移动 k 次后，尾部 kmodn 个元素会移动至数组头部，其余元素向后移动 kmodn 个位置。

该方法为数组的翻转：我们可以先将所有元素翻转，这样尾部的 kmodn 个元素就被移至数组头部，然后我们再翻转 [0,kmodn−1] 区间的元素和 [kmodn,n−1] 区间的元素即能得到最后的答案。

#### 复杂度分析

时间复杂度：O(n)，其中 n 为数组的长度。每个元素被翻转两次，一共 n 个元素，因此总时间复杂度为 O(2n)=O(n)。

空间复杂度：O(1)

```python
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n   
        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)
    
    def reverse(self, nums: List[int], i: int, j: int) -> None: 
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
```







