"""
0621, 第14题:
题目描述: 输入一个列表，列表中有n个单词，找出在所有单词中出现的前缀单词
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
Input: ["flower","flow","flight"]
Output: "fl"
"""


class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        """思路
         1、找出所有单词中缩短的一个
         2、首先匹配所有单词的第一个，如果匹配成功则匹配第二个，否则输出
        """
        if len(strs) == 0:
            return ''
        else:
            min_len = min(len(x) for x in strs)
            max_match_len = 0

            for index in range(min_len):
                words = set()

                for word_index in range(len(strs)):
                    words.add(strs[word_index][index])

                if len(words) == 1:  # 如果所有单词的第index位都相同，则匹配下一位
                    max_match_len += 1
                else:
                    break

            return strs[0][:max_match_len]


s = Solution()
print(s.longestCommonPrefix(["flower", "flo", "floight"]))
