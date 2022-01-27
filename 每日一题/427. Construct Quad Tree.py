from typing import List


# 四叉树算法
class Node:
    """
    # Definition for a QuadTree node.
    """

    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def helper(row, col, n):
            sum_val = sum(sum(e[col:col + n]) for e in grid[row:row + n])
            if n == 1 or sum_val in [n * n, 0]:
                # sum_val in [n * n, 0] 表明当前的区域内，所有元素的值都是相同的
                return Node(grid[row][col], 1, *[None] * 4)

            n //= 2
            top_left = helper(row, col, n)
            top_right = helper(row, col + n, n)
            bot_left = helper(row + n, col, n)
            bot_right = helper(row + n, col + n, n)
            root = Node(1, 0, top_left, top_right, bot_left, bot_right)
            return root

        return helper(0, 0, len(grid[0]))


solution = Solution()
solution.construct(
    grid=[[1, 1, 1, 1, 0, 0, 0, 0],
          [1, 1, 1, 1, 0, 0, 0, 0],
          [1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 0, 0, 0, 0],
          [1, 1, 1, 1, 0, 0, 0, 0],
          [1, 1, 1, 1, 0, 0, 0, 0],
          [1, 1, 1, 1, 0, 0, 0, 0]])
