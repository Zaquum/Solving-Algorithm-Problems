class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        
        def dfs(idx, cur):
            # exit case
            if idx == len(nums):
                if cur not in self.ans:
                    self.ans.append(cur)
                return
            
            # include
            dfs(idx+1, cur + [nums[idx]])
            # exclude
            dfs(idx+1, cur)
            return
        
        dfs(0, [])
        
        return self.ans
            