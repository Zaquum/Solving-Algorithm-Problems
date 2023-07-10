# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        mindepth = 100000

        def solve(cur: TreeNode, depth: int):
            nonlocal mindepth
            if cur is None:
                return 
            if cur.left is None and cur.right is None:
                mindepth = min(mindepth, depth)
            if cur.right:
                solve(cur.right, depth + 1)
            if cur.left:
                solve(cur.left, depth + 1)
        
        solve(root, 1)

        return mindepth