#### 1617--Count Subtrees With Max Distance Between Cities

```python
# 初始状态mask里面的1代表这次选的所有node，然后BFS尝试把所有node连在一起，每连一个node，就把1设置成0
from collections import defaultdict, deque

class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges):
        graph = defaultdict(list)
        for s, e in edges:
            graph[s-1].append(e-1)
            graph[e-1].append(s-1)
        print(graph)
        
        def get_max_dist(mask):
            # 1、检查mask是否可以构成一颗树
            # 2、如果可以构成一颗树，返回这个树的最大 distance
            # if str(bin(mask)[2:]).count('1') <= 1:
            #    return 0
            
            # 对于只选择一颗树的情况，最大距离就是 1
            if mask & (mask - 1) == 0:
                return 0
            
            ans = 0
            for i in range(n):
                if mask & (1 << i):
                    queue = deque([i])
                    
                    temp_mask = mask
                    temp_mask ^= 1 << i # 求异或
                     
                    d = 0
                    while queue:
                        que_len = len(queue)
                        for _ in range(que_len):
                            node = queue.popleft()
                            for nei in graph[node]:
                                if temp_mask & (1 << nei):
                                    queue.append(nei)
                                    temp_mask ^= 1 << nei
                        d += 1
                    if temp_mask:
                        return 0
                    ans = max(ans, d)
            return ans - 1
        
        res = [0] * (n-1)
        for mask in range(1<<n): # 遍历每一个树选或者不选
            dist = get_max_dist(mask)
            if dist:
                res[dist-1] += 1
        return res
```

```python
import collections, itertools

class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges):
        
        vertices = [i for i in range(1, n+1)]
        ans = [0]*(n-1)
        
        graph = collections.defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        
        def checkValid(tree):
            tree = set(tree)
            start = tree.pop() # 随机弹出一个 节点
            tree.add(start)
            
            trav = set()
            # 随机从一个subtree的一个节点出发，查看是否能够遍历sub_tree的所有节点
            def helper(curr):
                nonlocal trav
                
                trav.add(curr)
                for nei in graph[curr]:
                    if (nei not in trav) and (nei in tree):
                        helper(nei)
                        
            helper(start)
            return trav == tree
        
        def MaxDis(tree):
            # should be the diameter of tree
            tree = set(tree)
            start = tree.pop()
            tree.add(start)
            
            diameter = 0
            
            def DFS(curr, trav):
                nonlocal diameter
                
                neighbors_dep = []
                for nei in graph[curr]:
                    if nei not in trav and nei in tree:
                        neighbors_dep.append(DFS(nei, trav | {nei}))
                        
                if not neighbors_dep:
                    dia = 0
                    diameter = max(diameter, dia)
                    return 0
                elif len(neighbors_dep)==1:
                    dia = 1+neighbors_dep[0]
                    diameter = max(diameter, dia)
                    return dia
                else:
                    dia = sum(sorted(neighbors_dep)[-2:])+2
                    diameter = max(diameter, dia)
                    return max(neighbors_dep)+1
                
            DFS(start, {start})
            return diameter
        
        
        for l in range(1, n+1):
            # 从vertices中，返回长度为 l 的组合可能
            subtrees = list(itertools.combinations(vertices, l))
            for subtree in subtrees:
                # 验证每一个subtree
                if checkValid(subtree): # 首先验证 subtree 是不是有效的tree
                    max_dis = MaxDis(subtree) # 如果是有效的节点，计算节点之间的最大距离
                    if max_dis > 0:
                        ans[max_dis - 1] += 1
        return ans
```

##### 926-Flip String to Monotone Increasing

##### 730-Count Different Palindromic Subsequences