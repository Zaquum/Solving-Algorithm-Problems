# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        q = deque([root])
        while q:
            max_val = float('-inf')
            for _ in range(len(q)):
                cur = q.popleft()
                if not cur:
                    continue
                max_val = max(max_val, cur.val)
                q.extend([cur.left, cur.right])
            if max_val != float('-inf'):
                ans.append(max_val)
        return ans