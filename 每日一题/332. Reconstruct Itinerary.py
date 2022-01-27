from collections import defaultdict
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def dfs(point):
            while graph[point]:
                nxt_point = graph[point].pop()
                dfs(nxt_point)
            path.append(point)
            return

        in_deg = defaultdict(int)
        out_deg = defaultdict(int)
        graph = defaultdict(list)
        for a, b in tickets:
            in_deg[b] += 1
            out_deg[a] -= 1
            graph[a].append(b)

        start = 'JFK'
        for k in graph.keys():
            graph[k].sort(reverse=True)
        path = []
        dfs(start)
        return path[::-1]


res = Solution().findItinerary(tickets=[["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]])
print(res)
