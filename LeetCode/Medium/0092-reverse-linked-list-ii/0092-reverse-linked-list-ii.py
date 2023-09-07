# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        pre = dummy

        for _ in range(left - 1):
            pre = pre.next
        # 1->2->3->4->5
        # p  c  n
        cur = pre.next
        next_node = cur.next

        for _ in range(right - left):
            # 2 -> 4
            cur.next = next_node.next
            # 3 -> 2
            next_node.next = pre.next
            pre.next = next_node
            next_node = cur.next

        return dummy.next