"""
0621, 第13题:
题目描述: 将罗马数字转换为整型
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
"""


# 罗马数字排列有一个规律，就是大的数字在前面，小的在后面
class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        add = 0  # 最后的输出结果
        i = 0  # 移动的下标索引
        while i <= len(s) - 1:
            if i == len(s) - 1:  # 意味着到了最后s的最后一位
                add += d[s[i]]
                break
            if d[s[i]] < d[s[i + 1]]:
                # 如果前一位数字小于后一位的数字，需要用后一位的数字减去前一位的数字，比如9=IX
                # i 加了两次，相当于两个字符看作是一个数字
                add = add + (d[s[i + 1]] - d[s[i]])  # 10-1=9
                i += 1
            else:
                add = add + d[s[i]]
            i += 1
        return add


s = Solution()
print(s.romanToInt('XIX'))  # x=10, IX+9 = 19
"""
len(s) = 4
i=0, add=0
    0 <= 4-1
    i != 4-1
    d[s[0]] = 5, d[s[1]] = 1
    5 > 1
    add = add + 5

i=1, add=5
    1 < 3
    1 != 3
    d[s[1]] =1, d[s[2]] = 1
    1 == 1
    add = 1 + add = 6

i=2, add=6
    2 < 3
    2 != 3
    d[s[2]]= 1, d[s[3]] = 1
    1 == 1
    add = 1 + add =7

i = 3, add =7
    3 == 3
    add = d[s[4]] + add = 1 + 7 = 8
"""
