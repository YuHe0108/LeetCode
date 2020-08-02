"""
0621, 第6题:
题目描述: 将字符串以固定长度的
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility):
P   A   H   N
A P L S I I G
Y   I   R

（1）给定了行数；
(2）Z形的这种字符串应该分两种情况处理；第一种是“垂直”部分，
    即题目例子中第一列“PAY”，第三列“ALT”这种；第二种就是”斜线“的，如”YPA“和”ISH“这种类型的。
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        lin = 0
        pl = 1
        outp = [""] * numRows
        for i in range(len(s)):
            outp[lin] += s[i]  # 第i行
            if numRows > 1:  # 如果numRows大于1
                lin += pl  # 0 + 1 = 1
                if lin == 0 or lin == numRows - 1:  # lin == numRows - 1表示到了最后一行
                    pl *= -1  # -1 和 1 之间转换，实现上下反转
        outputStr = ""
        for j in range(numRows):
            outputStr += outp[j]
        return outputStr


if __name__ == '__main__':
    s = Solution()
    print(s.convert('ABCDEFGHIJKLMN', 4))

# letters = []
# parts = len(s) // (2 * numRows - 2) + 1
# for index in range(parts):
#     content = s[index * (2 * numRows - 2): (index + 1) * (2 * numRows - 2)]
#     if len(content) != 0:
#         letters.append(content)
#
# return_str = []
# indentation = '\t'
# mid_rows = range(numRows)[1:numRows - 1]
# print(letters)
# for row in range(numRows):
#     for part_index in range(len(letters)):
#         if len(letters[part_index]) > row:
#             return_str.append(letters[part_index][row])
#             return_str.append(indentation * (numRows - 1))
#             # if row % numRows in mid_rows:  # 中间字母
#             #     mid_word = '{}{}{}'.format('\t', letters[part_index][row], '\t')
#             #     return_str.append(mid_word)  # 中间字符
#     return_str.append('\n')
#
# result = ''.join(x for x in return_str)
# print(result)

