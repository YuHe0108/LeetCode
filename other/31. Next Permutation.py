"""
0623: 第31题
给定一个列表，要求每一位都是所给数字的最小值
如果没有比当前的排列更大的排列了（如 3 2 1这样最后的排列），就返回最小的排列（比如 1 2 3）

(1): 1,2,3 → 1,3,2
(2): 3,2,1 → 1,2,3
(3): 1,1,5 → 1,5,1
"""

"""
目标：
    在输入的数字中，如果前一位数字大于当前数字，则进行调换顺序
    并将其后面的全部逆序 
"""

class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        stack = []
        i = len(nums) - 1  # i = 2, nums = [1, 2, 3]
        while i > -1:
            # nums[i], nums[stack[-1]]: 前一位是不是小于后一位
            if stack and nums[i] < nums[stack[-1]]:
                pivot = stack.pop()

                while stack and nums[i] < nums[stack[-1]]:
                    pivot = stack.pop()

                nums[i], nums[pivot] = nums[pivot], nums[i]
                break

            stack.append(i)
            i -= 1
        nums[i + 1:] = nums[i + 1:][::-1]  # i+1 之后所有字符调换顺序


"""
（1） stack = [2], i -= 1, i = 1
（2） nums[1] = 2, stack[-1] = 2, nums[2] = 3, i = 1 
    2 < 3:
        pivot = stack.pop() = 2
        stack = []
    nums[i] = 2, nums[pivot] = nums[2] = 3
    nums = [1, 3, 2]
（3）nums[i+1:] = nums[2:] = nums[2:][::-1] = ''
"""

s = Solution()
nums = [1, 3, 6, 4]
s.nextPermutation(nums)
print(nums)
