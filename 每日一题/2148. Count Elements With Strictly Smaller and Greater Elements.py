class Solution:
    def countElements(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        cnt = 0
        for i in range(1, n-1):
            if nums[i] > nums[0] and nums[i] < nums[-1]:
                cnt += 1
        return cnt