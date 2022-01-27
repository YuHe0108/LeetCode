from typing import List
from collections import Counter


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = Counter(arr)
        cnt = 0
        for v in arr:
            if count[v] == 1:
                cnt += 1
                if cnt == k:
                    return v
        return ''


solution = Solution()
solution.kthDistinct(['a', 'b', 'a'], 3)
