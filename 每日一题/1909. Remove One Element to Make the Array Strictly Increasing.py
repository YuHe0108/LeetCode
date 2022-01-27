# class Solution:
#     def canBeIncreasing(self, nums) -> bool:
#         if nums == sorted(nums) and len(nums) == len(set(nums)):
#             return True
#
#         for i in range(len(nums)):
#             val = nums.pop(i)
#             if nums == sorted(nums) and len(nums) == len(set(nums)):
#                 return True
#             nums.insert(i, val)
#         return False


class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        prev = nums[0]
        prev2 = 0
        flag = False
        for i in range(1, len(nums)):
            curr = nums[i]
            if curr <= prev:
                if flag:
                    return False
                else:
                    flag = True
                    if curr > prev2:
                        prev = curr
            else:
                prev2, prev = prev, curr
        return True


s = Solution()
print(s.canBeIncreasing([2, 3, 1, 2]))
