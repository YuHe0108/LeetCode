"""
0623：
给定 n， 通过这 n 对字母生成成对的字符
当 n == 3 时：
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""


class Solution:
    def generateParenthesis(self, n: int):
        out_list = []
        self.helper(out_list, '', 0, 0, n)
        return out_list

    def helper(self, out_list, current_str, open_pattern, close_patten, max_pattern):
        if len(current_str) == 2 * max_pattern:
            out_list.append(current_str)
            return

        if open_pattern < max_pattern:
            self.helper(out_list, current_str + '(', open_pattern + 1, close_patten, max_pattern)

        if close_patten < open_pattern:
            self.helper(out_list, current_str + ')', open_pattern, close_patten + 1, max_pattern)


# class Solution:
#     def generateParenthesis(self, n: int):
#         res = []
#         self.helper(res, n, n)
#         return res
#
#     def helper(self, res, Open, Close, curr=''):
#         if Open == 0 and Close == 0:
#             res.append(curr)
#         if Open < 0 or Close < 0:
#             return
#
#         if Open == Close:
#             self.helper(res, Open - 1, Close, curr + '(')
#
#         if Open < Close:
#             self.helper(res, Open - 1, Close, curr + '(')
#             self.helper(res, Open, Close - 1, curr + ')')


"""
[] 3 3 
[] 2 3 (
[] 1 3 ((
[] 0 3 (((
[] -1 3 ((((
[] 0 2 ((()
[] -1 2 ((()(
[] 0 1 ((())
[] -1 1 ((())(
[] 0 0 ((()))
['((()))'] -1 0 ((()))(
['((()))'] 1 2 (()
['((()))'] 0 2 (()(
['((()))'] -1 2 (()((
['((()))'] 0 1 (()()
['((()))'] -1 1 (()()(
['((()))'] 0 0 (()())
['((()))', '(()())'] -1 0 (()())(
['((()))', '(()())'] 1 1 (())
['((()))', '(()())'] 0 1 (())(
['((()))', '(()())'] -1 1 (())((
['((()))', '(()())'] 0 0 (())()
['((()))', '(()())', '(())()'] -1 0 (())()(
['((()))', '(()())', '(())()'] 2 2 ()
['((()))', '(()())', '(())()'] 1 2 ()(
['((()))', '(()())', '(())()'] 0 2 ()((
['((()))', '(()())', '(())()'] -1 2 ()(((
['((()))', '(()())', '(())()'] 0 1 ()(()
['((()))', '(()())', '(())()'] -1 1 ()(()(
['((()))', '(()())', '(())()'] 0 0 ()(())
['((()))', '(()())', '(())()', '()(())'] -1 0 ()(())(
['((()))', '(()())', '(())()', '()(())'] 1 1 ()()
['((()))', '(()())', '(())()', '()(())'] 0 1 ()()(
['((()))', '(()())', '(())()', '()(())'] -1 1 ()()((
['((()))', '(()())', '(())()', '()(())'] 0 0 ()()()
['((()))', '(()())', '(())()', '()(())', '()()()'] -1 0 ()()()(
['((()))', '(()())', '(())()', '()(())', '()()()']





1、n=3
    open = close = 3
    res = [], open = open - 1=2, close=3, curr= '('
2、open=2, close=3
    open < close
    res = [], open-1= 2-1 = 1, close=3, curr='(('
    res = [], open = 1, close= 3-1 = 2, curr='(()'
3、open = 1, close = 2
    res = [], open = 1-1=0, close=2, curr = '(()('
    res = [], open = 1-1=0, close=2, curr = '(()()'
4、1 <

"""

s = Solution()
res = s.generateParenthesis(3)
print(res)
