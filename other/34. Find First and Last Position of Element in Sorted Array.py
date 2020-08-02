"""
0624:
问题描述：
给定一个数组，这个数组是有序的，并给定一个Target，这个target 在数组中重复出现，求出现的索引下标。

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
Your algorithm's runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""


class Solution:
    def searchRange(self, nums: list, target: int):
        def helper(lo, hi, left):
            found = -1
            while lo <= hi:
                mid = lo + (hi - lo) // 2
                if target > nums[mid]:
                    lo = mid + 1
                elif target < nums[mid]:
                    hi = mid - 1
                else:
                    if left:
                        found = mid
                        hi = mid - 1
                    else:
                        found = mid
                        lo = mid + 1

            return found

        l = helper(0, len(nums) - 1, True)
        r = helper(0, len(nums) - 1, False)
        return [l, r]
