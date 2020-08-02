"""
0621, 第10题:
题目描述: 匹配字符
Input: 121
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.
'.' Matches any single character. 一个字符
'*' Matches zero or more of the preceding element. 0个或多个字符
Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
"""


class Solution:
    def isMatch(self, text: str, pattern: str) -> bool:
        # 长度为 len(text) + 1, 每个里面都是一个列表，每个列表中都是len(pattern) + 1个False
        dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]
        # [[False, False], [False, False], [False, False]]
        dp[-1][-1] = True
        # [[False, False], [False, False], [False, True]]
        for i in range(len(text), -1, -1):
            for j in range(len(pattern) - 1, -1, -1):
                first_match = i < len(text) and pattern[j] in {text[i], '.'}  # 第一个字母是不是匹配的
                if j + 1 < len(pattern) and pattern[j + 1] == '*':
                    dp[i][j] = dp[i][j + 2] or first_match and dp[i + 1][j]
                else:
                    dp[i][j] = first_match and dp[i + 1][j + 1]
        return dp[0][0]


# s="aa", p='a'
s = Solution()
print(s.isMatch('aa', 'a'))
