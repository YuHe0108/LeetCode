import math


class Solution:
    def countTriples(self, n: int) -> int:
        cnt = 0
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                k = int(math.sqrt(i ** 2 + j ** 2))
                if k <= n and k ** 2 == i ** 2 + j ** 2:
                    cnt += 1
        return cnt


solution = Solution()
solution.countTriples(5)
