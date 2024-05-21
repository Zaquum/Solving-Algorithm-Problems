class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        def dfs(idx, cur):
            if idx == len(nums):
                if cur not in self.ans:
                    self.ans.append(cur)
                return
            dfs(idx+1, cur + [nums[idx]])
            dfs(idx+1, cur)
            return
        dfs(0, [])
        return self.ans
            