import bisect
from typing import List
from collections import Counter, defaultdict


class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        line_idx = []  # 竖线的索引坐标
        prefix = {}
        for i, v in enumerate(s):
            if v == '|':
                if not prefix:
                    prefix[i] = 0
                else:
                    prefix[i] = i - line_idx[-1] - 1 + prefix[line_idx[-1]]
                line_idx.append(i)

        if len(line_idx) < 2:  # 竖线的数量少于两个，肯定都是 0
            return [0] * len(queries)

        res = [0] * len(queries)
        for i, (left, right) in enumerate(queries):
            if left > line_idx[-1] or right < line_idx[0]:
                continue

            if s[left] == '|':  # 如果正好是竖线
                l_count = prefix[left]
            else:  # 如果不是竖线，向右找最先出现的竖线位置
                r_line_idx = line_idx[bisect.bisect_right(line_idx, left)]
                l_count = prefix[r_line_idx]

            if s[right] == '|':
                r_count = prefix[right]
            else:
                l_line_idx = line_idx[bisect.bisect_left(line_idx, right) - 1]
                r_count = prefix[l_line_idx]

            res[i] = max(r_count - l_count, 0)
        return res


solution = Solution()
solution.platesBetweenCandles(s = "**|**|***|", queries = [[2,5],[5,9]])
# s = "***|**|*****|**||**|*", queries = [[1,17],[4,5],[14,17],[5,11],[15,16]]
