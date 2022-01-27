from typing import List
from functools import reduce
from collections import defaultdict


class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        def traverse(root):
            nonlocal child_count
            if root not in child or child[root] == 0:
                child_count[root] = 1
                return 1
            if len(child[root]) == 1:  # 有一个子节点
                child_count[root] = traverse(child[root][0]) + 1
            else:  # 有两个子节点
                child_count[root] = traverse(child[root][0]) + traverse(child[root][1]) + 1
            return child_count[root]


        n = len(parents)
        child = defaultdict(list)  # 每个节点的子节点
        for i, v in enumerate(parents):
            child[v].append(i)

        child_count = defaultdict(int)  # 每个节点子孙节点的数量
        traverse(0)
        print(child_count)

        # 需要统计每个节点 子节点的数量
        res = 0
        max_val = 0
        for i in range(n):
            vals = []
            if len(child[i]) > 0:  # 子节点的子孙节点数量
                vals += [child_count[v] for v in child[i]]
            if i != 0:  # 父节点(祖先) 的子孙节点数量
                vals.append(child_count[0] - child_count[i])

            cur_val = reduce(lambda x, y: x * y, vals)
            if cur_val > max_val:
                res = 1
                max_val = cur_val
            elif cur_val == max_val:
                res += 1
            print(vals, cur_val, i)
        return res


solution = Solution()
r = solution.countHighestScoreNodes([-1, 10, 5, 0, 6, 9, 0, 4, 4, 1, 6, 10])
print(r)
