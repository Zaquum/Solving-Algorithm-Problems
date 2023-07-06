# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        length = 0
        val_list = []
        while head:
            length += 1
            val_list.append(head.val)
            head = head.next
        ans = 0
        half_len = length//2
        for i in range(half_len):
            twin_sum = val_list[i] + val_list[-(i+1)]
            if twin_sum > ans:
                ans = twin_sum
        return ans