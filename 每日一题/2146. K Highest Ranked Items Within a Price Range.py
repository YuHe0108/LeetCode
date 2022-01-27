from typing import List
from collections import deque


class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int):
        rows, cols = len(grid), len(grid[0])
        res = []
        if pricing[0] <= grid[start[0]][start[1]] <= pricing[1]:
            res.append([0, grid[start[0]][start[1]], start[0], start[1]])

        points = deque()
        points.append([0, start[0], start[1]])
        seen = set()
        while points:
            dis, x, y = points.popleft()
            seen.add((x, y))
            for nx, ny in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
                if nx < 0 or ny < 0 or nx >= rows or ny >= cols:
                    continue
                if (nx, ny) in seen:
                    continue
                if grid[nx][ny] == 0:
                    continue
                points.append([dis + 1, nx, ny])
                seen.add((nx, ny))
                if pricing[0] <= grid[nx][ny] <= pricing[1]:
                    res.append([dis + 1, grid[nx][ny], nx, ny])
        res.sort()
        res = res[:k]
        ans = []
        for _, _, x, y in res:
            ans.append([x, y])
        return ans


res = Solution().highestRankedKItems([[0, 2, 0]], [2, 2], [0, 1], 1)
print(res)
