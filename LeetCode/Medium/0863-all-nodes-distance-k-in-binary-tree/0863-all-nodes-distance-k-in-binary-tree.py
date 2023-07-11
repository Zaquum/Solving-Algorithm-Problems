# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parentMap = {}
        visited = set()
        ans = []

        def find_parent(child: TreeNode, parent: TreeNode):
            if child is None:
                return

            parentMap[child] = parent

            find_parent(child.left, child)
            find_parent(child.right, child)

        def find_dist(cur: TreeNode, dist: int) -> int:
            if (cur is None) or (cur in visited) or dist > k:
                return
            
            visited.add(cur)
            if dist == k:
                ans.append(cur.val)

            find_dist(cur.left, dist+1)
            find_dist(cur.right, dist+1)
            find_dist(parentMap[cur], dist+1)
        find_parent(root, None)
        find_dist(target, 0)

        return ans

            