class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        def dfs(idx, currentXOR):
            if idx == len(nums):
                return currentXOR
            # include current num
            include = dfs(idx + 1, currentXOR ^ nums[idx])
            exclude = dfs(idx + 1, currentXOR)
            return include + exclude
        
        return dfs(0, 0)