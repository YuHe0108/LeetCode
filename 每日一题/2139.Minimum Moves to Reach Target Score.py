class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        if target == 1:
            return 0

        cnt = 0
        while maxDoubles > 0 and target > 1:
            if target % 2 == 1:
                target -= 1
            else:
                target //= 2
                maxDoubles -= 1
            cnt += 1

        return cnt + target - 1


ans = Solution().minMoves(10, 4)
print(ans)
