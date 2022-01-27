from typing import List


class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        res = []
        for k, v in count.items():
            if v == 1 and k + 1 not in count and k - 1 not in count:
                res.append(k)
        return res


class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        nums += [-float("INF"), float("INF")]
        nums.sort()
        n = len(nums)
        res = []
        for i in range(1, n - 1):
            if nums[i] - nums[i - 1] > 1 and nums[i + 1] - nums[i] > 1:
                res.append(nums[i])
        return res
