# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n%2 == 0:
            return []
        dp = [[] for _ in range(n+1)]

        def solve(n):
            if dp[n]:
                return dp[n]

            if n==1:
                node = TreeNode(0)
                return [node]
            
            res = []
            for i in range(1,n,2):
                left = solve(i)
                right = solve(n-i-1)

                for l in left:
                    for r in right:
                        root = TreeNode(0)
                        root.left = l
                        root.right = r
                        res.append(root)

            dp[n] = res
            return res
        
        return solve(n)