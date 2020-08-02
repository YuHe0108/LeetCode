"""
0622 第16题:
给定一个含有 n 个元素的列表， 找出三个数字之和最接近 目标数字，并输出三个数字之和，可以认为每一个输入只有一个解法

Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target.
Return the sum of the three integers.
You may assume that each input would have exactly one solution.
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""


class Solution:
    def threeSumClosest(self, num: list, target: int) -> int:
        num.sort()
        result = num[0] + num[1] + num[2]  # 排序后的nums计算前三个数字的和
        for i in range(len(num) - 2):
            j, k = i + 1, len(num) - 1  # j 为 i 的前一位, k 为数组的最后一位
            while j < k:  # i为第一位，j为第二位，如果j小于最后一位
                sum = num[i] + num[j] + num[k]
                if sum == target:
                    return sum

                if abs(sum - target) < abs(result - target):
                    result = sum
                if sum < target:  # 如果和小于target了，要增加正数值，所以要右移
                    j += 1
                elif sum > target:  # 如果大于target了，说明需要增加负值，所以要左移
                    k -= 1
        return result


s = Solution()
print(s.threeSumClosest([0, 2, 1, -3], 1))

# sorted_nums = sorted(nums)
# target_in_nums_index = None
# if target < sorted_nums[0]:
#     target_in_nums_index = 0
# elif target > sorted_nums[-1]:
#     target_in_nums_index = len(sorted_nums) - 1
# else:
#     for index in range(len(sorted_nums)):
#         if sorted_nums[index] == target:  # 如果中间数字
#             target_in_nums_index = index
#             break
#         else:  #
#             if sorted_nums[index] < target < sorted_nums[index + 1]:
#                 target_in_nums_index = [index, index + 1]
#                 break
#
# # 计算最接近target的值
# if type(target_in_nums_index) is int:  # 是整数, 说明小于最小值、大于最大值 或者输入数组中正好存在这个值
#     if 0 < target_in_nums_index < len(nums) - 1:  # 正好是中间值
#         results = sorted_nums[target_in_nums_index - 1] + sorted_nums[target_in_nums_index] + \
#                   sorted_nums[target_in_nums_index + 1]
#     elif target_in_nums_index == 0:  # 首位
#         results = sorted_nums[target_in_nums_index] + sorted_nums[target_in_nums_index + 1] + \
#                   sorted_nums[target_in_nums_index + 2]
#     else:  # 末尾
#         results = sorted_nums[target_in_nums_index] + sorted_nums[target_in_nums_index - 1] + \
#                   sorted_nums[target_in_nums_index - 2]
# else:  # 是列表, 数字不在输入数组中，但是在输入数组的两个数中间
#     left_index = sorted(target_in_nums_index)[0]
#     right_index = sorted(target_in_nums_index)[1]
#     if left_index - 1 < 0:  # 如果左移一位小于0，说明越界了，只能向右移动两位
#         results = sorted_nums[left_index] + sorted_nums[right_index] + sorted_nums[right_index + 1]
#     elif right_index + 1 > len(nums) - 1:  # 如果右移一位大于输入num长度0，说明越界了，只能向左移动两位
#         results = sorted_nums[left_index - 1] + sorted_nums[left_index] + sorted_nums[right_index]
#     else:
#         left_results = sorted_nums[left_index] + sorted_nums[right_index] + sorted_nums[right_index + 1]
#         right_results = sorted_nums[left_index - 1] + sorted_nums[left_index] + sorted_nums[right_index]
#         results = left_results if abs(left_results - target) < abs(right_results - target) else right_results
# return results
