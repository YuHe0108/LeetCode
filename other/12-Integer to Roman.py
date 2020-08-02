"""
0621, 第12题:
题目描述: 将整数转换为罗马数字
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
Input: 3
Output: "III"

Input: 4
Output: "IV"

Input: 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3. #

Input: 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
C=100, X=10, XC = C-X = 90

# 4, 和 9 是特例: 4 = IV, 9 =IX
"""


class Solution:
    def intToRoman(self, num: int) -> str:
        roman = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC",
                 50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}
        ans = []
        for k, v in roman.items():
            ans.append(num // k * v)
            num %= k
        return "".join(ans)


s = Solution()
print(s.intToRoman(88))
