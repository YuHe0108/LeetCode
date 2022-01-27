class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        res = 0
        while len(cost) >= 2:
            v1 = cost.pop()
            v2 = cost.pop()
            if cost:
                cost.pop()
            res += v1 + v2
        return res + sum(cost)