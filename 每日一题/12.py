class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        if n % 2 == 1: # 如果长度为奇数，肯定不可以
            return []
        count = Counter(changed)
        odd_nums = []
        even_nums = []
        changed.sort()
        for v in changed:
            if v % 2 == 1:
                odd_nums.append(v)
            else:
                even_nums.append(v)
        cnt = 0
        idx = 0
        res = odd_nums
        while idx < len(odd_nums):
            v = odd_nums[idx]
            if count[v] == 0:
                idx += 1
            else:
                if count[v * 2] > 0:
                    count[v * 2] -= 1
                    count[v] -= 1
                    cnt += 2
                else:
                    return []
        idx = 0
        while idx < len(even_nums):
            v = even_nums[idx]
            if count[v] == 0:
                idx += 1
            else:
                if  count[v * 2] > 0:
                    res.append(v)
                    count[v * 2] -= 1
                    count[v] -= 1
                    cnt += 2
                else:
                    return []
        if cnt == n:
            return res
        return []