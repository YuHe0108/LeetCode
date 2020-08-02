"""
0623:
合并两个已经排序后的链表

Example:
    Input: 1->2->4, 1->3->4
    Output: 1->1->2->3->4->4
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1, p2 = l1, l2
        head = p1  # saves the head of list

        # p1: 1->2->4, p2: 1->3->4
        while p1 and p2:
            if p1.val < p2.val:
                if not p1.next:
                    p1.next = p2
                    break
                else:
                    p1 = p1.next
            else:
                tmp = ListNode(p1.val)
                tmp.next = p1.next
                p1.val = p2.val
                p1.next = tmp
                if not p1.next:
                    p1.next = p2.next
                    break
                p2 = p2.next

        return head if head else p2  # if p1 is null
