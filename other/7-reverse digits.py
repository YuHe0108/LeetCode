"""
0621, 第7题:
题目描述: 数字反转
Input: 123
Output: 321
Input: -123
Output: -321
Input: 120
Output: 21
"""


class Solution:
    def reverse(self, x: int) -> int:
        max_num = pow(2, 31)
        if x <= -max_num or x >= max_num - 1:
            return 0
        elif x == 0:
            return 0
        else:
            str_x = str(x)
            reversed_x = str_x[::-1]
            if x > 0:
                result = int(reversed_x)
            elif x < 0:
                result = -int(reversed_x[:-1])

            if result <= -max_num or result >= max_num - 1:
                return 0
            else:
                return result


s = Solution()
print(s.reverse(123))
