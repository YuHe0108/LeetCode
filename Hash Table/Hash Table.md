## Hash Table的用法

### 1. heap python的内置数据结构，在用于返回k个最大值或者最小值的时候有用

#### 1.1 堆的使用方法

1.  heapq.heappop(heap)：将heap的最小值pop出heap，heap为空时报IndexError错误

   ```python
   >>> items = [1,2,9,7,3]
   >>> heapq.heappush(items,10)
   >>> items
   >>> [1, 2, 9, 7, 3, 10]
   
   ```

2.  heapq.heappush(heap,item):将item，推入heap

   ```python
   # heap在pop时总是将最小值首先pop出
   >>> heapq.heappop(items)
   	1
   >>> items
   	[2, 3, 9, 7, 10]
   ```

3.  heapq.heappushpop(heap,item)：pop出heap中最小的元素，推入item

   ```python
   >>> items
   	[2, 3, 9, 7, 10]
   >>> heapq.heappushpop(items,11)
   	2
   >>> items
   	[3, 7, 9, 11, 10]
   >>>
   ```

4.  heapq.heapify(x)：将list X转换为heap

   ```python
   >>> nums = [1,10,9,8]
   >>> heap = list(nums)
   >>> heapq.heapify(heap)
   >>> heap
   [1, 8, 9, 10]
   
   ```

5.  heapq.heapreplace(heap,item)：pop出最小值，推入item，heap的size不变、

   与 heapq.heappushpop 的区别：heapreplace(a,x)返回最初在a中的最小值, 而不管x的值如何, 顾名思义, heappushpop(a,x) 在弹出最小值之前将 x 推送到a上.

   ```python
   >>> from heapq import *
   >>> a = [2,7,4,0,8,12,14,13,10,3,4]
   >>> heapify(a)
   >>> b = a[:]
   >>> heappushpop(a, -1)
   -1
   >>> heapreplace(b, -1)
   0
   ```

6. heapq.merge(*iterable)：将多个可迭代合并，并且排好序，返回一个iterator

   ```python
   >>> heap
   [8, 10, 9, 100]
   >>> heap1 = [10,67,56,80,79]
   >>> h = heapq.merge(heap,heap1)
   >>> list(h)
   [8, 10, 9, 10, 67, 56, 80, 79, 100]
   # 需要 说明的是这里所谓的排序不是完全排序，只是两个list对应位置比较，
   # 将小的值先push，然后大的值再与另外一个list的下一个值比较
   ```

7. heapq.nlargest(n,iterable,key)：返回item中大到小顺序的前N个元素，key默认为空，可以用来指定规则如：function等来处理特定的排序

   ```python
   itemsDict=[
       {'name':'dgb1','age':23,'salary':10000},
       {'name':'dgb2','age':23,'salary':15000},
       {'name':'dgb3','age':23,'salary':80000},
       {'name':'dgb4','age':23,'salary':80000}
   ]
    
   itemsDictlarge = heapq.nlargest(3,itemsDict,lambda s:s['salary'])
   print(itemsDictlarge)
   [{'name': 'dgb3', 'age': 23, 'salary': 80000}, {'name': 'dgb4', 'age': 23, 'salary': 80000}, {'name': 'dgb2', 'age': 23, 'salary': 15000}]
   ```
8.  如果items中有两个以上的元素，heapq会根据第一个元素排序，升序排序。

#### 例题：给定一个列表，返回其中k个出现频率最高的元素



