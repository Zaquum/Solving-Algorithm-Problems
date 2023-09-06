# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        cnt = 0
        result = [None] * k
         
        node = head
        while node:
            cnt += 1
            node = node.next
        
        n = cnt // k
        r = cnt % k

        node = head
        cur = None
        
        for i in range(k):
            result[i] = node

            for j in range(n):
                cur = node
                node = node.next
            
            if r > 0:
                cur = node
                node = node.next
                r -= 1

            if cur:
                # print(cur.val)
                cur.next = None
        
        return result