# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        move = 0
        
        @lru_cache
        def dfs(cur):
            nonlocal move
            
            if cur is None:
                return 0
            
            leftcoin = dfs(cur.left)
            rightcoin = dfs(cur.right)
            
            move += abs(leftcoin) + abs(rightcoin)
            
            return (cur.val - 1) + leftcoin + rightcoin
        
        dfs(root)
        
        return move
            