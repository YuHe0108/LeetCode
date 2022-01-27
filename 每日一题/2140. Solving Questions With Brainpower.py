from typing import List


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            point, skip = questions[i]
            dp[i] = max(dp[i + 1], point + dp[min(i + skip + 1, n)])
        return dp[0]


ans = Solution().mostPoints(questions=[[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]])
print(ans)
