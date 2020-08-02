"""
判断输入符号是否正确:

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Input: "()[]{}"
Output: true

Input: "([)]"
Output: false

Input: "{[]}"
Output: true
"""


class Solution:
    def isValid(self, s: str) -> bool:
        """思路：
         1、先判断 第0位的字符是否匹配第偶数位的字符
         2、如果条件1满足，在判断内部是不是满足
        """
        # pattern_dict = {'(': 0, ')': 1,
        #                 '{': 3, "}": 4,
        #                 '[': 6, ']': 7}
        # len_s = len(s)  # s的长度
        # half_len = len_s // 2
        # even_nums = [x for x in range(len_s) if x % 2 == 0]  # 所有偶数位的值
        # odd_nums = [x for x in range(len_s) if x % 2 == 1]  # 所有奇数位的值
        #
        # pattern_matched = True
        # for index in range(half_len):
        #     even_num = even_nums[index]
        #     for odd_index in range(index, half_len):
        #         odd_num = odd_nums[odd_index]
        #         diff = pattern_dict[s[odd_num]] - pattern_dict[s[even_num]]
        #         if odd_num - even_num == 1:
        #             if diff != 1:
        #                 pattern_matched = False  # ()[]{}对应这种情况
        #                 break
        #
        #         elif odd_num - even_num > 1 and diff == 1:  # ([]){}对应这种请况
        #             mid_len = odd_num - even_num  # 奇数
        #             if mid_len > 1:
        #                 mid_even = [x for x in range(even_num + 1, odd_num) if x % 2 == 0]
        #                 mid_odd = [x for x in range(even_num + 1, odd_num) if x % 2 == 1]
        #                 half_mid_len = len(mid_even)
        #                 for mid_index in range(half_mid_len):
        #                     mid_even_s = pattern_dict[s[mid_even[mid_index]]]
        #                     mid_odd_s = pattern_dict[s[mid_odd[mid_index]]]
        #                     if mid_even_s - mid_odd_s != 1:
        #                         pattern_matched = False
        #                         break
        #                     else:
        #                         pattern_matched = True
        #
        # return pattern_matched
        d = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for i in s:
            if i in d:  # 1
                stack.append(i)
            elif len(stack) == 0 or d[stack.pop()] != i:  # pop 移除列表的最后一位
                return False

        return len(stack) == 0  # 3


s = Solution()
print(s.isValid('()[]{}'))
print(s.isValid('([{}])'))
print(s.isValid('(){[]}'))
print(s.isValid('(}{[]}'))
a = [1, 2, 3]
# '([]){}'
"""
1、先判断两两是不是匹配的
2、如果1不满足，判断首尾是不是匹配的
3、如果都不满足，则为False
        if len(s) % 2 == 1:
            return False
        pattern_dict = {'(': 0, ')': 1,
                        '{': 3, "}": 4,
                        '[': 6, ']': 7}
        situation = [True, True]
        half_len = len(s) // 2
        half_nums = [x for x in range(half_len)]

        # 第二种情况
        for i in half_nums:
            pattern_1 = pattern_dict[s[i]]
            pattern_2 = pattern_dict[s[len(s) - 1 - i]]
            differ = pattern_2 - pattern_1
            if differ != 1:
                situation[0] = False
                break

        # 第一种情况
        even_nums = [x for x in range(len(s)) if x % 2 == 0]
        odd_nums = [x for x in range(len(s)) if x % 2 == 1]
        for index in range(len(even_nums)):
            pattern_1 = pattern_dict[s[even_nums[index]]]
            pattern_2 = pattern_dict[s[odd_nums[index]]]
            differ = pattern_2 - pattern_1
            if differ != 1:
                situation[1] = False

        if situation[0] is False and situation[1] is False:
            return False
        else:
            return True
"""
