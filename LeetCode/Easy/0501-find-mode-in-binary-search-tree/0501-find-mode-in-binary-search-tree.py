# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        count = {}
        q = deque([root])

        while q:
            cur = q.popleft()
            count[cur.val] = count.get(cur.val, 0) + 1
            
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)

        max_count = max(count.values())

        return [key for key, val in count.items() if val == max_count]