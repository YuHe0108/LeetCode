"""
0624--搜索旋转排序数组
nums:
(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
排过序，但是经过一些翻转
"""


# 中间的数小于最右边的数，那么mid（包括mid）右边的数是有序的，如果中间的数大于最右边的数，那么mid（包括mid）左边的数是有序的。

class Solution:
    def search(self, nums, target: int) -> int:
        start, end = 0, len(nums) - 1  # start = 0, end=7-1=6

        while start <= end:
            mid = (start + end) // 2  # 取中值, mid = 6 // 2 = 3，中值偏左

            if nums[mid] == target:  # num[3] = 7, 7 != 6
                return mid

            elif nums[mid] < target:  # 如果中间值小于目标值，判断目标值在中间值的左侧还是右侧
                # 中间值如果小于首元素，说明右边是有序的，否则左边是有序的，这一步确定了有序数列在哪边
                # 并且小于目标值
                if nums[mid] < nums[start] <= target:  # nums[start] = 4, num[3] = 7
                    end = mid - 1
                else:  # 目标值在mid的右边
                    start = mid + 1  # start = 3+1=4

            elif nums[mid] > target:  # 中间值大于目标值
                if target <= nums[end] < nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1

        return -1  # 都不存在，则返回-1


solution = Solution()
s = solution.search([4, 5, 6, 7, 0, 1, 2], 6)
print(s)
