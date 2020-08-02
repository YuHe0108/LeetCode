"""
0620, 第一题:
题目描述: 给定一个列表和目标数字，求这个数组第几号的下标之和为目标数字
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


class Solution:
    def twoSum(self, nums, target):
        for index in range(len(nums)):
            for i in range(index, len(nums)):
                if index != i:  # 同一个元素不使用两次
                    if nums[index] + nums[i] == target:
                        return sorted([i, index])
        return None


solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 17))
