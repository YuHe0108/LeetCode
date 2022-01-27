from typing import List
from functools import cmp_to_key
from collections import defaultdict


class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        nxt_course = defaultdict(list)  # 每个课程修完后可以修的课
        lines = defaultdict(int)
        for pre, nex in relations:
            lines[nex] += 1
            nxt_course[pre].append(nex)

        cost_time = [0] * (n + 1)  # 完成每个课程实际需要花费的时间
        time = [0] + time
        points = []
        for i in range(1, n + 1):
            if i not in lines or lines[i] == 0:  # 没有依赖课程
                points.append(i)
                cost_time[i] = time[i]

        while points:
            p = points.pop()
            for np in nxt_course[p]:
                cost_time[np] = max(cost_time[np], cost_time[p] + time[np])
                lines[np] -= 1
                if lines[np] == 0:
                    points.append(np)
        return max(cost_time)


solution = Solution()
r = solution.minimumTime(n=3, relations=[[1, 3], [2, 3]], time=[3, 2, 5])
print(r)
