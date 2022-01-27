from typing import List
from collections import defaultdict, deque


class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        points = deque()
        points.append([1, 0])  # 节点、花费时间
        seen = [0] * (n + 1)
        dist = [-1] * (n + 1)  # 到到
        dist[1] = 0
        while points:
            p, t = points.popleft()
            change_round = t // change  # 0 - change: 绿灯，change - change+1: 红灯
            if change_round % 2 == 0:
                nxt_t = t + time
            else:
                nxt_t = (change_round + 1) * change + time
            for nxp in graph[p]:
                if seen[nxp] < 2 and dist[nxp] < nxt_t:
                    dist[nxp] = nxt_t
                    seen[nxp] += 1
                    points.append([nxp, nxt_t])
                    if nxp == n and seen[nxp] == 2:  # 第二次到达终点
                        return nxt_t
        return -1


solution = Solution()
res = solution.secondMinimum(n=5, edges=[[1, 2], [1, 3], [1, 4], [3, 4], [4, 5]], time=3, change=5)
print(res)
