"""
0624:
给定一个字符串，输出最长成对匹配的符号，包含字符的数量

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        m = l = r = 0

        for e in s:
            if e == '(':
                l += 1
            else:
                r += 1
            if l == r:  # 只有当两个字符出现的次数相等时，才能算作匹配
                m = max(m, r + l)
            elif r > l:
                r = l = 0
        #
        # l = r = 0
        # for e in s[::-1]:
        #     if e == ')':
        #         r += 1
        #     else:
        #         l += 1
        #     if l == r:
        #         m = max(m, r + l)
        #     elif l > r:
        #         l = r = 0
        return m


solution = Solution()
result = solution.longestValidParentheses('(()')
print(result)
