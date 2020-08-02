"""
0622 第17题:
输入一个字符串类型的数字，要求返回两位字符所有可能的取值
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
2: a、b、c
3: d、e、f
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""


class Solution:
    def letterCombinations(self, digits: str) -> list:
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z'],
                 }

        result = []

        def combine_digits(current, digit):
            if len(digit) == 0:
                result.append(current)
                return
            else:
                for char in phone[digit[0]]:
                    combine_digits(char + current, digit[1:])

        if len(digits) == 0:
            return []
        else:
            combine_digits('', digits)
            return result


s = Solution()
print(s.letterCombinations('23'))

"""
第一位2：abc
'' + a = a
helpCombine('a', '3')
for char in ['d', 'e', 'f']:
    current + char = 'a' + 'd' = 'ad'
    helpCombine(current+char, leftoverDigits[1:]='')
"""
