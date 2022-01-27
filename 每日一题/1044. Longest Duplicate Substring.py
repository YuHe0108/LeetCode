from typing import List
from collections import defaultdict

"""
class Solution:
    def longestDupSubstring(self, s: str) -> str:
        def check(length):
            nonlocal max_len, ans
            if length == 0:
                return False

            count = defaultdict(int)
            # code = 0
            # for i in range(length):
            #     code = code * base + s_num[i]
            for i in range(len(s) - length + 1):
                count[s[i:i + length]] += 1

            for k, v in count.items():
                if v > 1 and length > max_len:
                    max_len = length
                    ans = k
                    return True
            return False

        left = 0
        right = len(s)
        max_len = 0
        ans = ''
        while left < right:
            mid = left + (right - left + 1) // 2
            if check(mid):
                left = mid
            else:
                right = mid - 1
        return ans
"""


class Solution:
    def longestDupSubstring(self, s: str) -> str:
        base = pow(10, 7) + 1
        mod = 1 << 64 - 1

        def check(length):
            if length == 0:
                return -1
            code = 0
            seen = set()
            for i in range(length):
                code = (code * base + s_num[i]) % mod
            seen.add(code)
            mult = pow(base, length - 1, mod)
            for i in range(length, len(s)):
                code = (code - s_num[i - length] * mult) * base + s_num[i]
                code %= mod
                if code in seen:
                    return i - length + 1
                seen.add(code)
            return -1

        s_num = [ord(x) - ord('a') + 1 for x in s]
        left = 0
        right = len(s)
        idx = -1
        max_len = 0
        while left < right:
            mid = left + (right - left + 1) // 2
            check_res = check(mid)
            if check_res != -1:
                max_len = mid
                idx = check_res
                left = mid
            else:
                right = mid - 1
        return s[idx:idx + max_len] if idx != -1 else ''


res = Solution().longestDupSubstring(
    "nyvzwttxsshphczjjklqniaztccdrawueylaelkqtjtxdvutsewhghcmoxlvqjktgawwgpytuvoepnyfbdywpmmfukoslqvdrkuokxcexwugogcwvsuhcziwuwzfktjlhbiuhkxcreqrdbj")
print(res)
