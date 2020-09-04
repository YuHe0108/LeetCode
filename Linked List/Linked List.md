### 1. 链表的定义

    1. 链表是一种递归的数据结构，它或者为空（null），或者是指向一个结点（node）的引用，
       该节点还有一个元素和一个指向另一条链表的引用。
    2. 链表（Linked list）是一种常见的基础数据结构，是一种线性表，但是并不会按线性的顺序存储数据，
       而是在每一个节点里存到下一个节点的指针 (Pointer)。由于不必须按顺序存储，链表在插入的时候可以达到 O(1) 的复杂度，
       比另一种线性表顺序表快得多，但是查找一个节点或者访问特定编号的节点则需要 O(n)的时间，
       而顺序表相应的时间复杂度分别是 O(logn)和 O(1)。
    3. 使用链表结构可以克服数组链表需要预先知道数据大小的缺点，链表结构可以充分利用计算机内存空间，实现灵活的内存动态管理。
       但是链表失去了数组随机读取的优点，同时链表由于增加了结点的指针域，空间开销比较大。

### 2. 链表的结构
#### 2.1 单向链表
    1. 链表中最简单的一种是单向链表，它包含两个域，一个信息域和一个指针域。
    2. 这个链接指向列表中的下一个节点，而最后一个节点则指向一个空值。
    3. 一个单向链表包含两个值: 当前节点的值和一个指向下一个节点的链接一个单向链表的节点被分成两个部分。
    4. 第一个部分保存或者显示关于节点的信息，第二个部分存储下一个节点的地址。单向链表只可向一个方向遍历。
<img src='linked list_1.jpg' width=400 div align=center />

#### 2.2 双向链表
    1. 一种更复杂的链表是 “双向链表” 或“双面链表”。
       每个节点有两个 链接：一个指向前一个节点，（当此 “连接” 为第一个 “连接” 时，指向空值或者空列表）；
       而另一个指向下一个节点，（当此 “连接” 为最后一个 “连接” 时，指向空值或者空列表）。
    2. 一个双向链表有三个整数值: 数值, 向后的节点链接, 向前的节点链接
    3. 双向链表也叫双链表:双向链表中不仅有指向后一个节点的指针，还有指向前一个节点的指针。
       这样可以从任何一个节点访问前一个节点，当然也可以访问后一个节点，以至整个链表。
       一般是在需要大批量的另外储存数据在链表中的位置的时候用。
       双向链表也可以配合下面的其他链表的扩展使用。
<img src='linked list_2.jpg' width=400>

#### 2.3 循环链表
    1. 在一个 循环链表中, 首节点和末节点被连接在一起。这种方式在单向和双向链表中皆可实现。要转换一个循环链表，
       你开始于任意一个节点然后沿着列表的任一方向直到返回开始的节点。
    2. 再来看另一种方法，循环链表可以被视为 “无头无尾”。这种列表很利于节约数据存储缓存， 
       假定你在一个列表中有一个对象并且希望所有其他对象迭代在一个非特殊的排列下。指向整个列表的指针可以被称作访问指针。
<img src='linked list_3.jpg' width=400>

### 3. 链表相关的核心点
    1. null/nil 异常处理
    2. dummy node 哑巴节点
    3. 快慢指针
    4. 插入一个节点到排序链表
    5. 从一个链表中移除一个节点
    6. 翻转链表
    7. 合并两个链表
    8. 找到链表的中间节点

### 4. 相关题型

#### 4.1 链表的反转十分重要

<img src="E:\Codes\LeetCode\Linked List\0901\206.jpg" alt="206" style="zoom:90%;" />


```python
class Solution:
    def reverseList(self, head):
        pre = None
        cur = head 
        while cur:
            temp = curr.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre
```

#### 4.2 链表元素的Swap：

##### 题目说明：

​			给定一个链表，每隔两个相邻节点交换并返回其头。您不能修改列表节点中的值，只能更改节点本身。

##### Example:

   			Given 1->2->3->4,  you should return the list as 2->1->4->3.

```python
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        res = root = ListNode()
        res.next = head
        while res.next and res.next.next:
            a = res.next
            b = res.next.next
            c = res.next.next.next
            res.next = b
            res.next.next = a
            res.next.next.next = c
            res = res.next.next
        return root.next
```

#### 4.3 链表的快慢节点：

​		快慢指针：慢指针每次移动一个节点，快指针每次移动两个节点。当快指针遍历到链表结尾时，慢指针刚好指向中间节点。

**快慢指针**

​		快慢指针的快慢主要是指在遍历链表过程中指针移动的快慢。比如遍历单链表，我们可以让慢指针每次移动一个节点，让快指针移动两个或两个以上的节点。

#### 4.4 构造双向指针

​		双向指针:

```python
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return
        vals = []
        while head:
            vals.append(head.val)
            child_val = self.check_child(head)
            vals.extend(child_val)
            head = head.next
        
        res = root = Node(0, None, None, None)
        nodes = [] 
        for i in range(len(vals)):
            root.next = Node(vals[i], None, None, None)
            root = root.next
            if nodes:
                root.prev = nodes.pop()
            nodes.append(root)
        return res.next
            
    def check_child(self, root):
        child = root.child
        vals = []
        while child:
            vals.append(child.val)
            if child.child:
                c_vals = self.check_child(child)
                vals.extend(c_vals)
            child = child.next
        return vals
```









​	