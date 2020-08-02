"""
0621, 第四题:
题目描述: 两个已经排序过后的列表，长度分别为m和n。找出两个列表元素的中值
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
You may assume nums1 and nums2 cannot be both empty.
example 1:
nums1 = [1, 2]
nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5

example 2:
nums1 = [1, 3]
nums2 = [2]
The median is 2.0
"""


class Solution:
    def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:
        joined_nums = sorted(nums1 + nums2)  # 对列表1和列表2排序
        total_length = len(joined_nums)
        if total_length % 2 == 0:
            left_index = total_length // 2 - 1
            right_index = total_length // 2
            result = (joined_nums[left_index] + joined_nums[right_index]) / 2
        else:
            result = joined_nums[total_length // 2]
        return float(result)


if __name__ == '__main__':
    s = Solution()
    print(s.findMedianSortedArrays([1, 3], [2, 4]))
