"""
0621, 第五题:
题目描述: 从一个字符串中找出一个 ‘头和尾 ’ 相同的子字符串
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Input: "cbbd"
Output: "bb"
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 1、建立一个字典，字典中的key时字符串中的字符，用set()寻找, value为该字母在字符串中出现的索引下标
        if len(s) <= 1:
            return s
        else:
            letter_dict = dict()
            for index, letter in enumerate(s):
                if letter not in letter_dict:
                    letter_dict[letter] = [index]
                else:
                    letter_dict[letter].append(index)

            max_letter = ''
            max_len = 0
            letters_index = list(letter_dict.values())  # 所有字母出现在字符串中的索引下标

            for letter_index in letters_index:  # [0, 2], [1] index
                for index in range(len(letter_index)):
                    for i in range(index, len(letter_index) - 1):
                        start = letter_index[index]  # 同一个字符取间隔 acac ==> aca, cac
                        end = letter_index[1 + i]
                        sub_string = s[start:end + 1]
                        sub_string_len = len(sub_string)  # 子字符串的长度
                        if (end - start + 1) <= 3 and sub_string_len > max_len:  # 如果字符串的长度为小于3且大于之前最长的子字符串
                            max_letter = sub_string
                            max_len = sub_string_len
                        elif sub_string_len > max_len:  # 如果长度大于4
                            half_len = sub_string_len // 2
                            checked = True  # 是否是回文数字
                            for j in range(1, half_len):
                                if sub_string[j] != sub_string[sub_string_len - j - 1]:  # 如果对应位置不相等则不是回文数字
                                    checked = False
                                    break
                            if checked and sub_string_len > max_len:
                                max_letter = sub_string
                                max_len = sub_string_len
            if max_len == 0:
                max_letter = s[0]
            return max_letter


if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome('ac'))
    print(s.longestPalindrome('bb'))
    print(s.longestPalindrome('ccc'))
    print(s.longestPalindrome('cabdc'))
    print(s.longestPalindrome('babad'))
    print(s.longestPalindrome(
        "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"))

    # indexs = [0, 3, 6]
    # for i in range(len(indexs)):  # [0, 1, 2]
    #     for j in range(i, len(indexs) - 1):  # 0, 1, 1
    #         print(indexs[i], indexs[j + 1])
