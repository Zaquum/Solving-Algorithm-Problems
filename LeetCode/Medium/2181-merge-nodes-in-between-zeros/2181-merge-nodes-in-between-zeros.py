# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = []
        tmp_sum = 0
        cur_head = None
        while head:
            if head.val == 0:
                if tmp_sum != 0:
                    tmp_head = ListNode(val=tmp_sum)
                    if cur_head:
                        cur_head.next = tmp_head
                        cur_head = cur_head.next
                    else:
                        start_head = tmp_head
                        cur_head = tmp_head
                tmp_sum = 0
            else:
                tmp_sum += head.val
            
            head = head.next
        return start_head