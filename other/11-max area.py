"""
0621, 第11题:
题目描述: 有n个非负数，n个数的高度代表了木板的长度
每个模板间隔为1，不改变木板距离，求使用两个木板装最多水为多少
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines,
which together with x-axis forms a container, such that the container contains the most water.
"""


class Solution:
    def maxArea(self, height: list) -> int:
        # 最左边、最右边、最大的面积初始值
        left_board, right_board, max_area = 0, len(height) - 1, 0

        while left_board < right_board:
            distance = right_board - left_board  # distance
            min_height = min(height[left_board], height[right_board])
            max_area = max((distance * min_height), max_area)

            # 如果左边的木板长度小于右边的木板长度，左边木板索引加1
            if height[left_board] < height[right_board]:
                left_board += 1
            else:
                right_board -= 1
        return max_area


s = Solution()
print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))

""" way-1:
list_len = len(height)
max_area = 0
for i in range(list_len):
    for j in range(i, list_len):
        if i != j:
            print(i, j)
            distance = j - i  # 两个木板之间的间隔
            left_board = height[i]
            right_board = height[j]
            min_height = min(left_board, right_board)
            area = min_height * distance
            if area > max_area:
                max_area = area
"""
