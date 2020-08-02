"""
0621, 第8题:
题目描述: 将字符串转换为整型，并且在 pow(2, 31)范围内
 if x >= pow(2, 31)- 1  x <= -pow(2, 31):
    return 0
Input: "42"
Output: 42

Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.

Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical
             digit or a +/- sign. Therefore no valid conversion could be performed.

Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−231) is returned.
"""


class Solution:
    def myAtoi(self, string: str) -> int:
        list1 = []
        hasSpace = False
        for _ in range(0, len(string)):
            if hasSpace and string[_].isdigit() is False:
                break
            elif string[_] != ' ' or string[_] == '-' or string[_] == '+' or string[_].isdigit():
                # 如果是 非空格、加号、减号、数字, 后面就必须是数字，否则就跳出循环
                hasSpace = True
                list1.append(string[_])
        try:
            if int(''.join(list1)) > (2 ** 31) - 1 or int(''.join(list1)) < (2 ** 31) * -1:
                if list1[0] == '-':
                    return (2 ** 31) * -1
                else:
                    return (2 ** 31) - 1
        except ValueError:
            return 0
        return int(''.join(list1))


s = Solution()
print(s.myAtoi("word  -0012a42"))
