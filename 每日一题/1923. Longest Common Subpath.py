from typing import List
from collections import defaultdict, Counter


# rolling hash
# class Solution:
#     def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:
#
#         def check(m, count):
#             for z, path in enumerate(paths):
#                 len_p = len(path)
#                 code_val = 0
#                 for i in range(len_p - m + 1):
#                     if i == 0:
#                         for j, v in enumerate(path[i:i + m]):
#                             code_val += pow(base, j) * v
#                     else:
#                         code_val -= path[i - 1]
#                         code_val /= base
#                         code_val += path[i + m - 1] * pow(base, m - 1)
#                     code_val %= mod_val
#                     count[code_val].add(z)
#                     print(m, code_val, path[i:i + m])
#             for key, val in count.items():
#                 if len(val) == total:
#                     print(key, val)
#                     return True
#             return False
#
#         base, mod_val = 97755331, 49999 ** 4 * 3 * 7
#         total = len(paths)
#         k = [len(x) for x in paths]  # k 的最大长度为paths中的最下值
#         left = 0
#         right = min(k)
#         while left < right:
#             mid = left + (right - left + 1) // 2
#             count = defaultdict(set)
#             if check(mid, count):
#                 left = mid
#             else:
#                 right = mid - 1
#         return left
#
#
# res = Solution().longestCommonSubpath(405,
#                                       [[340, 88, 187, 280, 359, 397, 300, 255, 258, 201, 301, 17, 245, 124, 380, 206,
#                                         345, 377, 191],
#                                        [224, 300, 255, 258, 201, 301, 17, 245, 124, 380, 206, 339, 260, 55, 398, 83,
#                                         266, 201, 189],
#                                        [375, 15, 240, 22, 157, 360, 314, 300, 255, 258, 201, 301, 17, 245, 124, 380,
#                                         206, 303, 296],
#                                        [331, 87, 86, 257, 116, 6, 300, 255, 258, 201, 301, 17, 245, 124, 380, 206, 394,
#                                         102, 276],
#                                        [118, 207, 263, 176, 295, 180, 235, 137, 300, 255, 258, 201, 301, 17, 245, 124,
#                                         380, 206, 337]])
# print(res)
#
#
# class Solution:
#     def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:
#         # P和Q为字符串哈希的关键词
#         P, Q = 133331, (1 << 64) + 1
#         m = len(paths)
#         N = 100010
#         p = [1] * N
#         h = [0] * N
#
#         # 获取区间字符串对应的哈希值
#         def get(l, r):
#             return (h[r] - h[l - 1] * p[r - l + 1]) % Q
#
#         # 判断是否存在长度为mid的公共子串
#         def check(mid):
#             cnt = Counter()
#
#             for v in paths:
#                 visited = set()
#                 size = len(v)
#                 for i in range(size):
#                     p[i + 1] = p[i] * P % Q
#                     h[i + 1] = (h[i] * P + v[i]) % Q
#                 for i in range(mid, size + 1):
#                     t = get(i - mid + 1, i)
#                     if t not in visited:
#                         visited.add(t)
#                         cnt[t] += 1
#             return max(cnt.values()) == m
#
#         # 二分满足条件的公共子串长度
#         l, r = 0, len(min(paths, key=lambda x: len(x)))
#         while l < r:
#             mid = l + (r - l + 1) // 2
#             if check(mid):
#                 l = mid
#             else:
#                 r = mid - 1
#         return l
#
#
# res = Solution().longestCommonSubpath(10,
#                                       [[1, 7, 0, 6, 9, 0, 7, 4, 3, 9, 1, 5, 0, 8, 0, 6, 3, 6, 0, 8, 3, 7, 8, 3, 5, 3, 7,
#                                         4, 0, 6, 8, 1, 4],
#                                        [1, 7, 0, 6, 9, 0, 7, 4, 3, 9, 1, 5, 0, 8, 0, 6, 3, 6, 0, 8, 3, 7, 8, 3, 5, 3, 7,
#                                         4, 0, 6, 8, 1, 5],
#                                        [8, 1, 7, 0, 6, 9, 0, 7, 4, 3, 9, 1, 5, 0, 8, 0, 6, 3, 6, 0, 8, 3, 7, 8, 3, 5, 3,
#                                         7, 4, 0, 6, 8, 1]])
# print(res)


class Solution:
    def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:
        base, mod = 97755331, 49999 ** 4 * 3 * 7
        m = len(paths)

        def check(length):

            bucket = set()
            for i, path in enumerate(paths):
                compare_bucket = set()
                code = 0
                for j in range(length):
                    code = (code * base + path[j]) % mod

                if i == 0:
                    bucket.add(code)
                else:
                    compare_bucket.add(code)
                mult = pow(base, length - 1, mod)
                for j in range(length, len(path)):
                    code = (code - path[j - length] * mult) * base + path[j]
                    code = code % mod
                    if i == 0:
                        bucket.add(code)
                    else:
                        compare_bucket.add(code)
                if i > 0:
                    print(compare_bucket, bucket)
                    bucket = bucket & compare_bucket
                    print(bucket, 'a', length)
            if bucket:
                return True
            return False

        left = 0
        right = min([len(x) for x in paths])
        while left < right:
            mid = left + (right - left + 1) // 2
            if check(mid):
                left = mid
            else:
                right = mid - 1
        return left


res = Solution().longestCommonSubpath(5,
                                      [[0, 1, 2, 3, 4], [2, 3, 4], [4, 0, 1, 2, 3]])
print(res)
