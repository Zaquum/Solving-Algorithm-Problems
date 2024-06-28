# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def inorder_traversal(root):
            result = []
            def traverse(node):
                if node:
                    traverse(node.left)
                    result.append(node.val)
                    traverse(node.right)
            traverse(root)
            return result

        def sorted_array_to_bst(nums):
            if not nums:
                return None
            mid = len(nums) // 2
            root = TreeNode(nums[mid])
            root.left = sorted_array_to_bst(nums[:mid])
            root.right = sorted_array_to_bst(nums[mid+1:])
            return root

        def balance_bst(root):
            sorted_values = inorder_traversal(root)
            return sorted_array_to_bst(sorted_values)
        
        return balance_bst(root)