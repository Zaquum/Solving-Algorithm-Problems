# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        val_set = set()
        while head:
            if head in val_set:
                return True
            val_set.add(head)
            head = head.next
            # if head.next == None:
        return False