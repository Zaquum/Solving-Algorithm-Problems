# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def dfs_sum(cur) -> int:
            if cur == None:
                return 0
            return cur.val + dfs_sum(cur.left) + dfs_sum(cur.right)
        
        def dfs_cnt(cur):
            if cur is None:
                return 0
            return 1 + dfs_cnt(cur.left) + dfs_cnt(cur.right)
        # print(dfs_sum(root), dfs_cnt(root))

        # ans = []
        result = 0
        q = deque([root])
        while q:
            cur = q.popleft()
            if dfs_sum(cur)//dfs_cnt(cur) == cur.val:
                # ans.append(cur.val)
                result += 1
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
        # print(ans)
        # return len(ans)
        return result