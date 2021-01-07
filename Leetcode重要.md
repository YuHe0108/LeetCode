## 1、并查集的使用及代码模版

##### 684. Redundant Connection

```python
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        father = dict()
        
        def find_father(x):
            # 查找 x 的祖先节点
            if father[x] != x:
                father[x] = find_father(father[x])
            return father[x]
        
        def union(x, y):
            x = find_father(x) # 查找x的祖先节点
            y = find_father(y) # 查找y的祖先节点
            if x > y:
                father[x] = y # 将x的祖先节点设置为y的祖先节点
            else:
                father[y] = x
            
        for a, b in edges:
            if a not in father:
                father[a] = a
            if b not in father:
                father[b] = b
            if find_father(a) == find_father(b):
                return (a, b)
            else:
                # 父节点不同的话，需要 union一下
                union(a, b)
```



## 2、二叉搜索树

##### 701. Insert into a Binary Search Tree： 

​	将一个数字插入到二差搜索树中，并保持二差搜索树的性质不变。

```python
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        return root
```



## 3、遍历从根节点到叶子节点的所有路径

```python
def dfs(node, path):
    nonlocal res
    if not node: return
    if not node.left and not node.right:
        path.append(node.val)
        path.pop()
        return
    path.append(node.val)
    dfs(node.left, path)
    dfs(node.right, path)
    path.pop()
```

##### 1448. Count Good Nodes in Binary Tree： 

```python
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        
        def dfs(node, path):
            nonlocal res
            if not node:
                return
            if not node.left and not node.right:
                path.append(node.val)
                if node.val >= max(path):
                    res += 1
                path.pop()
                return
            if not path or node.val >= max(path):
                res += 1
            path.append(node.val)
            dfs(node.left, path)
            dfs(node.right, path)
            path.pop()
        
        dfs(root, [])
        return res
```



## 4、从根节点向上操作

##### 814-Binary Tree Pruning

```python
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        def helper(node):
            if not node:
                return None
            node.left = helper(node.left)
            node.right = helper(node.right)
            if not node.left and not node.right and node.val == 0:
                return None
            return node
        
        return helper(root)
```



## 5、重建树：low bound\high bound

##### 1008-Construct Binary Search Tree from Preorder Traversal

```python
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        
        def helper(low, high):
            nonlocal idx
            if idx == N: 
                return None
            val = preorder[idx]
            if val < low or val > high:
                return None
            idx += 1
            cur_node = TreeNode(val)
            cur_node.left = helper(low, val)
            cur_node.right = helper(val, high)
            return cur_node

        idx = 0
        N = len(preorder)
        return helper(-float('inf'), float('inf'))
```



## 6、遍历二叉树下有多少节点

```python
def count_elements(root):
	if not root: 
        return 0
	l_count = count_elements(root.left)
	r_count = count_elements(root.right)
	return l_count + r_count + 1
```



## 7、进制之间的相互转换

##### 1017-Convert to Base -2：将10进制的数字转换为 -2 进制

```python
class Solution:
    def baseNeg2(self, N: int) -> str:
        if N == 0: return '0'
        base, res, carry = -2, [], 0
        while N != 0:
            r = N % base # 余数
            d = N // (base) # 商
            if r < 0: # 余数不能出现负数
                d += 1
                r += abs(base)
            res.append(str(r))
            N = d #　直到商不为0为止
        res.reverse()
        return ''.join(res)
```



##### 1073-Adding Two Negabinary Numbers：实现两个数组之间的进制转换

```python
class Solution:
    def addNegabinary(self, arr1, arr2):
        base = -2
        # 按最高有效位到最低有效位的顺序排列
        arr1.reverse() # reverse之后，最低位在idx=0的位置
        arr2.reverse()
        res = []
        carry = 0 
        for i in range(max(len(arr1), len(arr2)) + 2):
            a = arr1[i] if i < len(arr1) else 0
            b = arr2[i] if i < len(arr2) else 0
            sum_val = a + b + carry
            r = sum_val % (base) # 余数
            carry = sum_val // (base) # 商
            if r < 0:
                carry += 1
                r += abs(base)
            res.append(r)
        while len(res) > 1 and res[-1] == 0:
            res.pop()
        res.reverse()
        return res
```



### 8、DP 常见问题类型

##### 8-1 决策形--递归 + 记忆法

##### 1140-Stone Game II

```python
from collections import defaultdict

class Solution:
    def stoneGameII(self, piles) -> int:
        M, N = 1, len(piles)
        suf_sum = [0] * (N + 1)
        for i in range(N-1, -1, -1):
            suf_sum[i] = suf_sum[i+1] + piles[i]
        self.seen = defaultdict(int)
        return self.helper(0, 1, suf_sum, piles)
    
    def helper(self, i, M, suf_sum, piles):
        if i == len(piles): 
            return 0
        key = (i, M)
        if key in self.seen:
            return self.seen[key]
        
        sum_val = 0
        for x in range(1, M*2+1):
            if i + x - 1 >= len(piles):
                break
            sum_val += piles[i + x -1]
            self.seen[key] = max(self.seen[key], 
            				   sum_val + suf_sum[i+x] - self.helper(i+x, max(x, M),suf_sum, piles))
        return self.seen[key]
            
        
```



##### 8-2 DP + 前缀和

1546-Maximum Number of Non-Overlapping Subarrays With Sum Equals Target

```python
class Solution:
    def maxNonOverlapping(self, nums, target: int) -> int:
        # 前缀和
        pre_sum = [0, nums[0]]
        for i in range(1, len(nums)):
            pre_sum.append(pre_sum[-1] + nums[i])
        
        pre_sum_dict = {0: 0} # 0 的前缀和为0
        dp = [0] * (len(nums) + 1)
        if nums[0] == target: 
            dp[1] = 1
        for i in range(1, len(nums) + 1):
            dp[i] = dp[i-1] # 不使用当前的 val
            needs = pre_sum[i] - target
            if needs in pre_sum_dict:
                j = pre_sum_dict[needs]
                dp[i] = max(dp[i], dp[j] + 1)
            pre_sum_dict[pre_sum[i]] = i
        return dp[-1]
```



##### 8-2 第一类区间型 DP

##### 8-3 第一类区间型 DP

##### 8-4 第一类区间型 DP

## 8、Bit Manipulation 常见问题类型

##### 1、如何取出一个二进制的低 n 位

例如：一个数的二进制表达形式为：10001，那么如何取出这个数的 100 [01] 这两个数字呢？

可以使用位运算：10001 & （int(11)）-->  01 



###### 405-Convert a Number to Hexadecimal： 二进制转换16进制

![405](E:\Codes\LeetCode\Bit Manipulation\1108\405.jpg)

```python
class Solution:
    def toHex(self, num: int) -> str:
        hex_num = '0123456789abcdef'
        if num == 0: return '0'
        
        cnt = 0
        h = ''
        while cnt < 8 and num:
            h = hex_num[num & 15] + h # 15 -> 1111 表示取出低四位
            num >>= 4
            cnt += 1
        return h
```



###### 2、生成具有 k 个 1 的 bit-mask 的全部可能

```python
# m 表示想要生成有多少位 的二进制
m = 10
state = (1 << k) - 1 # 具有 k 个 1 的 bit-mask

while state < (1 << m):
    # check(state)
    c = state & -state
    r = state + c
    state = (((r ^ state) >> 2) / c) | r
```



## 9、前缀树 Trie

##### 1、前缀树模版

```python
class Node:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = Node()
        
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]
        node.is_end = True
```



## 10、双端队列的构建

```python
class LinkedListNode:
    def __init__(self, val: int):
        self.val = val
        self.prev = None # 前节点
        self.succ = None # 后节点

class LinkedList:
    def __init__(self):
        self.head = LinkedListNode(-1)
        self.tail = LinkedListNode(-1)
        self.head.succ = self.tail
        self.tail.prev = self.head
        self.size = 2 # 初始化长度2 即两个dummy节点
    
    def __str__(self):
        ret = list()
        cur = self.head
        while cur:
            ret.append(cur.val)
            cur = cur.succ
        return str(ret)

    def insert(self, it: LinkedListNode, val: int):
        """在当前节点前插入一个节点"""
        self.size += 1
        node = LinkedListNode(val)
        it.prev.succ = node
        node.prev = it.prev
        it.prev = node
        node.succ = it
    
    def erase(self, it: LinkedListNode) -> LinkedListNode:
        """删除当前节点"""
        self.size -= 1
        ret = it.succ
        it.prev.succ = it.succ
        it.succ.prev = it.prev
        return ret
    
    def advance(self, it: LinkedListNode, dt: int) -> LinkedListNode:
        """移动指针指定个位置"""
        if dt > 0:
            for _ in range(dt):
                it = it.succ
        elif dt < 0:
            for _ in range(-dt):
                it = it.prev
        return it


class FrontMiddleBackQueue:

    def __init__(self):
        self.q = LinkedList()
        self.it = self.q.head
        self.ptrpos = 0 # 当前指针位置

    def pushFront(self, val: int) -> None:
        # 指针不指向哑头节点
        if self.ptrpos != 0:
            self.ptrpos += 1
        self.q.insert(self.q.head.succ, val)

    def pushMiddle(self, val: int) -> None:
        pos = self.q.size // 2
        # 均摊 O(1)
        self.it = self.q.advance(self.it, pos - self.ptrpos) # 移动到中间位置
        self.q.insert(self.it, val)
        self.ptrpos = pos+1
        
    def pushBack(self, val: int) -> None:
        # 指针指向哑尾节点
        if self.ptrpos == self.q.size - 1:
            self.ptrpos += 1
        self.q.insert(self.q.tail, val)

    def popFront(self) -> int:
        if self.q.size == 2:
            return -1
        ret = self.q.head.succ.val
        if self.ptrpos == 1:
            self.it = self.q.erase(self.it)
        else:
            self.q.erase(self.q.head.succ)
            # 指针不指向哑头节点
            if self.ptrpos != 0:
                self.ptrpos -= 1
        return ret

    def popMiddle(self) -> int:
        if self.q.size == 2:
            return -1
        pos = (self.q.size - 1) // 2
        # 均摊 O(1)
        self.it = self.q.advance(self.it, pos - self.ptrpos)
        ret = self.it.val
        self.it = self.q.erase(self.it)
        self.ptrpos = pos
        return ret

    def popBack(self) -> int:
        if self.q.size == 2:
            return -1
        ret = self.q.tail.prev.val
        if self.ptrpos == self.q.size - 2:
            self.it = self.q.erase(self.it)
        else:
            self.q.erase(self.q.tail.prev)
            # 指针指向哑尾节点
            if self.ptrpos == self.q.size:
                self.ptrpos -= 1
        return ret

# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()
```

































