"""
0621, 第三题:
题目描述: 给一个string，找出其中出现最多 <子字符串>的长度
Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 1、字符串从开头开始数，有多少个字母不同
        str_list = []
        max_length = 0
        for letter in s:
            if letter in str_list:  # 如果在str_list中
                str_list = str_list[str_list.index(letter) + 1:]
                print(str_list, letter)
            str_list.append(letter)  # 如果字母不在str_list中
            max_length = max(max_length, len(str_list))
        return max_length


if __name__ == '__main__':
    # "pw", 'wke', 'wabcde'
    s = Solution()
    print(s.lengthOfLongestSubstring("pwwkewkea"))
