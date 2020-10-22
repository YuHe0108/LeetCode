##### 1、并查集的使用及代码模版

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

#### 2、二叉搜索树

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



#### 3、遍历从根节点到叶子节点的所有路径

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



#### 4、从根节点向上操作

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



#### 5、重建树：low bound\high bound

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

