from collections import deque
from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        dq = deque()
        dq.append(entrance)
        seen = set(entrance)
        cnt = 0
        while dq:
            for _ in range(len(dq)):
                r, c = dq.popleft()

                if maze[r][c] == '.' and (r == rows - 1 or c == cols - 1 or r == 0 or c == 0) and [r, c] != entrance:
                    return cnt

                for nr, nc in (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1):
                    if nr >= rows or nc >= cols or nr < 0 or nc < 0:
                        continue
                    if maze[nr][nc] == '+' or (nr, nc) in seen:
                        continue
                    dq.append((nr, nc))
                    seen.add((nr, nc))
            cnt += 1
        return -1


solution = Solution()
res = solution.nearestExit(maze=[["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]], entrance=[1, 2])
print(res)
