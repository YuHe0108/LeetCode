"""
0624:
    给定一个排序后的数组、一个待插入的数字
    要求将该数字插入值数组中，并保持有序状态，有该数字在列表中应该插入的下标索引

Input: [1,3,5,6], 5
Output: 2
Input: [1,3,5,6], 2
Output: 1
Input: [1,3,5,6], 7
Output: 4
Input: [1,3,5,6], 0
Output: 0
"""


class Solution:
    def searchInsert(self, nums, target: int) -> int:
        start = 0
        end = len(nums) - 1
        insert_index = 0
        if len(nums) == 0:
            return 0

        while start <= end:
            mid = (end - start) // 2 + start

            if target <= nums[start]:
                return start
            elif target >= nums[end]:
                if target == nums[end]:
                    return end
                else:
                    return end + 1
            elif nums[start] < target < nums[mid]:
                start += 1
            elif nums[mid] < target < nums[end]:
                end -= 1
            else:
                return mid

        return insert_index


s = Solution()
index = s.searchInsert([3, 6, 7, 8, 10], 5)
print(index)
