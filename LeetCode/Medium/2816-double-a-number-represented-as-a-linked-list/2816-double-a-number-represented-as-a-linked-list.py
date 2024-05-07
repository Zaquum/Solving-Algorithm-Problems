# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Reverse Linked List
        def reverse_link(head):
            prev = None
            cur = head
            next_node = cur.next
            while cur:
                cur.next = prev
                prev = cur
                cur = next_node            
                if cur:
                    next_node = cur.next
            return prev
        reversed_head = reverse_link(head)
        
        # do * 2
        prev = None
        cur = reversed_head
        carry = 0
        while cur:
            tmp = cur.val * 2 + carry
            if tmp > 9:
                cur.val = tmp - 10
                carry = 1
            else:
                cur.val = tmp
                carry = 0
            prev = cur
            cur = cur.next
        if carry:
            prev.next = ListNode(val=carry)
            prev = prev.next
        # print(prev)
        # print(reversed_head)
        return reverse_link(reversed_head)
            