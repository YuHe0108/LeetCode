from collections import defaultdict


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        alphas = set(s)
        ans = 0
        for v in alphas:
            l_idx = s.index(v)
            r_idx = s.rindex(v)
            if l_idx < r_idx - 1:
                ans += len(set(s[l_idx + 1:r_idx]))
        return ans


if __name__ == '__main__':
    solution = Solution()
    solution.countPalindromicSubsequence(s="aabca")
