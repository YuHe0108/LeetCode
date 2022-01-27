import bisect
from typing import List
from collections import defaultdict


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        count = defaultdict(int)
        for s, e, v in events:
            count[s] = max(count[s], v)  # 每个开始时间能够获取的最大值

        # 根据开始时间排序
        count = sorted(count.items(), key=lambda x: x[0])
        max_val = defaultdict(int)
        cur_max = count[-1][-1]  # 最后一个开始时间能够获取的最大值
        max_val[count[-1][0]] = cur_max
        for i in range(len(count) - 2, -1, -1):
            cur_max = max(count[i][-1], cur_max)
            max_val[count[i][0]] = cur_max

        res = 0
        start_time = [x[0] for x in count]  # 开始时间有哪些
        n = len(start_time)
        for s, e, v in events:
            n_s = bisect.bisect_left(start_time, e + 1)
            if n_s == n:
                res = max(res, v)
            else:
                res = max(res, v + max_val[start_time[n_s]])
        return res


solution = Solution()
solution.maxTwoEvents(events=[[1, 5, 3], [1, 5, 1], [6, 6, 5]])
