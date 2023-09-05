"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        # Step 1: Create a deep copy of each node and place it next to the original node
        current = head
        while current:
            new_node = Node(current.val, current.next)
            current.next = new_node
            current = new_node.next
        
        # Step 2: Set the random pointers of the copied nodes
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next

        # Step 3: Separate the copied nodes from the original nodes
        copied_head = head.next
        current = head
        while current:
            temp = current.next
            current.next = temp.next
            if temp.next:
                temp.next = temp.next.next
            current = current.next

        return copied_head