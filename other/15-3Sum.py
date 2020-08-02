"""
0622, 第15题:
题目描述: 给定一个列表，有n个元素， 要求求和为0，并且每一个数字不能重复使用，
如果某个数字在输入数组中只出现了一次，那么能使用超过两次
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.
Note:
The solution set must not contain duplicate triplets.
Given array nums = [-1, 0, 1, 2, -1, -4],
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


class Solution:
    def threeSum(self, nums: list):
        neg = {}  # 用字典存储正值和负值
        pos = {}
        zeros = 0

        # 存储解决方案，重复的方案会自动过滤
        solutions = set()

        # 初始化字典. O(n).
        for i in nums:
            if i < 0:
                neg.setdefault(i, 0)
                neg[i] += 1
            elif i > 0:
                pos.setdefault(i, 0)
                pos[i] += 1
            else:
                zeros += 1

        # {num for num in nums} 是一个set， 会过滤相同的数字，i 和 j的符号一定是不同的
        for i in {num for num in nums}:
            if i < 0:  # 如果 i 是一个负数，j要从正数里面找
                for j in pos:  # j 是 pos 字典中的键
                    # Seek for third number, k = -(i + j)
                    k = -i - j  # k是一个差值，i + j + k = 0
                    if k in pos:  # 如果k是正值
                        # 如果 k 正好等于 j 并且  j 在原始输入数组中出现的次数只有一次，那么为无效方案
                        if k == j and pos[j] == 1:
                            continue
                        else:  # Valid solution;
                            solutions.add(tuple(sorted((i, j, k))))
                    # If third number is '0' and we have zeros to use.
                    elif k == 0 and zeros > 0:
                        solutions.add(tuple(sorted((i, j, 0))))

            # Logic below is nearly identical logic as above. Kept it verbose for readability.
            # Seeking negative numbers to offset positive numbers.
            elif i > 0:
                for j in neg:
                    k = -i - j
                    if k in neg:
                        if k == j and neg[j] == 1:
                            continue
                        else:
                            solutions.add(tuple(sorted((i, j, k))))
                    elif k == 0 and zeros > 0:
                        solutions.add(tuple(sorted((i, j, 0))))

            # 如果输入列表中的0含有三个以上，可以使用(0, 0, 0)作为一个方案
            elif zeros >= 3:
                solutions.add((0, 0, 0))

        return [list(s) for s in solutions]


s = Solution()
print(s.threeSum([-1, 0, 1, 2, -1, -4]))
