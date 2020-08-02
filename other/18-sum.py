"""
0622 第18题： 找出由四个元素组成的列表，其中列表和的值等于target，数字不能重复选择

Given an array nums of n integers and an integer target,
are there elements a, b, c, and d in nums such that a + b + c + d = target?
Find all unique quadruplets in the array which gives the sum of target.

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""


class Solution:
    def fourSum(self, n: list, t: int) -> list:
        if not n:
            return []

        n.sort()  # 首先对n排序, # [-2, -1, 0, 0, 1, 2]
        L = len(n)  # n的长度
        N = {j: i for i, j in enumerate(n)}  # 如果是重复的元素，则只保留索引大的值
        S = set()  # 一个集合，去除重复的元素
        M = n[-1]  # M为最后一个元素
        print(N)
        for i in range(L - 3):  # 因为要取四位，因此取值的范围要在输入数组长度-3之内

            a = n[i]
            if a + 3 * M < t:  # 当前值 + 3 * 最大值 小于 目标值，说明在需要增加当前值，所以跳出本此循环
                continue
            if 4 * a > t:  # 如果当前值的 四倍 大于 目标值，需要跳出循环, 因为a越往后值越大，所以不用计算
                break

            # 如果 当前值 + 3 * 最大值 大于 目标值，说明缩小最大值，有可能接近 target 的值
            for j in range(i + 1, L - 2):  # j 为 i 的之后一个值
                b = n[j]
                if a + b + 2 * M < t:  # 将3M 转换为2M，说明将之前的值减小了
                    continue
                if a + 3 * b > t:  # a + 3*b 是最小值, 如果之和仍然比 target 大，直接退出
                    break
                for k in range(j + 1, L - 1):
                    c = n[k]  # C 是 第 k 位 的值, 也是第三个值
                    d = t - (a + b + c)  # d是第四个值
                    if d > M:
                        continue
                    if d < c:
                        break
                    # N[d] > k, 说明 d 的值要大于 c 的值
                    if d in N and N[d] > k:  # N[d] 是 d 在 num 中的索引下标
                        S.add((a, b, c, d))
        S = list(S)
        return [list(x) for x in S]


s = Solution()
print(s.fourSum([1, 0, -1, 0, -2, 2], 0))
# [[-2, -1, 1, 2], [-2, 0, 0, 2], [-2, 0, 1, 1], [-1, 0, 0, 1]]
# [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
# {-2: 0, -1: 1, 0: 3, 1: 4, 2: 5}
# [-2, -1, 0, 0, 1, 2]
