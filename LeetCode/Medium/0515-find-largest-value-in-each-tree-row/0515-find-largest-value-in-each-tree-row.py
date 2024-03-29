# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        q = deque([root])
        while q:
            max_val = float('-inf')
            size = len(q)
            changed = False
            for _ in range(size):
                cur = q.popleft()
                if not cur:
                    continue
                max_val = max(max_val, cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
                changed = True
            
            if changed:
                ans.append(max_val)
        return ans