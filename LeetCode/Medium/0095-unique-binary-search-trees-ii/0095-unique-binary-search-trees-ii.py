# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        ans = []
        def solve(start, end):
            if start > end:
                return [None]
            trees = []
            for i in range(start, end+1):
                left = solve(start,i-1)
                right = solve(i+1, end)

                for l in left:
                    for r in right:
                        cur = TreeNode(i)
                        cur.left = l
                        cur.right = r
                        trees.append(cur)
            return trees
        return solve(1,n)