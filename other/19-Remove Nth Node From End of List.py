"""
0622 第19题：
移除列表中的第 n 个节点

Given linked list: 1->2->3->4->5, and n = 2. n 表示移除第 2 个节点
After removing the second node from the end, the linked list becomes 1->2->3->5.
"""

"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, value=0, next_value=None):
        self.value = value
        self.next_value = next_value


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head is None:
            return None

        result = []

        def get_value(node):
            if type(node) is int:  # 如果链表的下一个值为整数不是链表，说明结束了
                result.append(node)
            else:
                result.append(node.value)
                node = node.next_value
                get_value(node)

        get_value(head)
        result.pop(n - 1)  # 移除第几号链表的值, 根据索引删除值
        depth = len(result)  # 链表的深度
        print(result)

        # 连接链表
        return_node = ListNode(result[0])
        next_node = return_node.next_value
        for i in range(1, depth):
            if i == depth - 2:
                next_node = ListNode(result[i], result[i + 1])
            else:
                next_node = ListNode()
                next_node.value = result[i]
                next_node.next_value = ListNode()

        get_value(return_node)
        print(result)
        return return_node

"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        size = 0
        cur = p = head
        while cur.next:
            size += 1
            cur = cur.next
            # ?
            if size > n + 0:
                p = p.next


        if size == n:  # 去掉首节点
            return head.next
        else:
            p.next = p.next.next
            return head


s = Solution()
result_ = s.removeNthFromEnd(ListNode(1,
                                      ListNode(2,
                                               ListNode(3,
                                                        ListNode(4,
                                                                 ListNode(5, ListNode(6)
                                                                          )
                                                                 )
                                                        )
                                               )
                                      )
                             , 4)

"""
size = 1
cur = p = head
while cur.next:
    size += 1
    cur = cur.next
    if size > n + 1:
        p = p.next
if size == n:
    return head.next
else:
    p.next = p.next.next
    return head

"""
