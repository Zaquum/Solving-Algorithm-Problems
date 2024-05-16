# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(cur):
            if cur.left is None and cur.right is None:
                return False if cur.val == 0 else True
            if cur.val == 2:
                return dfs(cur.left) or dfs(cur.right)
            else:
                return dfs(cur.left) and dfs(cur.right)
        return dfs(root)