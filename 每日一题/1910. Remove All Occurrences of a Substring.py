"""
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        if part not in s:
            return s

        n, m = len(s), len(part)
        part_list = list(part)
        while part in s:
            s_list = list(s)
            for i in range(n - m + 1):
                if s_list[i:i + m] == part_list:
                    s_list[i:i + m] = [''] * m
                    break
            s = ''.join(s_list)
        return s
"""


class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        # 方法1: 模拟+贪心+多个判断条件+短路特性
        cur = ""
        m = len(part)
        for c in s:
            cur += c
            if c == part[-1] and len(cur) >= m and cur[-m:] == part:
                # 利用短路特性, 判断条件依次变复杂, 避免直接进行成本较高的判断
                cur = cur[:-m]
        return cur
        # 方法2: KMP+额外动态维护当前res的next数组
        # 对于res而言, 当遇到匹配子串后它也会回到前面的位置, 所以同样利用KMP的思想, 动态求res的next数组
        m = len(part)
        # 下面这部分是经典的求part的next数组过程
        nextp = [-1] + [0] * m
        l, r = -1, 0
        while r < m:
            if l == -1 or part[l] == part[r]:
                l += 1
                r += 1
                nextp[r] = l
            else:
                l = nextp[l]
        # 下面这部分是经典的KMP双指针匹配过程, 但是需要额外维护一个数组, 用于映射res的下标i到匹配的part的下标j之间的关系
        # 数组初始化一个哨兵元素-1, 用于处理s的前缀与part匹配的情况, 此时移除该匹配后需要重新从0开始匹配
        nexts = [-1]
        # res初始化为空, 只有在遇到与part匹配的字符时才追加, 另外当与整个part字符串匹配时还要移除这部分
        res = ""
        i, j = 0, 0
        while i < len(s):
            if j == -1 or s[i] == part[j]:
                res += s[i]
                # 当前字符与part的下标j匹配, 将其加入nexts数组中
                nexts.append(j)
                i += 1
                j += 1
            else:
                j = nextp[j]
            if j == m:
                # 找到一个匹配, 移除res和nexts数组的长度为m的后缀
                res = res[:-m]
                nexts = nexts[:-m]
                # nexts[-1]存储的是res移除长度为m的后缀后的最后一个字符相匹配的part的字符下标, 此处加1表示继续从part的下一个字符处开始匹配
                j = nexts[-1] + 1
        return res


s = Solution()
res = s.removeOccurrences("aabababa", "aba")
print(res)
