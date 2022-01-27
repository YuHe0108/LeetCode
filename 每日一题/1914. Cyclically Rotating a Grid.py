from typing import List


class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        layers = min(rows // 2, cols // 2)

        res = [[0] * cols for _ in range(rows)]
        for i in range(layers):
            s_r, s_c = i, i
            cur_r, cur_c = rows - 2 * i, cols - 2 * i
            candidate = []
            for c in range(cur_c):
                candidate.append((s_r, s_c + c))
            s_c += cur_c - 1
            for r in range(1, cur_r):
                candidate.append((s_r + r, s_c))
            s_r += cur_r - 1
            for c in range(1, cur_c):
                candidate.append((s_r, s_c - c))
            s_c = i
            for r in range(1, cur_r - 1):
                candidate.append((s_r - r, s_c))

            total = len(candidate)
            cur_k = k % total
            for idx in range(total):
                n_idx = (idx + cur_k) % total
                r, c = candidate[idx]
                n_r, n_c = candidate[n_idx]
                res[r][c] = grid[n_r][n_c]
                idx += 1
        return res


solution = Solution()
solution.rotateGrid(
    [[10, 1, 4, 8],
     [6, 6, 3, 10],
     [7, 4, 7, 10],
     [1, 10, 6, 1],
     [2, 1, 1, 10],
     [3, 8, 9, 2],
     [7, 1, 10, 10],
     [7, 1, 4, 9],
     [2, 2, 4, 2],
     [10, 7, 5, 10]],1)
