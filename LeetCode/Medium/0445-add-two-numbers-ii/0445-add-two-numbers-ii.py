# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverse(head):
            prev = None
            while head:
                nextNode = head.next
                head.next = prev
                prev = head
                head = nextNode
            return prev
                       
        l1, l2 = reverse(l1), reverse(l2)

        # print(l1)
        head = None
        carry = 0

        while l1 or l2 or carry:
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)
            sum_ = val1 + val2 + carry
            carry = sum_ // 10
            out = sum_ % 10
            
            
            tmp = ListNode(out)
            tmp.next = head
            head = tmp

            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)

        return head