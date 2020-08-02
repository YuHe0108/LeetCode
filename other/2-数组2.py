"""
0620, 第二题:
题目描述: 给了一个链表, 求两个链表的和, 仍然以链表的形式返回
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4): 个、十、百
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807。
"""


# class ListNode:
#     # 创建一个列表
#     def __init__(self, value=0, next_value=None):
#         self.value = value
#         self.next_value = next_value
#
#
# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         value_1_list = self.return_node_value(l1)
#         value_2_list = self.return_node_value(l2)
#         len_1 = len(value_1_list)
#         len_2 = len(value_2_list)
#         min_len = min(len_1, len_2)
#
#         result_node = ListNode(0)
#         next_node = result_node
#         for i in range(min_len):
#             sum_value = value_1_list[i] + value_2_list[i] + next_node.value
#             next_node.value = sum_value % 10
#             if i != min_len - 1:  # 最后输出时:
#                 if sum_value >= 10:
#                     next_node.next_value = ListNode(value=1)
#                 else:
#                     next_node.next_value = ListNode(value=0)
#                 next_node = next_node.next_value
#             else:
#                 if sum_value > 10:
#                     next_node.next_value = 1
#         return result_node
#
#     @staticmethod
#     def get_next_value(node):
#         if type(node) is ListNode:
#             node_next_value = node.value
#         elif type(node) is int:
#             node_next_value = node
#         else:  # None
#             node_next_value = 0
#         return node_next_value
#
#     @staticmethod
#     def get_node_len(node):
#         """获取一个node的长度"""
#         i = 2
#         if type(node.next_value) is None:  # 也有可能只有一个值
#             return 1
#         if type(node.next_value) is not int:
#             i += 1
#         return i
#
#     @staticmethod
#     def return_node_value(node_list):
#         next_value = node_list.next_value
#         values = [node_list.value]
#         while True:
#             if next_value is None:
#                 break
#             elif type(next_value) is int:
#                 values.append(next_value)
#                 break
#             else:
#                 values.append(next_value.value)
#                 next_value = next_value.next_value
#         return values
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        value_1_list = self.return_node_value(l1)
        value_2_list = self.return_node_value(l2)
        len_1 = len(value_1_list)
        len_2 = len(value_2_list)
        min_len = min(len_1, len_2)

        result_node = ListNode(0)
        next_node = result_node
        if min_len > 1:
            for i in range(min_len):
                sum_value = value_1_list[i] + value_2_list[i] + next_node.val
                next_node.val = sum_value % 10
                if i != min_len - 1:  # 最后输出时:
                    if sum_value >= 10:
                        next_node.next = ListNode(val=1)
                    else:
                        next_node.next = ListNode(val=0)
                    next_node = next_node.next
                else:
                    if sum_value > 10:
                        next_node.next = 1
        else:
            sum_value = value_1_list[0] + value_2_list[0]
            if sum_value >= 10:
                result_node = ListNode(sum_value % 10, 1)
            else:
                result_node = ListNode(sum_value % 10)
        return result_node

    @staticmethod
    def get_next_value(node):
        if type(node) is ListNode:
            node_next_value = node.val
        elif type(node) is int:
            node_next_value = node
        else:  # None
            node_next_value = 0
        return node_next_value

    @staticmethod
    def get_node_len(node):
        """获取一个node的长度"""
        i = 2
        if type(node.next_value) is None:  # 也有可能只有一个值
            return 1
        if type(node.next_value) is not int:
            i += 1
        return i

    @staticmethod
    def return_node_value(node_list):
        next_value = node_list.next
        values = [node_list.val]
        while True:
            if next_value is None:
                break
            elif type(next_value) is int:
                values.append(next_value)
                break
            else:
                values.append(next_value.val)
                next_value = next_value.next
        return values


if __name__ == '__main__':
    node_1 = ListNode(5)
    node_2 = ListNode(5)
    s = Solution()
    result = s.addTwoNumbers(node_1, node_2)
    print(result.val, result.next)
    print(s.return_node_value(result))


# 返回的结果: result_node: 各位数字
# sum_value = l1.value + l2.value
# result_node = ListNode((l1.value + l2.value) % 10)  # 个位
#
# # 获取两个node list的长度
# node_1_length = self.get_node_len(l1)
# node_2_length = self.get_node_len(l2)
# max_length = max(node_1_length, node_2_length)
# min_length = min(node_1_length, node_2_length)
#
# # list node的下一位数字: 有是node、int或者None
# node_1_next = l1.next_value
# node_2_next = l2.next_value
#
# for i in range(min_length):
#     node_1_next_value = self.get_next_value(node_1_next)
#     node_2_next_value = self.get_next_value(node_2_next)
#
#     if i != min_length - 1:
#         if type(node_1_next_value) is int or type(node_2_next_value) is int:  # 如果两个有一个为整数
#             # 求下一位数字
#             if sum_value > 10:
#                 result_node.next_value = ListNode((node_1_next_value + node_2_next_value + 1) % 10, 1)
#             else:
#                 result_node.next_value = ListNode((node_1_next_value + node_2_next_value) % 10, 0)
#     else:
#         pass
#
#     sum_value = node_1_next_value + node_2_next_value
#
# return result_node


