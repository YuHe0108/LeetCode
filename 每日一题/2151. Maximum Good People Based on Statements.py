from typing import List


# class Solution:
#     def maximumGood(self, statements: List[List[int]]) -> int:
#
#         def check(state_dict, state_int):
#             # 检测评价为好人的人，说的话是否能够对应 state_dict 的结果
#             for k in range(n):
#                 is_truth = (state_int >> k) & 1  # 有没有在说真话
#                 if is_truth:  # 说真话的人，检查和结论是否有冲突
#                     for m in range(n):
#                         if statements[k][m] == 2:
#                             continue
#                         if m in state_dict and statements[k][m] != state_dict[m]:
#                             return False
#                         state_dict[m] = statements[k][m]
#                 else:
#                     if k not in state_dict:  # 说假话肯定是坏人
#                         state_dict[k] = 0
#                     elif state_dict[k] == 1:  # 结果不能将说假话的判定为好人
#                         return False
#             for k in range(n):
#                 if k not in state_dict:  # 不确定的人说真话，可以将其是做好人
#                     is_truth = (state_int >> k) & 1
#                     if is_truth:
#                         state_dict[k] = 1
#             return True
#
#         n = len(statements)
#         total = 1 << n
#         max_res = 0
#         for i in range(total - 1, -1, -1):  # 每个人在说真话还是谎话，1：真话, 0: 谎话
#             cur = {}
#             reasonable = True
#             for j in range(n):
#                 statement = (i >> j) & 1
#                 if statement == 1:  # 说真话
#                     for v in range(n):
#                         state_v = statements[j][v]
#                         if state_v == 2:
#                             continue
#                         if v in cur and cur[v] != state_v:
#                             reasonable = False
#                             break
#                         cur[v] = state_v
#                 else:
#                     for v in range(n):
#                         state_v = statements[j][v]
#                         if state_v == 2:
#                             continue
#                         if v in cur and cur[v] == state_v:
#                             reasonable = False
#                             break
#                         cur[v] = 1 - state_v
#
#             print(cur, bin(i)[2:])
#             if reasonable and check(cur, i):
#                 # print(cur, bin(i)[2:])
#                 max_res = max(max_res, sum(cur.values()))
#         return max_res

class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        n = len(statements)
        ans = 0
        for state in range(1 << n):
            is_reasonable = True
            count = {}
            cur_state = list(bin(state)[2:])
            cur_state = ['0'] * (n - len(cur_state)) + cur_state
            for i in range(n):
                is_good = (state >> i) & 1
                if is_good:  # 说真话的人一定是好人
                    count[i] = 1
                    for j in range(n):
                        if statements[i][j] == 2:
                            continue
                        if statements[i][j] == 1 and cur_state[j] == '0':
                            is_reasonable = False
                            break
                        if j not in count:
                            count[j] = statements[i][j]
                        else:
                            if statements[i][j] != count[j]:  # 说真话产生了冲突
                                is_reasonable = False
                                break
                if not is_reasonable:
                    break
            cur_cnt = sum(count.values())

            if is_reasonable and cur_cnt == bin(state)[2:].count('1'):
                ans = max(ans, cur_cnt)
        return ans


r = Solution().maximumGood(
    [[2, 1, 2], [1, 2, 2], [2, 0, 2]])
print(r)
