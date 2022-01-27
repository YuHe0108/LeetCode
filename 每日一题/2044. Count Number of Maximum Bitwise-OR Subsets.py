from typing import List
from collections import defaultdict


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = len(nums)
        t = 1 << n
        xor_val = 0
        xor_cnt = 1
        for c in range(1, t):
            cur = 0
            for i in range(n):
                if (c >> i) & 1 == 1:
                    cur |= nums[i]
            if cur > xor_val:
                xor_val = cur
                xor_cnt = 1
            elif cur == xor_val:
                xor_cnt += 1
        return xor_cnt


solution = Solution()
solution.countMaxOrSubsets(nums=[3, 2, 1, 5])
