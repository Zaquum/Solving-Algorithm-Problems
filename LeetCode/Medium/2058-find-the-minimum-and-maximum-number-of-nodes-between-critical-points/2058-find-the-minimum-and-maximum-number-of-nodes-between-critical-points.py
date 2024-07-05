# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = head
        cur = head.next
        next_ = head.next.next

        criticals = []
        i = 1
        while next_:
            # minimum
            if cur.val < prev.val and cur.val < next_.val:
                criticals.append(i)
            # maximum
            if cur.val > prev.val and cur.val > next_.val:
                criticals.append(i)
            prev = prev.next
            cur = cur.next
            next_ = next_.next
            i += 1
            
        if len(criticals) < 2:
            return [-1, -1]
        
        min_dist = float('inf')
        for i in range(1, len(criticals)):
            min_dist = min(min_dist, criticals[i]-criticals[i-1])
        
        max_dist = criticals[-1] - criticals[0]
        return [min_dist, max_dist]