from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = [[arr[0], 1]]
        n = len(arr)
        mod_val = 1e9 + 7
        values = [arr[0]]
        for i in range(1, n):
            v = arr[i]
            ans = 0
            cnt = 1
            while stack and v <= stack[-1][0]:
                pre_v, pre_cnt = stack.pop()
                ans -= pre_v * pre_cnt
                cnt += pre_cnt
            stack.append([v, cnt])
            values.append(values[-1] + v * cnt + ans)
        return int(sum(values) % mod_val)


solution = Solution()
res = solution.sumSubarrayMins([2, 3, 1, 4])
print(res)
print(11 + 81 + 11 + 11 + 81 + 94 + 11 + 43 * 3 + 15)
print(sum([11, 81, 94, 43, 3]) - res)
