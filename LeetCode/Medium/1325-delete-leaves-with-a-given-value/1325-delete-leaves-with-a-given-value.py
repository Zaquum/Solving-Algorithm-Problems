# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def dfs(cur):
            if cur is None:
                return None
            cur.left = dfs(cur.left)
            cur.right = dfs(cur.right)
            if cur.left is None and cur.right is None:
                if cur.val == target:
                    return None
            return cur
        return dfs(root)