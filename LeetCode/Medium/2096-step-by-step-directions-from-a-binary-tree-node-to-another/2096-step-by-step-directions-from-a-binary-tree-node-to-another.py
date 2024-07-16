# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def findLCA(root, p, q):
            if not root or root.val == p or root.val == q:
                return root
            left = findLCA(root.left, p, q)
            right = findLCA(root.right, p, q)
            if left and right:
                return root
            return left if left else right

        def findPath(root, target, path):
            if not root:
                return False
            if root.val == target:
                return True
            if root.left and findPath(root.left, target, path):
                path.append('L')
                return True
            if root.right and findPath(root.right, target, path):
                path.append('R')
                return True
            return False
        
        lca = findLCA(root, startValue, destValue)
        # print(lca.val)
        
        startPath = []
        findPath(lca, startValue, startPath)
        # startPath = startPath[::-1]

        destPath = []
        findPath(lca, destValue, destPath)
        destPath = destPath[::-1]

        return 'U' * len(startPath) + ''.join(destPath)