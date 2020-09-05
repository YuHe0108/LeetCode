### Back Tracking 

#### 		backtracking（回溯算法）也叫试探法，它是一种系统地搜索问题的解的方法。回溯算法的基本思想是：从一条路往前走，能进则进，不能进则退回来，换一条路再试。

#### 		回溯算法说白了就是穷举法。不过回溯算法使用剪枝函数，剪去一些不可能到达最终状态（即答案状态）的节点，从而减少状态空间树节点的生成。

#### 		回溯法是一个既带有系统性又带有跳跃性的的搜索算法。它在包含问题的所有解的解空间树中，按照**深度优先**的策略，从根结点出发搜索解空间树。算法搜索至解空间树的任一结点时，总是先判断该结点是否肯定不包含问题的解。如果肯定不包含，则跳过对以该结点为根的子树的系统搜索，逐层向其祖先结点回溯。否则，进入该子树，继续按深度优先的策略进行搜索。

##### 		1. 回溯法在用来求问题的**所有解**时，要回溯到根，且根结点的所有子树都已被搜索遍才结束。

##### 		2. 而回溯法在用来求问题的**任一解**时，只要搜索到问题的一个解就可以结束。		

	#### 	这种**以深度优先的方式**系统地搜索问题的解的算法称为回溯法，它适用于解一些组合数较大的问题。

### 1. 46-Permutations 全排列问题

##### 要求：返回给定数组的全排列

```python
Input: [1,2,3]
Output:
    [
      [1,2,3],
      [1,3,2],
      [2,1,3],
      [2,3,1],
      [3,1,2],
      [3,2,1]
    ]
```

```python
class Solution:
    def permute(self, nums):
        self.res = []
        self.dfs(nums, [])
        return self.res
    
    def dfs(self, nums, path):
        if not nums:
            self.res.append(list(path))
            return
        
        for i in range(len(nums)):
            path.append(nums[i])
            self.dfs(nums[:i] + nums[i+1:], path)
            path.pop()
```

### 2. 47  Permutations II

​	**要求：给定的数组中含有重复的元素**

```python
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.nums = nums
        counter = Counter(nums)
        self.dfs(counter, [])
        return self.res
    
    def dfs(self, counter, path):
        if len(path) == len(self.nums):
            self.res.append(list(path))
            return
        
        for x in counter:
            if counter[x] > 0:
                counter[x] -= 1
                path.append(x)
                self.dfs(counter, path)
                path.pop()
                counter[x] += 1
            else:
                continue
```





