# class Solution:
#     def sumGame(self, num: str) -> bool:
#         odd_sum = even_sum = 0
#         for i, v in enumerate(num):
#             if v == '?':
#                 continue
#             if i % 2 == 0:
#                 even_sum += int(v)
#             else:
#                 odd_sum += int(v)
#
#         num_list = list(num)
#         idx = 0
#         alice = True  # alice 先手
#         while '?' in num_list:
#             if num_list[idx] == '?':
#                 if alice:
#                     if idx % 2 == 0:
#                         if even_sum > odd_sum:
#                             even_sum += 9
#                             num_list[idx] = '9'
#                         else:
#                             num_list[idx] = '0'
#                     else:
#                         if even_sum > odd_sum:
#                             num_list[idx] = '0'
#                         else:
#                             odd_sum += 9
#                             num_list[idx] = '9'
#                     alice = False
#                 else:
#                     if idx % 2 == 0:
#                         if even_sum > odd_sum:
#                             num_list[idx] = str(0)
#                         else:
#                             dif = odd_sum - even_sum
#                             even_sum += dif
#
#                             num_list[idx] = str(dif)
#                     else:
#                         if even_sum > odd_sum:
#                             dif = even_sum - odd_sum
#                             odd_sum += dif
#                             num_list[idx] = str(dif)
#                         else:
#                             num_list[idx] = '0'
#                     alice = True
#             idx += 1
#         print(odd_sum, even_sum)
#         return odd_sum == even_sum

class Solution:
    def sumGame(self, num: str) -> bool:
        front, back = 0, 0
        n = len(num)
        mid = n // 2
        for i in range(mid):
            v = num[i]
            if v != '?':
                front += int(num[i])
        for i in range(mid, n):
            v = num[i]
            if v != '?':
                back += int(num[i])

        alice = True
        for i in range(n):
            if num[i] == '?':
                if alice:
                    alice = False
                    if i < mid:
                        if front > back:
                            front += 9
                    else:
                        if front < back:
                            back += 9
                else:
                    alice = True
                    if i < mid:
                        if front < back:
                            front += min(9, back - front)
                    else:
                        if front > back:
                            back += min(9, front - back)
        print(front, back)
        return front != back


solution = Solution()
res = solution.sumGame(num="25??")
print(res)
