# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next: # 1 -> 2 -> 3 -> 4
            tmp = head.next # 2
            head.next = tmp.next # 1 -> 3
            tmp.next = head # 2 -> 1
            tmp.next.next = self.swapPairs(head.next)
            return tmp
        return head