"""
0621, 第9题:
题目描述: 判断一个数字是不是回文数
Input: 121
Output: true
Input: -121
Output: false
Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            num_list = []
            while x > 0:
                num_list.append(x % 10)
                x = x // 10

            mid_len = len(num_list) // 2
            for i in range(mid_len):
                if num_list[i] != num_list[len(num_list) - i - 1]:
                    return False
            return True


s = Solution()
print(s.isPalindrome(10001))
